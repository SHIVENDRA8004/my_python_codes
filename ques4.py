def force(m,a):
    print(f"Mass of the Body is {m}")
    print(f"Acceleration of the Body is {a}")
    force=m*a
    print(f"The Force is {force}")
    n=1
    for i in range (1,force+1):
        n=n*i
    print(f"The Factorial of No. is {n}")
m=int(input("Enter the Mass of the Body:"))
a=int(input("Enter the Acceleration of the Body:"))
force(m,a)