def fehrecels(f):
    print(f"The temperature in Fehrenheit is : {f}")
    c=(f-32)*(5/9)
    print(f"The temperature in Celsius is : {c}")
f=int(input("Enter The Temperature in Fehrenheit: "))
fehrecels(f)