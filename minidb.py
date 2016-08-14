"""

f = open("txt", "a")
f.write("Yo yo yo\n") 
f.close()

f = open("txt")
for line in f:
    print line
f.close()

"""