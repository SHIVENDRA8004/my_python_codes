def printnumber(choice):
    if(choice == 1):
        for i in range(1, 11):
            print(i)
    elif(choice == 2):
        for j in range(10, 0, -1):
            print(j)


print("Enter 1: For Ascending Order")
print("Enter 2: For Descending Order")
choice = int(input())
printnumber(choice)
