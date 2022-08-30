def compute(celsius):
    #coverting c to f
    c = int(celsius)
    fahrenheit = (c * 1.8) + 32
    #print("fahrenheit : " , fahrenheit ,"F")
    return fahrenheit
compute(input("Enter the temperature in celsius(C): "))

