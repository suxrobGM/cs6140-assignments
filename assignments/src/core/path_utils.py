import os

def get_data_path(relative_path: str) -> str:
    """
    Get the full path to a file in the dataset directory.
    :param relative_path: The path to the file relative to the dataset directory including the file name and extension.
    """
    return os.path.join(os.path.dirname(__file__), "../../dataset", relative_path)
