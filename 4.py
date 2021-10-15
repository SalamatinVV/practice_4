day=int(input("Day:"))
pop= int(input("Population:"))
i=int(0)
pr=int(input("%:"))/100
print ("День     Популяция")
while i<day:
    print(i, "    ",round(pop,5))
    i+=1
    pop=pop*(1+pr)


