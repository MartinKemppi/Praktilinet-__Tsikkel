from math import*
from random import *
import string 

#harjutus 15

try:
    x=0
    print("Osta elevant ära!")
    vastus=input("")
    while True:
        if vastus == "elevant":
            x+=1
            break
        else:
            print("Osta elevant ära!")
            vastus=input("")
            x+=1
    print("Küsimus oli esitatud", x ,"korda")
except:
    print("Vale andmetüüp")

try:
    x=0
    print("Osta elevant ära!")
    vastus=input("")
    while vastus=="elevant":
        if vastus == "elevant":
            x+=1
            break
        else:
            print("Osta elevant ära!")
            vastus=input("")
            x+=1
    print("Küsimus oli esitatud", x ,"korda")
except:
    print("Vale andmetüüp")

#harjutus 0

a=randint(1,10)
b=0
try:
    while True:
        b = int(input("Arva ära arv vahemikus 1 kuni 10: "))
        if b>10 or b<1:
            print("Vahemiku viga")
        if b < a:
            print("Suurem!")
            x+=1
        elif b > a:
            print("Vähem!")
            x+=1
        else:
            print("Oled võitnud! Arvasid arv pärast", x ,"korda")
            break
except:
    print("Vale andmetüüp")

a=randint(1,10)
b=0
x=0
try:
    while x<=4:
        b = int(input("Arva ära arv vahemikus 1 kuni 10, sul on 3 katset: "))
        x+=1
        if b>10 or b<1:
            print("Vahemiku viga")          
        if b < a:
            print("Suurem!")
        elif b > a:
            print("Vähem!")
        else:
            print("Oled Võitnud!")
            break
        if x==3:
            print("Oled kaotanud!")
            break

except:
    print("Vale andmetüüp")


#harjutus 10
#x=1
#while x<=100:
#    if x%5==0:
#        print(x, end=" ")
#    x+=1

#harjutus o_0
#a=random.randint(1,100)
#b=0
#while b!=a:
#    try:
#        b = int(input("Sisesta number vahemikus 1-100: "))
#        if b>100 or b<1:
#            print("vahemiku viga")
#        if b < a:
#            print("Liiga väike! Proovi uuesti")
#        elif b > a:
#            print("Liiga suur! Proovi uuesti")
#        else:
#            print("Palju õnne! Sa arvasid mõistatuslik numbri ära.", a)
#            break
#    except:
#        print("Vale andmetüüp")

#harjutus 17
#try:
#    num_horiz=int(input("Sisesta ruutude arv horisontaalselt =>> \n"))
#except:
#    print("Value Error")
#    num_horiz=randint(1, 10000)
#try:
#    num_vert=int(input("Sisesta ruutude arv horisontaalselt =>> \n"))
#except:
#    print("Value Error")
#    num_vert=randint(1, 10000)

#for y in range(num_vert):
#    for x in range(num_horiz):
#        print("□", end=" ")
#    print()
   
#    harjutus 16    
#ans = randint(1, 10)
#while True:
#    g = input("mis numbri ma arvasin? (1-10, mängu lõpetamiseks kirjutage *lõpp*) \n")
#    if g.lower() == "lõpp":
#        print("mäng on läbi!")
#        break
#    if not g.isnumberic():
#        print("Vale andmetüüp")
#        continue
#    g = int(g)
#    if g == ans:
#        print("õige! sa arvasid ära!")
#        break
#    if g>10 or g<1:
#        print("Vahemik on vale!")
#        continue
#    elif g !=ans:
#        print(f"vale! proovi veel korra!")

#harjutus 3

#g=1
#try:
#    f=int(input("mitu ülesandeid sa tahad? "))
#    for d in range (0,f,1):
#        print(f"ülesanne {g}: ")
#        a = randint(1,50)
#        b = randint(1,50)
#        c = a+b
#        for i in range (0,5,1):
#            answer = int(input(f"{a}+{b}=? "))
#            if answer == a+b:
#                print(" see on õige")
#                break
#            else:
#                print("Proovi veel korra")
#                print()
#        g = g+1
#        print(f"õige on {c}")
#except:
#    print("see ei ole õige")

##harjutus 13
#print("arv", "    ruut ", "    kuup")
#for i in range (1, 11):
#    print(f" {i}     {i**2}         {i**3}")
##harjutus 13-2
#print("arv", "     ruut", "       kuup")
#i = 1
#while i < 11:
#    print(f" {i}    {i**2}     {i**3}")
#    i += 1

#print("Arva täht - ( Aa - Zz)")
#letter = random.choice(string.ascii_letters)

#while True:
#    answ = str(input("Teie oletus: "))
#    if letter == answ:
#        print("Tubli!")
#        break
#    else: print("Proovi uuesti!")

#harjutus 22
#a=1
#while True:
#    print("Tahan kommi!")
#    a = str(input())
#    if a.lower()== "komm":
#        print("Äitäh! Oli vaja" + str(n) + " katse.")
#        break
#    else:
#        n = n+1

#harjutus6
#print()
#for i in range(0,5):
#    print("* "*5)
#print()
#for i in range(0,10):
#    print("* "*1)
#print()
#for i in range (0,10):
#    print("* "(10-1))
#print()

#harjutus 8

#while True:
#    try:
#        mainnumber = int(input("Vali number 1-100: "))
#        break
#    except ValueError:
#        print("See pole täisarv")
#if mainnumber<1 or mainnumber >100:
#    print("Vali õige number")
#else:
#    paaris = 0
#    paaritu = 0
#    x = 0
#    while x != mainnumber:
#        x = x+1
#        print(int(x), end=" ")
#        if x%2==0:
#            paaris +=1
#        else:
#            paaritu +=1
#print("Paaris numbrid:", paaris)
#print("Paaritu numbrid:", paaritu)

#harjutus 11
#n=randint(1,10)
#a=0
#while True:
#    text = input("Väljumiseks sisestage number: ")
#    a+=1
#    if text == "stopp":
#        print("Välju programmist! Kohtumiseni! See sai tehtud", n)
#        break
#    elif int(text) == n:
#        print("palju õnne, sa võitsid")
#        break
#    else:
#        print("Proovi veel korra")
#    if a==3:
#        print("3 katset ammendatud")
#        break