import os
import shutil

def empty_iso_data(path):
    total_saved_space = 0
    print("\nWARNING: DELETING FILES. PROCEED AT YOUR OWN RISK.")
    print("This script will empty the 'iso_data' folder.\n")
    input("Press Enter to continue or Ctrl+C to abort...")

    for root, dirs, files in os.walk(path):
        if 'iso_data' in dirs:
            iso_data_path = os.path.join(root, 'iso_data')
            try:
                total_saved_space += sum(os.path.getsize(os.path.join(iso_data_path, f)) for f in os.listdir(iso_data_path))

                for filename in os.listdir(iso_data_path):
                    file_path = os.path.join(iso_data_path, filename)
                    try:
                        if os.path.isfile(file_path):
                            # Check if the file is .gitignore and skip it
                            if filename == '.gitignore':
                                continue
                            os.remove(file_path)
                            print(f"Deleted file {file_path}")
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                            print(f"Deleted directory {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")

                print(f"Emptied 'iso_data' folder at {iso_data_path}")
            except Exception as e:
                print(f"Error emptying 'iso_data' folder at {iso_data_path}: {e}")

    print(f"\nTotal space saved: {total_saved_space / (1024*1024)} MB")

if __name__ == "__main__":
    base_path = os.path.expanduser("~")
    relative_iso_data_path = os.path.join("Documents", "Github")

    # You can just hardcode this to whereever you have all your repos
    full_path = os.path.join(base_path, relative_iso_data_path)
    empty_iso_data(full_path)
