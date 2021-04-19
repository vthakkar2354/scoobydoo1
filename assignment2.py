# Name: Vraj Thakkar
# Date: 04/14/2021
# Program: Scoobydoo


# Function (Open, Write, Close)
print ("function 1 output")
def scoobydoo1 ():
    # Open the file
    scoobydoo_file= open ('scoobydoo.txt', 'r')

    #Read the file contents
    scoobydoo_contents= scoobydoo_file.read()
    
    # close the file
    scoobydoo_file.close()

    #print the file
    print (scoobydoo_contents)

scoobydoo1()

#open a new function
print("function 2 output")
def scoobydoo2 ():
    #open the same file again
    scoobydoo_file= open ('scoobydoo.txt', 'r')

    #read the file content
    line1 = scoobydoo_file.readline()
    line2 = scoobydoo_file.readline()
    line3 = scoobydoo_file.readline()
    #close the scoobydoo file
    scoobydoo_file.close() 

    #print the file
    print (line1)
    print (line2)
    print (line3)

#close the other function
scoobydoo2()