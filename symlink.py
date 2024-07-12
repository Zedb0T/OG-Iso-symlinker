import os
import sys
import subprocess
import shutil

def create_junction(target, link_name):
    try:
        # Use subprocess to call mklink for creating a junction point
        subprocess.check_call(['cmd', '/c', 'mklink', '/J', link_name, target])
        print(f'Junction created: {link_name} -> {target}')
    except subprocess.CalledProcessError as e:
        print(f'Error creating junction: {e}')

def remove_directory_or_link(path):
    try:
        if os.path.islink(path):
            os.unlink(path)  # Remove symlink
            print(f'Removed symlink: {path}')
        elif os.path.isdir(path):
            shutil.rmtree(path)  # Remove directory
            print(f'Removed directory: {path}')
    except OSError as e:
        print(f'Error removing {path}: {e}')

if __name__ == "__main__":
    # Determine the AppData path dynamically
    appdata_path = os.path.expandvars('%APPDATA%')

    # Define the target directories and their corresponding symlink names
    targets = {
        os.path.join(appdata_path, 'OpenGOAL-Mods', '_iso_data', 'jak1'): 'jak1',
        os.path.join(appdata_path, 'OpenGOAL-Mods', '_iso_data', 'jak2'): 'jak2',
        os.path.join(appdata_path, 'OpenGOAL-Mods', '_iso_data', 'jak3'): 'jak3'
    }

    if len(sys.argv) != 2:
        print("Usage: python symlink.py <target_directory>")
        sys.exit(1)

    target_directory = sys.argv[1]

    # Check if "iso_data" subdirectory exists in the target directory
    iso_data_dir = os.path.join(target_directory, 'iso_data')
    if not os.path.exists(iso_data_dir):
        for target, link_name in targets.items():
            link_path = os.path.join(target_directory, link_name)
            remove_directory_or_link(link_path)  # Remove existing directory or symlink
            create_junction(target, link_path)
    else:
        for target, link_name in targets.items():
            link_path = os.path.join(iso_data_dir, link_name)
            remove_directory_or_link(link_path)  # Remove existing directory or symlink
            create_junction(target, link_path)
