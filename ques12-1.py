def square(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i == 1 or i == n or j == 1 or j == n):
                if((i == 1 and j == 1) or (i == 1 and j == n) or (i == n and j == 1) or (i == n and j == n)):
                    print("+", end=" ")
                else:
                    if(j == 1 or j == n):
                        print("|", end=" ")
                    else:
                        print("-", end=" ")
            else:
                print(" ", end=" ")
        print()


n = int(input("Enter The Number:"))
square(n)
