def square(n):
    for i in range(1, (4*n)-2):
        for j in range(1, (4*n)-2):
            if (i == 1 or i == n or j == 1 or j == n or j == (2*n)-1) or i == (2*n)-1 or i == (3*n)-2 or i == (4*n)-3 or j == (3*n)-2 or j == (4*n)-3:
                if((i == 1 and j == 1) or (i == 1 and j == n) or (i == n and j == 1) or (i == n and j == n) or (i == 1 and j == (2*n)-1) or (i == (2*n)-1 and j == (2*n)-1) or (i == (2*n)-1 and j == 1) or (i == n and j == (2*n)-1) or (i == (2*n)-1 and j == n) or (i == 1 and j == (3*n)-2) or (i == (3*n)-2 and j == 1) or (i == n and j == (3*n)-2) or (i == (3*n)-2 and j == n) or (i == (2*n)-1 and j == (3*n)-2) or (i == (3*n)-2 and j == (2*n)-1) or (i == (3*n)-2 and j == (3*n)-2) or (i == 1 and j == (4*n)-3) or (i == n and j == (4*n)-3) or (i == (2*n)-1 and j == (4*n)-3) or (i == (3*n)-2 and j == (4*n)-3) or (i == (4*n)-3 and j == (4*n)-3) or (i == (4*n)-3 and j == 1) or (i == (4*n)-3 and j == n) or (i == (4*n)-3 and j == (2*n)-1) or (i == (4*n)-3 and j == (3*n)-2)):
                    print("+", end=" ")
                else:
                    if(j == 1 or j == n or j == (2*n)-1 or j == (3*n)-2 or j == (4*n)-3):
                        print("|", end=" ")
                    else:
                        print("-", end=" ")
            else:
                print(" ", end=" ")
        print()


n = int(input("Enter a Number: "))
square(n)
