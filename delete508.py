from pathlib import Path

fileName = (input("What is the name of your input file? "))
out = (input("What is the name of your output file? "))

fName = open(fileName, "r")
oName = open(out, "w")


target = input("State the amino acid you are looking to delete: ")
position = int(input("State the position of the amino acid to be deleted "))
count = 1


while True: # loop indefinitely

    char = fName.read(1) # read the char 1 byte at a time
    if not char: # if the value of char is null, exit out of the loop
        break

    if count != position: # when not at the desired position, add 1 to count
        if char != "\n":
            count = count + 1
        elif char == "\n": # if the character is a newline, don't change the count
            pass

        oName.write(char) # write the character to the output file


    elif count == position and char == target: # if the count is the same as the position and the character is the target, do not write to output
        print("The amino acid at 508 is " + char) # letting the user know that the aa is there
        count = count + 1 # increasing count


fName.close()
oName.close()
