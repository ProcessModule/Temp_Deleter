import os
import shutil
import glob

def clean_system_temporary_files():
    temporary_locations = [
        os.path.expandvars(r'%temp%'),
        os.path.join(os.getenv('SYSTEMROOT'), 'Temp'),
        os.path.join(os.getenv('SYSTEMROOT'), 'Prefetch'),
        os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Temp')
    ]

    for location in temporary_locations:
        if not os.path.exists(location):
            print(f"Directory not found: {location}")
            continue

        process_temporary_location(location)

def process_temporary_location(folder_path):
    try:
        items_to_remove = glob.glob(os.path.join(folder_path, '*'))
        
        for item in items_to_remove:
            try:
                remove_temporary_item(item)
            except PermissionError:
                print(f"Access denied (File in use): {item}")
            except Exception as error:
                print(f"Removal failed: {item}")
                print(f"Error details: {str(error)}")
                
    except Exception as error:
        print(f"Failed to access folder: {folder_path}")
        print(f"Error details: {str(error)}")

def remove_temporary_item(item_path):
    try:
        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"Removed file: {item_path}")
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Removed Directory: {item_path}")
    except Exception as error:
        raise error

def main():
    print("starting system cleanup...")
    print("-" * 50)
    
    clean_system_temporary_files()
    
    print("-" * 50)
    print("cleanup process completed")

if __name__ == "__main__":
    main()
