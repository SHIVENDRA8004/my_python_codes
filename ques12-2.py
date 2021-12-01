def square(n):
    for i in range(1, (2*n)):
        for j in range(1, (2*n)):
            if (i == 1 or i == n or j == 1 or j == n or j == (2*n)-1) or i == (2*n)-1:
                if((i == 1 and j == 1) or (i == 1 and j == n) or (i == n and j == 1) or (i == n and j == n) or (i == 1 and j == (2*n)-1) or (i == (2*n)-1 and j == (2*n)-1) or (i == (2*n)-1 and j == 1) or (i == n and j == (2*n)-1) or (i == (2*n)-1 and j == n)):
                    print("+", end=" ")
                else:
                    if(j == 1 or j == n or j == (2*n)-1):
                        print("|", end=" ")
                    else:
                        print("-", end=" ")
            else:
                print(" ", end=" ")
        print()


n = int(input("Enter the Number:"))
square(n)
