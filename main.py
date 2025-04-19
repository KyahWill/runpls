#!/usr/bin/env python3
import sys
import os
import yaml

def process_command_line():
    arguments = sys.argv[1:]
    return arguments

def get_current_directory():
    current_directory = os.getcwd()
    return current_directory

def get_runpls_file(filename:str, search_path:str=".") :
    """
    Searches for a file with the given filename in the specified search path and its subdirectories.

    Args:
        filename (str): The name of the file to search for.
        search_path (str): The starting directory for the search (default: current directory).

    Returns:
        str: The absolute path to the file if found, or None if not found.
    """
    for root, _, files in os.walk(search_path):
        if filename in files:
            return os.path.abspath(os.path.join(root, filename))
    return None


def get_local_runpls_commands(filepath):
    """
    Opens a YAML file and prints its contents.

    Args:
        filepath (str): The path to the YAML file.
    """
    try:
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)  # Use safe_load to avoid security risks
            if data is not None: #yaml.safe_load returns None if the file is empty.
                print("YAML FILE WITH CONTENTS")
                # print(yaml.dump(data, default_flow_style=False)) #dump it back to yaml, for easy readability.
            else:
                print("YAML file is empty.")
            return data

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML format in '{filepath}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    arguments = process_command_line()
    current_directory = get_current_directory()
    
    local_runpls_file = get_runpls_file(filename="runpls.yaml",search_path=".")
    local_runpls_commands = {}
    if(local_runpls_file is not None):
        local_runpls_commands = get_local_runpls_commands(local_runpls_file)

    print("Command line arguments:", arguments)
    print("Current directory:", current_directory)
    #print("runpls file", local_runpls_file)
    #print("runpls commands:", local_runpls_commands)
