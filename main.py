def compute(celsius):
    #coverting c to f
    fahrenheit = (celsius * 1.8) + 32
    print("fahrenheit : " , fahrenheit ,"F")
    return fahrenheit
c=input("Enter the temperature in celsius(C): ")
a=int(c)
compute(a)