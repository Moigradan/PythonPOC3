# for i in range(1,13):
#    print ("Numarul {} patrat e {} si cub e {:4}".format(i,i**2,i**3));

name = input(" Numele: ")
age = int(input(" Ce varsta ai, {0}?".format(name)))
print(age)

#if age >= 18:
#    print("E ok, poti vota")
#    print(" Pune un x in cutie")
# else:
#    print("Nu ai ce cota aici.Hai inapoi peste {0} ani".format(18 - age))

if age < 18:
    print("Nu ai ce cota aici.Hai inapoi peste {0} ani".format(18 - age))
elif age == 900:
    print("Wasted")
else:
    print("poti vota")
    print("Da-i sa mearga cu voturileeee")
