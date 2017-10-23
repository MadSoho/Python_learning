temperatures=[10,-20,-289,100]

def c2f (value):
    f = float(value)*1.8+32
    return(f)

for c in temperatures:
    if c > -273.15:
        print(c,"°C are equivalent to", c2f(c),"°F")
    else:
        print("There is no such temperature in this universe!")
