#Loops
# Break and continue

i = 1
while i <= 5:
    print(i)
    if(i==6):
        break
    i += 1

    #Continue

    e = 1
while e <= 10:

    if(e%2 != 0):
        e += 1
        continue
    print(e)
    e += 1