#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    print(out)
    return out

print(toString("sample2.txt"))

print(toString("sample2.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    f1=toString(fileName)
    maxline = ""
    for line in f1:
        print(line)
        if len(line) > len(maxline):
            maxline = line
    print(maxline)
    return maxline


print(longestLine("sample2.txt")=="Here is the text")

def toBinary(fileName):
    #f = open(fileName)
    STR=toString(fileName)
    out1 = []

    for i in range(0, len(STR), 8):
        out1.append(STR[i:i+8])

    return out1
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    pass
print(toBinary("sample3.txt"))
