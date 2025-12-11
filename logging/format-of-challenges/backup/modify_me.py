import os


# Given a string directory value, list all the files using 'ls' with os.system(...).
def list_files(directory):
    os.system(f'ls {directory}')