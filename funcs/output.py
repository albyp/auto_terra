import logging
import os

def rename_merged_cloud(output_filename) -> None:
    """
    Renames the merged cloud file to the specified output filename.
    
    This function searches for files with the extension '.las' and renames them
    to the specified output filename. It is used to ensure that the merged cloud
    file has a consistent name.

    Args:
        output_filename (str): The desired name for the merged cloud file.

    Returns:
        None
    """
    logging.info("Renaming merged cloud file.")
    for file in os.listdir():
        if file.endswith('.las'):
            os.rename(file, output_filename)
            logging.debug(f"Renamed file: {file} to {output_filename}")
            break


def delete_unmerged_files() -> None:
    """
    Deletes unmerged files in the current directory.
    
    This function searches for files with the extension '.las' and deletes them.
    It is used to clean up unmerged files after processing.

    Returns:
        None
    """
    logging.info("Deleting unmerged files.")
    for file in os.listdir():
        if file.endswith('.las'):
            os.remove(file)
            logging.debug(f"Deleted file: {file}")