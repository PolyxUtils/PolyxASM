from os import sys

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Please enter a file directory")
        exit(1)

    srcFile = open(sys.argv[1], 'r')

    srcFile.close()

    exit(0)