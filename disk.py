import os


""" File path to the file where the version number is stored """
data_directory = 'data'

""" File path to the file where the version number is stored """
filename = os.path.join(data_directory, 'trellis_version.txt')


def read_version():
    """
    Attempts to read the version from the 'data/trellis_version.txt' file.
    If this file doesn't exist, it creates it.

    Returns:
        str or None: stored version of trellis
    """
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    if not os.path.exists(filename):
        open(filename, 'a').close()
        return None

    with open(filename, 'r') as version_file:
        version = version_file.read()
        return version


def write_version(version):
    """
    Writes the version to the 'data/trellis_version.txt' file

    Args:
        version (str): trellis version to be stored to disk
    """
    with open(filename, 'w') as version_file:
        version_file.write(version)
