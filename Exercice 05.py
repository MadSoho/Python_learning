temperatures=[10,-20,-289,100]

def c2f (value):
    f = float(value)*1.8+32
    return(f)

with open("converted.txt",'w') as file:
    for c in temperatures:
        if c > -273.15:
           file.write(str(c2f(c))+"\n")
