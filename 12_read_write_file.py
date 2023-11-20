
file = open("countries.txt", "a+")
print('Readable: ',file.readable())
print('Writable: ',file.writable())


def readContents():
    fileContent = file.readlines()

    for line in fileContent:
        print(line)

def writeContent(content):
    char_written = file.write(content)
    print("Line Number: ", char_written)


writeContent("\n- Japan")
print("-----x-----")
readContents()


file.close()