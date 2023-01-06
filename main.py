import random

# 1. open a file with the lyrics - how to open a file?
# 1.1 make a copy from original file
# 2. work on each file's line
# 3. remove a random word from each file's line
# 4. export results as new file

try: 
    # open file in current directory
    lyrics = open('crazy.txt')

    # read the file
    read_lyrics = lyrics.readlines()
    read_lyrics_copy = read_lyrics
    for line in read_lyrics_copy:
        selected_word = len(line.split())
        #print("-")
        line.split()
        #print(random.randint(1,selected_word))
        print(type(line))

    #print(read_lyrics_copy)

finally:
    # close file
    lyrics.close()