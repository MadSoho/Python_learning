import glob
import datetime

##### #variables #####
folder = ".\Exo 06\\"

#Format of the date and time\
fmt = "%Y-%m-%d-%H-%M-%S-%f"

#List the txt files in the "Exo 06" folder
liste = glob.glob(folder + "file*.txt")

#optain and format date and time to name the concatened file
#now = datetime.datetime.strftime(datetime.datetime.now(), fmt)   ### this was my first idea of this code
now = datetime.datetime.now().strftime(fmt)

##### Main code #####
#Main loop which concatenate all the txt files in one named with the datetime
with open(folder + now +".txt" , 'w') as outfile:
    for fname in liste:
        with open(fname) as infile:
            outfile.write(infile.read() + '\n')
