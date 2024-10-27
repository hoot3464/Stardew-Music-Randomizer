
import os
import random
import shutil

# use with bulk_random.py
# this script will essentially replace the current content.json in Piano Valley folder to a random one



def content_string():
    list = []
    c = "content"
    j = ".json"
    
    for i in range(100):
        list.append(c + str(i+1) + j)
        
    
    # get one random item from the list
    random_item = random.choice(list)
    
    return random_item
    

def main():
    
    contents_folder = r"C:\Users\Administrator\Documents\Python Stuff\Stardew Music Randomizer\contents" # has 100 content.json files
    mods_folder = r"C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\Mods\[CP] Piano Valley"
    
    # gets a random content.json from the contents folder and renames it to content.json
    new_content = content_string()
    
    # deletes the old content.json    
    old_content = os.path.join(mods_folder, "content.json")
    
    if os.path.exists(old_content):
        print("content.json detected. Deleting now...")
        os.remove(old_content)
    else:
        print("content.json not detected. Continuing...")
    
    # copies a random content.json to the mods folder
    content_path = os.path.join(contents_folder, new_content)
    
    try:
        shutil.copy(content_path, mods_folder)
        print("File copied successfully.")
    except Exception as e:
        print(f"Failed to copy file: {e}")
    
    # renames the new content.json to content.json
    new_content_path = os.path.join(mods_folder, new_content)
    os.rename(new_content_path, os.path.join(mods_folder, "content.json"))
    input("New content.json has been added. Press enter to exit.")
    

if __name__ == "__main__":
    main()