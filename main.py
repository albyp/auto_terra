import logging
import pyautogui as pg
import threading
from pynput import mouse
import time

# Import window functions
from funcs.state import stop_script
from funcs.window import get_terra_window, focus_terra
from funcs.utils import return_mouse_pos, check_interrupt, on_right_click, processing_confirm
from funcs.inputs import new_lidar_mission, name_mission, input_mission_data, start_processing, ok_processing
from funcs.base_settings import select_base_settings, change_coordinate_system, input_coordinates
from funcs.parameters import modify_parameters

# Set logging level
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Import config
from config import MOVE_OUTPUTS, TERRA_OUTPUT_DIR, TERRA_ACCOUNT, PROJECT_OUTPUT_DIR, EPSG, BASE_COORDINATES, AUTO_ACCEPT
from config import MISSIONS
PROCESS_BASE = True

def main() -> None:
    logging.debug("Saving the initial mouse coordinates.")
    initial_mouse_pos = pg.position()

    # Start interrupt listener threads
    interrupt_thread = threading.Thread(target=check_interrupt, daemon=True)
    interrupt_thread.start()

    mouse_listener = mouse.Listener(on_click=on_right_click)
    mouse_listener.start()

    logging.info("Script started. Press ESC or right-click to stop.")

    while not stop_script:
        try:
            # Check for Terra and focus application
            window = get_terra_window()
            focus_terra(window)

            for mission in MISSIONS:
                focus_terra(window)

                # Create new mission and set up for import
                new_lidar_mission(window)
                name_mission(mission[0], window)

                # Import LiDAR data to project
                input_mission_data(mission[1], window)
                
                # Process base settings
                if PROCESS_BASE:
                    logging.info("Executing process base functions...")
                    select_base_settings(window)
                    change_coordinate_system(EPSG, window)
                    input_coordinates(BASE_COORDINATES, window)

                modify_parameters(window)

                if AUTO_ACCEPT == True:
                    start_processing()
                    ok_processing(window)
                else:
                    start_processing()
                    if len(MISSIONS) > 1:
                        time.sleep(1)
                        ans = processing_confirm()
                        if ans:
                            ok_processing(window)
                        else: 
                            logging.info('Processing aborted...')
                            return_mouse_pos(initial_mouse_pos)
                            break


                return_mouse_pos(initial_mouse_pos)
            break

        except Exception as e:
            logging.error(f"Error during execution: {e}")
            break

    return_mouse_pos(initial_mouse_pos)

    # Move outputs to Terra output directory
    if MOVE_OUTPUTS:
        logging.info("Moving outputs from Terra output directory to project outputs.")
        
        terra_outputs = os.path.join(TERRA_OUTPUT_DIR, TERRA_ACCOUNT)

        for mission in MISSIONS:
            mission_name = mission[0]
            mission_output_dir = os.path.join(terra_outputs, mission_name, 'lidars', 'terra_las')
            if 'cloud_merged.las' in os.listdir(mission_output_dir):
                merged_cloud = os.path.join(mission_output_dir, 'cloud_merged.las')
                os.rename(merged_cloud)
                output_path = os.path.join(mission[1], mission_name, PROJECT_OUTPUT_DIR)
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                shutil.move(merged_cloud, output_path)
                logging.info(f"Moved {merged_cloud} to {output_path}")

        import shutil
        import os

# Run program
if __name__ == '__main__':
    main()