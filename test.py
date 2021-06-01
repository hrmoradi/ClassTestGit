def ourFirstFunction (arg):

    arguments = ""
    for i in range(len(arg)):
        arguments = arguments + " "+str(i)+": "+arg[i]

    print("Inputs to program as arguments: " + arguments)
    print("Printed results will be sent to stdout and displayed on your screen")

    content = ""
    with open(arg[1],'r') as f:
        content = f.read()
    print("Number of words in the file will be returned ("+str(len(content.split()))+")")
    return(len(content.split()))

import sys
if __name__== "__main__":
    ourFirstFunction(sys.argv)
