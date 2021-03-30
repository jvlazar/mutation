from pathlib import Path

fileName = (input("What is the name of your input file? (enter with .txt) "))
out = (input("What is the name of your output file? (enter with .txt) "))

fName = open(fileName, "r")
oName = open(out, "w")


target = input("What amino acid do you want to delete?: ")
target = target.upper() # converts input to uppercase
position = int(input("What position do you want to delete?: "))

count = 1

while True: # loop indefinitely
    char = fName.read(1)

    if not char: # if the value of char is null, exit out of the loop
        break

    if char == ">": # if the file is in FASTA format read until you reach "]"
        while True:
            if char == "]":
                char = fName.read(1)
                break
            else:
                char = fName.read(1)

    if count != position: # when not at the desired position, add 1 to count
        if char != "\n":
            count = count + 1
            print("The position is " + str(count) + " " + char)
        elif char == "\n": # if the character is a newline, don't change the count
            pass

        oName.write(char) # write the character to the output file


    elif count == position and char == target:
        print("The amino acid at " + str(position) + " is " + char) # letting the user know that the aa is there
        count = count + 1 # increasing count



fName.close()
oName.close()
