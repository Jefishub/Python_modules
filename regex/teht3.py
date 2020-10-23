import re
txt = "The rain in Spain 45599"
# Match all the non numbers
x = re.findall("[^0-9]", txt)
print(x)



txt2 = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
y = re.findall("falls|stays", txt2)
print(y)
if y:
    print("Yes, there is at least one match!")
else:
    print("No match")




txt3 = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 0 or more "x" characters:
z = re.findall("aix*", txt3)
print(z)
if z:
    print("Yes, there is at least one match!")
else:
    print("No match")