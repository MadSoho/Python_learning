def c2f (value):
    f = float(value)*1.8+32
    return(f)

c=input("What is temperature in Celsius? ")
print(c,"°C are equivalent to", c2f(c),"°F")
