import os


# simple script to get the songs list from assets folder into a text file called songs_list.txt
# use this if you don't already have a songs_list txt file but you have assets folder


def get_song_list():

    songs_list = []

    for root, dirs, files in os.walk("assets"):
        for file in files:
            if file.endswith(".ogg"):
                songs_list.append(file)
                
    with open("songs_list.txt", "w") as f:
        for song in songs_list:
            f.write(song + "\n")


def main():
    get_song_list()

if __name__ == "__main__":
    main()