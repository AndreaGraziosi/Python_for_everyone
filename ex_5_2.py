largest = None
smallest = None
user_list = []
while True:
    snum = input("Enter a number: ")
    if snum == "done" : break
    try:
        fnum = float(snum)
        user_list.append(fnum)
        #print(user_list)
    except:
        print('Invalid input')

# for fnum in user_list:
    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum


    elif largest is None:
        largest = fnum
    elif fnum > largest:
        largest = fnum


print("Maximum", int(largest))
print("Minimum", int(smallest))
