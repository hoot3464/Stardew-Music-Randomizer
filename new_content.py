import json
import random
import os

# Music Randomizer
# Make sure to look at the README before using this script


# this function essentially does the magic. it changes the file paths in the content.json
def modify_file_paths(template_data, new_file_names):
    changes = template_data.get("Changes", [])
    if changes:
        entries = changes[0].get("Entries", {})
        for entry_id, entry_data in entries.items():
            file_paths = entry_data.get("FilePaths", [])
            if file_paths:
                file_paths.clear()  # Remove the old file path
                if entry_id in new_file_names:  # Check if entry_id is a valid index
                    new_file_path = "{{AbsoluteFilePath: assets/" + new_file_names[entry_id] + "}}"
                    file_paths.append(new_file_path)  # Add the new file path


# a function to get a list of music id's as well as song filepaths 
# text files must be in the same folder and have the correct names
def get_lists():
    
    songs_list = []
    music_ids = []
    
    with open("songs_list.txt", "r") as f:
        for line in f:
            songs_list.append(line.strip())
            
    with open("music_ids.txt" , "r") as f:
        for line in f:
            music_ids.append(line.strip())
            
    return songs_list, music_ids


# function to generate unique songs for each music id. its where the magic happens!
def randomizer(songs_list, music_ids):
    
    new_list = []
    
    for i in range(len(music_ids)-1):
        k = random.randint(0, len(songs_list)-1)
        new_list.append(songs_list[k])
        
    # new songs list
    return new_list
    

# optional function to generate unique songs for each music id so that there are no duplicates
def unique_randomizer(songs_list, music_ids):
    
    new_list = []
    
    for i in range(len(music_ids)-1):
        k = random.randint(0, len(songs_list)-1)
        if songs_list[k] not in new_list:
            new_list.append(songs_list[k])
            
    # new songs list
    return new_list


def main():
    
    # template for any new content.json, it creates a dictionary that python can use
    with open("template.txt", "r") as f:
        data = json.load(f)
        
        
    # important! this part is set to open specific text files
    # songs_list.txt and music_ids.txt must be in the same folder as this script
    songs, ids = get_lists()
    
    
    # make a new list of songs 
    # new_songs_list = unique_randomizer(songs, ids)
    new_songs_list = randomizer(songs, ids)
    

    # dictionary with music id's and different songs made by randomizer
    entries = dict(zip(ids, new_songs_list))
    
    # sets up new content.json
    modify_file_paths(data, entries)
    
    # check if content.json exists and if it does, delete it and make a new one. Otherwise make a new one
    # you could remove this if you want, it was used for testing. 
    # you could also modify most of this main function to loop several times and make several content.jsons
    if os.path.exists("content.json"):
        os.remove("content.json")
        print("content.json successfully deleted")
        print("new content.json being created...")    
        
    # generates content.json with good formatting
    with open("content.json", "w") as f:
        json.dump(data, f, indent=4, separators=(',', ': '))
        
    print("content.json successfully generated!")

    
    
if __name__ == "__main__":
    main()
