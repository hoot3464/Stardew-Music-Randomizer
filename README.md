# Welcome to My Music Randomizer!

This is a python script that generates a **`content.json`** to be used in the Piano Valley mod for Stardew Valley.

There's a few things you need to know before using this program:

## Here is what's inside:

- Ensure these files are in the folder:
  - `new_content.py`
  - `songs_list.txt`
  - `music_ids.txt`
  - `template.txt`
  - `stardew_valley_ids.xlsx`
  - A folder called `assets`
  - The `.dist` folder is something VSCode does

- UPDATED: see changelog.txt for details. New python scripts added for more functionality. Make sure to take a look and change file paths in the scripts for your needs.

- This script actually creates a generalized version of the Piano Valley mod, which simply replaces a lot of the music in the game with soft beautiful piano versions of the tunes you normally hear. I'm a huge fan and I'm glad I found out about this mod. Huge shoutouts to the people who made it. You can find out more here: https://www.nexusmods.com/stardewvalley/mods/7103

- **Music IDs**: These are targets for playing certain music at specific seasons, times of day, or locations.

- Refer to the Excel spreadsheet and navigate to the **Music Bank IDs** tab to learn more. The provided `music_ids.txt` has 28 entries I found most useful.
  - Note: The tune **"springtown"** almost always plays if the weather is sunny and it's after 12 PM and you're in town.

- **`songs_list.txt`**: A list of songs with a name and `.ogg` file extension.

- If you have lots of songs you want to put in the game, consider setting up multiple folders and make sure to edit the folder names. My assets folder has 100 songs in it and it might be too many lol.

- If you have a folder full of songs with no subfolders, copy everything and paste into a text file and remove folder name prefixes. Ensure no file names have whitespaces. This is how I made `songs_list.txt`.

- **`template.txt`**: Used to make a dictionary object that Python can use. **Do not delete this.**

- **Note**: The script uses a randomizer function so that every time you run the script, you could make a new **`content.json`** file and listen to different music every time you play! However the function doesn't check for duplicates, so there could be the same song paired with different music IDs. You can apply the `unique_randomizer` function instead to ensure no duplicates.

- After you finish using the script, make sure to replace the current **`content.json`** with the new one, and make sure it has the exact same assets folder used in the script or else the game will crash. I recommend backing up the Piano Valley mod somewhere before doing all this.

- The **`content.json`** and assets folder should be located here: **`C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\Mods\[CP] Piano Valley`** or wherever your game is located. Also make sure you have SMAPI and Content Patcher installed.

- That's all! I hope you enjoy! I had a blast finding music that fits the calm comfortable vibes of the game, as well as funky upbeat tunes to jam out to make me even more productive. There are truly endless possibilities for what music to hear while playing.

- But on that note, this game already has some nice music in it. Credit to ConcernedApe for this game and the lovely soundtrack that comes with it.

## JSON Structure

The JSON data is a single object containing several key-value pairs.

- **Format**: Matches the Content Patcher version, so it doesn't change.
- **Changes**: Part of the new 1.6 update, the JSON structure has one value, which is the rest of the data.
- **Action**: How Content Patcher finds the data to patch.
- **Target**: How Content Patcher finds the data to patch.
- **Entries**: The most complex part of the JSON. This dictionary contains several key-value pairs and is what the script modifies. My `music_ids.txt` has 28 items, so this section has 28 entries. Each entry is a dictionary with a name and ID, which are always the same.
- **Id**: The music ID target.
- **Category**: It's all about the music!
- **FilePaths**: The actual file paths. The format is `["{{AbsoluteFilePath: assets/{something}.ogg}}"]`. **IMPORTANT**: **THIS ENTRY MUST BE FORMATTED THIS WAY OR THE GAME WILL CRASH.** It's because the game will try to find targets from the Content folder inside Stardew Valley rather than the correct target.
- **Looped**: Default True. Determines if the music loops.
- **StreamedVorbis**: NOTE: in the updated version, all values have been set to FALSE instead of TRUE to hopefully prevent the game from crashing.

