# Name: Vraj Thakkar
# Date: 04/14/2021
# Program: Scoobydoo


# Function (Open, Write, Close)
def scoobydoo1 ():
    # Open the file
    scoobydoo_file= open ('scoobydoo.txt', 'w')

    # Write to a file
    scoobydoo_file.write("shaggy")
    scoobydoo_file.write("         scoobydoo\n")
    scoobydoo_file.write("daphne\n")
    scoobydoo_file.write("velma\n")
    
    # close the file
    scoobydoo_file.close()
scoobydoo1()
#open a new function
def scoobydoo2 ():
    #open the same file again
    scoobydoo_file = open ('scoobydoo.txt', 'w')

    #add to this file
    scoobydoo_file.write("fred\n")
    scoobydoo_file.write("scrappy\n")
    scoobydoo1 ()
    #close the file
    scoobydoo_file.close()

#close the other function
scoobydoo2()

