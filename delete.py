from pathlib import Path
import sys


try:
    fName = open(sys.argv[1], "r")
    oName = open(sys.argv[2], "w+")

    if len(sys.argv) !=3:
        print("An input and output file name must be provided")
        quit()

    fasta = False

    target = input("What amino acid do you want to delete?: ")
    target = target.upper() # converts input to uppercase
    position = int(input("What position do you want to delete?: "))


    count = 1 # initialize count for the input file
    total_count = 1
    out_count = 1 # initialize count for the output file
    mutation = 0
    deleted = False

    while True: # loop indefinitely
        char = fName.read(1)

        if not char: # if the value of char is null, exit out of the loop
            break

        if char == ">": # if the file is in FASTA format read until you reach "]"
            fasta = True
            count = 1 # initialize count to 1 for each new organism
            out_count = 1 # initialize output count to 1 for each new organism

            while True:

                if char == "]":
                    oName.write(char) # write the character to the output file
                    char = fName.read(1)
                    break
                else:
                    oName.write(char) # write the character to the output file
                    char = fName.read(1)
                total_count = total_count + 1

        if count != position: # when not at the desired position, add 1 to count
            if char != "\n":
                count = count + 1
                out_count = out_count + 1

            elif char == "\n": # if the character is a newline, don't change the count
                pass

            oName.write(char) # write the character to the output file

        elif count == position:
            if char == target:
                print("The amino acid " + char + " at " + str(position) + " is deleted") # letting the user know that the aa is there
                print("didn't add " + char + " because it's at position " + str(position))
                count = count + 1 # increasing count
                mutation = mutation + 1
                deleted = True

            else:
                oName.write(char)
                count = count + 1
                out_count = out_count + 1
                if deleted == False:
                    print("There was no mutation")

        total_count = total_count + 1



    difference = total_count - mutation

    if fasta == True:
        print("In the FASTA files, the length is " + str(total_count) +" before the mutation and " + str(difference) \
                + " after the " + str(mutation) +" mutation(s)")
    else:
        print("There are " + str(count) +" amino acids before the mutation and " + str(out_count) \
                    + " amino acids after the " + str(mutation) +" mutation(s)")
    fName.close()
    oName.close()



except FileNotFoundError:
    print("File could not be opened")
    quit
