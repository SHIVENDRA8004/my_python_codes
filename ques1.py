def simpleinterest(p,r,t):
    print(f"The Principle Amount is {p}")
    print(f"The Rate is {r}")
    print(f"The Time is {t}")
    si=p*r*t
    print(f"The simple interest = {si}")
p=int(input("Enter The Principle Amount:"))
r=int(input("Enter The Rate:"))
t=int(input("Enter The Time:"))
simpleinterest(p,r,t)