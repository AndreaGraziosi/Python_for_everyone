# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt


fname = input("Enter file name: ") # get the input
fh = open(fname) #open a file
readfh = fh.read()#read a file
fline = readfh.rstrip().split() #remove blank space to the right and split the paragraph into words
lst = list() #call a list
for item in fline: #here if the word is not on the list we add it to the list
    if item in lst:
        continue
    else:
        lst.append(item)
lst.sort() #sort in alphabetical oder
print(lst)
