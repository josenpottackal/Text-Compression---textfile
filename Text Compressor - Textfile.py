# File Name: Text Compression - textfile.py
# Purpose: Program can compresses and decompresses textfiles
# Date: 2015-01-15
# Last modified: 2020-01-15
# Author: Josen Pottackal
# Copy right no copyright
# Version: 1.0


# Compresses textfile
# @param textfile input textfile name.
def compression(textfile):  # defined function which compress an inputted notepad file.
    textfile_open = open(textfile, 'r')
    textfile_edit = (textfile_open.read().split())
    print("Textfile contents:", textfile_edit, "\n")

    singular_words = []  # creates a list of singular words from within the users notepad file.
    [singular_words.append(x) for x in textfile_edit if x not in singular_words]
    print("Singular words within textfile:", singular_words, "\n")

    positions = []  # each value in "textfile_edit" is replaced with the value that it represents in "singular_words".
    [positions.append(str(singular_words.index(x) + 1)) for x in textfile_edit]
    position_string = (",".join(positions))
    print('Compression:', position_string, '\n')

    compression = open("Compression.txt", 'w')
    compression.write(position_string)  # writes a notepad file which stores the contents of "position_string".
    compression.close()
    singular_string = (" ".join(singular_words))

    wordfile = open("Individual_words.txt", 'w')
    wordfile.write(singular_string)  # writes a notepad file which stores the contents of "singular_string".
    wordfile.close()

# Decompresses textfile
# @param inputTextfile input textfile name.
# @param wordfile wordfile name.
def decompression(inputTextfile, wordfile):  # defined function which decompress a compressed notepad file.
    positions_open = open(inputTextfile, "r")
    positions_edit = (positions_open.read().split(","))  # the notepad file's contents are read in and split into a list of words.
    positions_integer = [int(i) for i in positions_edit]  # converts "positions_edit" from a string into a list of integers
    print('Textfile contents:', positions_edit, "\n")

    words_open = open(wordfile, "r")
    singular_words = (words_open.read().split())  # the notepad file's contents are read in and split into a list of words.
    print("Singular words within textfile:", singular_words, "\n")

    decompress = []  # each value in "positions_edit" is replaced with the value that it represents in "singular_words".
    for pos in positions_integer:
        decompress.append(singular_words[pos - 1])
    print('Decompression:', " ".join(decompress), '\n')


while True:
    print('This program compresses, and decompresses a notepad file')
    print('1: Compression')
    print('2: Decompression\n')

    answer = input('Enter which function you would like to perform:\n')

    if answer not in ("1", "2"):
        print('Sorry I didn’t understand, please try again\n')

    elif answer == "1":
        answer = input('Would you like to use the default notepad file ("textfile_input.txt")(yes/no):\n').lower()
        if answer not in ("yes", "no"):
            print("Sorry I didn’t understand, please try again\n")
            continue
        elif answer == "yes":
            textfile = "textfile_input.txt"
        else:
            textfile = input("Enter notepad file name:\n")
        compression(textfile)

    else:
        answer = input('Would you like to use the default compressed textfile(Compression.txt)and the default list of '
                       'words textfile(Individual_words.txt)?(yes/no):\n').lower()
        if answer not in ("yes", "no"):
            print('Sorry I didn’t understand, please try again:\n')
            continue
        elif answer == "yes":
            integerTextfile = "Compression.txt"
            wordTextFile = "Individual_words.txt"
        else:
            integerTextfile = input('what is the name of the compressed textfile?\n')
            wordTextFile = input('what is the name of the textfile or words?\n')
        decompression(integerTextfile, wordTextFile)

    while True:
        answer = input("Would you like to restart the program?(yes/no):\n").lower()
        if answer in ("yes", "no"):
            break
        print("Sorry I didn’t understand, please try again:\n")
    if answer == "yes":
        continue
    else:
        print("End program\n")
        break
