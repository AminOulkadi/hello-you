'''
print("Hello you!")
name = input("Wie ben je? ")
print("Hallo " + str(name) + " mijn naam is Amin" )

teller = 0

print("Wat is mijn favorieten eten")
print("a = noodles")
print("b = gehakt")
print("c = asperges")
gbr_antwoord = input("> ").lower()
if gbr_antwoord == "b":
    print("dat is goed!")
    teller+=5
elif gbr_antwoord == "a":
    print("dat is niet goed")
    teller-=2
elif gbr_antwoord == "c":
    print("dat is niet goed")
    teller-=2

print("Wat is mijn favorieten drinken")
print("a = milkshake")
print("b = water")
print("c = thee")
gbr_antwoord = input("> ").lower()
if gbr_antwoord == "c":
    print("dat is goed!")
    teller+=5
elif gbr_antwoord == "a":
    print("dat is niet goed")
    teller-=2
elif gbr_antwoord == "b":
    print("dat is niet goed")
    teller-=2

print("Wat is mijn favorieten spel")
print("a = sea of thieves")
print("b = fortnite")
print("c = minecraft")
gbr_antwoord = input("> ").lower()
if gbr_antwoord == "a":
    print("dat is goed!")
    teller+=5
elif gbr_antwoord == "c":
    print("dat is niet goed")
    teller-=2
elif gbr_antwoord == "b":
    print("dat is niet goed")
    teller-=2

print("Wat zijn mijn hobbies")
print("a = coderen en voetballen")
print("b = gamen en hockey")
print("c = voetballen en gamen")
print("d = coderen en hockey")
gbr_antwoord = input("> ").lower()
if gbr_antwoord == "c":
    print("dat is goed!")
    teller+=5
elif gbr_antwoord == "a":
    print("dat is niet goed")
    teller-=2
elif gbr_antwoord == "b":
    print("dat is niet goed")
    teller-=2
elif gbr_antwoord == "d" :
    print("dat is niet goed")
    teller-=2
'''

# print("jij hebt " +str(teller) + " punten!")

while True: 
    print("wil jij een spelletje spelen? ")
    antwoord = input("antwoord > ")
    if antwoord == "ja":
        print("laat we een verhaal spel spelen")
        break
    elif antwoord == "nee":
        print("oh ok doei! ")
        exit()
    else: print("ik verstond dat niet")

print("\nJe ouders vinden dat je op vakantie moet gaan op een Cruise ship je twijfelt of je wel wilt gaan.")
print("a = ja")
print("b = nee")
antwoord = input("antwoord > ")
if antwoord == "ja": 
    print("\nJe gaat naar de cruise en bent een beetje nerveus, maar 3 uur later in de avond is er een all you can eat diner. ")
    print("je denkt eraan om te gaan maar je hebt niet echt honger.")
    print("a = je gaat eten ")
    print("b = je gaat erheen maar eet niks ")
    print("c = je gaat naar bed ")
    antwoord = input("antwoord > ")
    if antwoord == "a":
        print("\nje ging naar het diner en at een klein beetje.")
        print("je voelt je een beetje duizelig en valt neer.")
        print("voordat je flauw valt zie octopus monsters die je meenemen")
        print("YOU DIED,")
        print("probeer volgende keer een andere keuze.")
    elif antwoord == "b":
        print("\nJe gaat erheen maar eet niks. ")
        print("Je ontmoet een getrouwd stel, ze bieden je wat eten aan maar je eet het niet.")
        print("Na ongeveer 10 minuten voelen ze zich slaperig en opeens vallen mensen neer. ")
        print("Je bent de enige daar dus je kijkt rond. ")
        print("Je hoort mensen komen.")
        print("a = ga richting het geluid en vraag om hulp ")
        print("b = je doet alsof jij ook bent neergevallen.")
        if antwoord == "a":
            print("Je gaat richting het geluid maar het zijn geen mensen. ")
            print("Het zijn alien monsters en ze schieten je met een alien wapen. ") 