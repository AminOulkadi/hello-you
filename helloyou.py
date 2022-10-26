from time import sleep
def printsleep(sleeptime, txt):
    sleep(sleeptime)
    print(txt)

print("Hello you!")
name = input("Wie ben je? ")
print("Hallo " + str(name) + " mijn naam is Amin" )

teller = 0

printsleep(1.0,"Wat is mijn favorieten eten")
printsleep(1.0,"a = noodles")
printsleep(1.0,"b = gehakt")
printsleep(1.0,"c = asperges")
gbr_antwoord = input("> ").lower()
if gbr_antwoord == "b":
    printsleep(1.0,"dat is goed!")
    teller+=5
elif gbr_antwoord == "a":
    printsleep(1.0,"dat is niet goed")
    teller-=2
elif gbr_antwoord == "c":
    printsleep(1.0,"dat is niet goed")
    teller-=2

printsleep(1.0,"Wat is mijn favorieten drinken")
printsleep(1.0,"a = milkshake")
printsleep(1.0,"b = water")
printsleep(1.0,"c = thee")
gbr_antwoord = input("> ").lower()
if gbr_antwoord == "c":
    printsleep(1.0,"dat is goed!")
    teller+=5
elif gbr_antwoord == "a":
    printsleep(1.0,"dat is niet goed")
    teller-=2
elif gbr_antwoord == "b":
    printsleep(1.0,"dat is niet goed")
    teller-=2

printsleep(1.0,"Wat is mijn favorieten spel")
printsleep(1.0,"a = sea of thieves")
printsleep(1.0,"b = fortnite")
printsleep(1.0,"c = minecraft")
gbr_antwoord = input("> ").lower()
if gbr_antwoord == "a":
    printsleep(1.0,"dat is goed!")
    teller+=5
elif gbr_antwoord == "c":
    printsleep(1.0,"dat is niet goed")
    teller-=2
elif gbr_antwoord == "b":
    printsleep(1.0,"dat is niet goed")
    teller-=2

printsleep(1.0,"Wat zijn mijn hobbies")
printsleep(1.0,"a = coderen en voetballen")
printsleep(1.0,"b = gamen en hockey")
printsleep(1.0,"c = voetballen en gamen")
printsleep(1.0,"d = coderen en hockey")
gbr_antwoord = input("> ").lower()
if gbr_antwoord == "c":
    printsleep(1.0,"dat is goed!")
    teller+=5
elif gbr_antwoord == "a":
    printsleep(1.0,"dat is niet goed")
    teller-=2
elif gbr_antwoord == "b":
    printsleep(1.0,"dat is niet goed")
    teller-=2
elif gbr_antwoord == "d" :
    printsleep(1.0,"dat is niet goed")
    teller-=2


printsleep(1.0,"jij hebt " +str(teller) + " punten!")

while True: 
    printsleep(1.0,"wil jij een spelletje spelen? ")
    antwoord = input("antwoord > ")
    if antwoord == "ja":
        printsleep(1.0,"laat we een verhaal spel spelen")
        break
    elif antwoord == "nee":
        printsleep(1.0,"oh ok doei! ")
        exit()
    else: printsleep(1.0,"ik verstond dat niet")

printsleep(1.0,"\n\nJe ouders vinden dat je op vakantie moet gaan op een Cruise ship je twijfelt of je wel wilt gaan.")
printsleep(1.0,"\na = ja")
printsleep(1.0,"b = nee")
antwoord = input("antwoord > ")
if antwoord == "b":
    printsleep(1.0,"\n\nJe vertelt je ouders je gaat op de cruise maar je gaat eigenlijk naar buiten met je vrienden.")
    printsleep(1.0,"Je vraagt aan je vrienden of je bij hem mag slapen.")
    printsleep(1.0,"\nYOU GOT THE LAZY ENDING.")
elif antwoord == "a": 
    printsleep(1.0,"\n\nJe gaat naar de cruise en bent een beetje nerveus, maar 3 uur later in de avond is er een all you can eat diner. ")
    printsleep(1.0,"je denkt eraan om te gaan maar je hebt niet echt honger.")
    printsleep(1.0,"\na = je gaat eten ")
    printsleep(1.0,"b = je gaat erheen maar eet niks ")
    printsleep(1.0,"c = je gaat naar bed ")
    antwoord = input("antwoord > ")
    if antwoord == "a":
        printsleep(1.0,"\n\nje ging naar het diner en at een klein beetje.")
        printsleep(1.0,"je voelt je een beetje duizelig en valt neer.")
        printsleep(1.0,"voordat je flauw valt zie octopus monsters die je meenemen")
        printsleep(1.0,"\nYOU DIED,")
        printsleep(1.0,"probeer volgende keer een andere keuze.")
    elif antwoord == "b":
        printsleep(1.0,"\n\nJe gaat erheen maar eet niks. ")
        printsleep(1.0,"Je ontmoet een getrouwd stel, ze bieden je wat eten aan maar je eet het niet.")
        printsleep(1.0,"Na ongeveer 10 minuten voelen ze zich slaperig en opeens vallen mensen neer. ")
        printsleep(1.0,"Je bent de enige daar dus je kijkt rond. ")
        printsleep(1.0,"Je hoort mensen komen.")
        printsleep(1.0,"\na = ga richting het geluid en vraag om hulp ")
        printsleep(1.0,"b = je doet alsof jij ook bent neergevallen.")
        antwoord = input("antwoord > ")
        if antwoord == "a":
            printsleep(1.0,"\n\nJe gaat richting het geluid maar het zijn geen mensen. ")
            printsleep(1.0,"Het zijn alien monsters en ze schieten je met een alien wapen. ") 
            printsleep(1.0,"\nYOU DIED,")
            printsleep(1.0,"probeer volgende keer een andere keuze.")
        elif antwoord == "b": 
            printsleep(1.0,"\n\nJe ligt op de grond naast het getrouwd stel waarmee je eerder sprak, ")
            printsleep(1.0,"de mensen die je eerder hoorde komen zijn geen mensen ze lijken op een soort octopus monster. ")
            printsleep(1.0,"Je kijkt rond en vind een mes.")
            printsleep(1.0,"Je pakt de mes en rent weg je gaat naar boven naar de besturings kamer. ")
            printsleep(1.0,"Er is daar niemand geen kapitein geen monsters.")
            printsleep(1.0,"\na = proberen te communiceren met een haven ")
            printsleep(1.0,"b = probeer wapens te vinden ")
            printsleep(1.0,"c = probeer het cruiseschip te varen in een ijsberg ")
            antwoord = input("antwoord > ")
            if antwoord == "c":
                printsleep(1.0,"\n\nJe vaart het schip richting een ijsberg.")
                printsleep(1.0,"Je hoort de monsters komen in de gang,")
                printsleep(1.0,"dus je doet de deur opslot en doet een kast ervoor.")
                printsleep(1.0,"het schip crashed in een ijsberg.")
                printsleep(1.0,"je rent naar een reddingsboot en vaart weg.")
                printsleep(1.0,"\nYOU GOT THE SELFISH ENDING.")
            elif antwoord == "a":
                printsleep(1.0,"\n\nJe probeert met een haven te communiceren en ontvangt een signaal.")
                printsleep(1.0,"Je vertlet hun alles wat je weet en vraagt of ze so snel mogelijk kunnen komen.")
                printsleep(1.0,"Je hoort de monsters lopen in de gang dus je zegt tegen de mensen dat ze er aan komen en zet de radio uit.")
                printsleep(1.0,"Je doet de deur zachtjes opslot en verstopt in een kast.")
                printsleep(1.0,"ze kijken rond maar kunnen je niet vinden.")
                printsleep(1.0,"Na 15 minuten hoor je boten en helikopters aan komen.")
                printsleep(1.0,"Je rent naar de uitgang en wordt gered.")
                printsleep(1.0,"\nYOU GOT THE SELFLESS ENDING.")
            elif antwoord == "b":
                printsleep(1.0,"\n\nJe zoekt naar iets dat je kan gebruiken tegen deze monsters en vind een AK-47. ")
                printsleep(1.0,"De monsters komen eraan dus je gaat achter de deur staan en staat klaar met je wapen.")
                printsleep(1.0,"Maar ze komen niet ze lopen langs de kamer en gaan weg.")
                printsleep(1.0,"Je wilt hier weg komen maar twijfelt een beetje.")
                printsleep(1.0,"\na = Je zoekt de kastjes voor een ander wapen")
                printsleep(1.0,"b = Blijf in de kamer en probeer uit te vogelen hoe je wegkomt")
                printsleep(1.0,"c = Je gaat de gang in en probeert weg te komen")
                antwoord = input("antwoord > ")
                if antwoord == "c":
                    printsleep(1.0,"\n\nJe gaat de gang in en probeert de weg naar de reddingbootjes te vinden.")
                    printsleep(1.0,"Je ziet de monsters voor je dus je draait om en rent weg maar ze zijn ook achter je.")
                    printsleep(1.0,"Je wordt van beide kanten neergeschoten.")
                    printsleep(1.0,"\nYOU DIED,")
                    printsleep(1.0,"probeer volgende keer een andere keuze.")
                elif antwoord == "a":
                    printsleep(1.0,"\n\nJe zoekt de kastjes en vind een trophy.")
                    printsleep(1.0,"Je neemt het mee naar huis.")
                    printsleep(1.0,"\nYOU GOT A COLLECTIBLE!")
                    printsleep(1.0,"\nKies 1 van de 2 opties van de vorige vraag om verder te gaan.")
                    printsleep(1.0,"\nb = Blijf in de kamer en probeer uit te vogelen hoe je wegkomt")
                    printsleep(1.0,"c = Je gaat de gang in en probeert weg te komen")
                    antwoord = input("antwoord > ")
                    if antwoord == "c":
                        printsleep(1.0,"\n\nJe gaat de gang in en probeert de weg naar de reddingbootjes te vinden.")
                        printsleep(1.0,"Je ziet de monsters voor je dus je draait om en rent weg maar ze zijn ook achter je.")
                        printsleep(1.0,"Je wordt van beide kanten neergeschoten.")
                        printsleep(1.0,"\nYOU DIED,")
                        printsleep(1.0,"probeer volgende keer een andere keuze.")
                    elif antwoord == "b":
                        printsleep(1.0,"\n\nJe zoekt rond in de controle en vind een blauwdruk van het schip.")
                        printsleep(1.0,"Op de blauwdruk zie welke richting je op moet gaan om bij de reddingsboten te komen.")
                        printsleep(1.0,"Je probeert zo snel mogelijk daar te komen maar je probeert ook zo stil mogelijk te zijn.")
                        printsleep(1.0,"je komt aan bij de reddingsboten maar er zijn daar 2 monsters.")
                        printsleep(1.0,"\na = Schiet ze dood met je AK-47.")
                        printsleep(1.0,"b = Ren naar de reddingsboot en probeer weg te komen.")
                        printsleep(1.0,"c = Ga naar een doos en zoek naar iets dat je kan gebruiken tegen de monsters")
                        antwoord = input("antwoord > ")
                        if antwoord == "a":
                            printsleep(1.0,"\n\nJe rent recht voor de reddingsboot en schiet de octopus monsters.")
                            printsleep(1.0,"Helaas kon je maar 1 van 2 de mosnters doden.")
                            printsleep(1.0,"De monsters schieten je doodt en gooien jouw lichaam het ship af.")
                            printsleep(1.0,"\nYOU DIED,")
                            printsleep(1.0,"probeer volgende keer een andere keuze.")
                        elif antwoord == "b":
                            printsleep(1.0,"\n\nJe rent zo snel mogelijk naar de reddingsboten.")
                            printsleep(1.0,"Je valt in het water omdat je bent gestruikeld door jouw losse veters.")
                            printsleep(1.0,"Nu lachen de octopus monsters je uit terwijl een haai aan je knabbelt.")
                            printsleep(1.0,"\nYOU DIED,")
                            printsleep(1.0,"probeer volgende keer een andere keuze.")
                        elif antwoord == "c":
                            printsleep(1.0,"\n\nJe vindt een mes net zoals een mes van cs:go.")
                            printsleep(1.0,"Je gaat hitman mode en je snijdt de eerste octopus monsters nek helemaal open en gooit zijn lichaam van boord.")
                            printsleep(1.0,"De tweede monster komt om te kijken waar de eerste monster is gebleven.")
                            printsleep(1.0,"Dat is het moment waar je jouw arm om hem heen doet en ook zijn nek open snijdt.")
                            printsleep(1.0,"Je stapt in de reddingboot en wanneer je de boot heb losgemaakt komen nog meer monster,")
                            printsleep(1.0,"Helaas voor hun zijn ze te laat en ben je weg.")
                            printsleep(1.0,"\nYOU GOT THE MAIN ENDING")
                elif antwoord == "b":
                    printsleep(1.0,"\n\nJe zoekt rond in de controle en vind een blauwdruk van het schip.")
                    printsleep(1.0,"Op de blauwdruk zie welke richting je op moet gaan om bij de reddingsboten te komen.")
                    printsleep(1.0,"Je probeert zo snel mogelijk daar te komen maar je probeert ook zo stil mogelijk te zijn.")
                    printsleep(1.0,"je komt aan bij de reddingsboten maar er zijn daar 2 monsters.")
                    printsleep(1.0,"\na = Schiet ze dood met je AK-47.")
                    printsleep(1.0,"b = Ren naar de reddingsboot en probeer weg te komen.")
                    printsleep(1.0,"c = Ga naar een doos en zoek naar iets dat je kan gebruiken tegen de monsters")
                    if antwoord == "a":
                        printsleep(1.0,"\n\nJe rent recht voor de reddingsboot en schiet de octopus monsters.")
                        printsleep(1.0,"Helaas kon je maar 1 van 2 de mosnters doden.")
                        printsleep(1.0,"De monsters schieten je doodt en gooien jouw lichaam het ship af.")
                        printsleep(1.0,"\nYOU DIED,")
                        printsleep(1.0,"probeer volgende keer een andere keuze.")
                    elif antwoord == "b":
                        printsleep(1.0,"\n\nJe rent zo snel mogelijk naar de reddingsboten.")
                        printsleep(1.0,"Je valt in het water omdat je bent gestruikeld door jouw losse veters.")
                        printsleep(1.0,"Nu lachen de octopus monsters je uit terwijl een haai aan je knabbelt.")
                        printsleep(1.0,"\nYOU DIED,")
                        printsleep(1.0,"probeer volgende keer een andere keuze.")
                    elif antwoord == "c":
                        printsleep(1.0,"\n\nJe vindt een mes net zoals een mes van cs:go.")
                        printsleep(1.0,"Je gaat hitman mode en je snijdt de eerste octopus monsters nek helemaal open en gooit zijn lichaam van boord.")
                        printsleep(1.0,"De tweede monster komt om te kijken waar de eerste monster is gebleven.")
                        printsleep(1.0,"Dat is het moment waar je jouw arm om hem heen doet en ook zijn nek open snijdt.")
                        printsleep(1.0,"Je stapt in de reddingboot en wanneer je de boot heb losgemaakt komen nog meer monster,")
                        printsleep(1.0,"Helaas voor hun zijn ze te laat en ben je weg.")
                        printsleep(1.0,"\nYOU GOT THE MAIN ENDING")
    elif antwoord == "c":
        printsleep(1.0,"\n\nJe gaat naar bed.")
        printsleep(1.0,"maar je kan niet slapen dus je gaat wat te drinken halen.")
        printsleep(1.0,"Je ziet iemand op de grond en probeert hem wakker te maken maar het werkt niet.")
        printsleep(1.0,"Na 5 minuten wordt hij wakker en hij zegt dat iedereen vergiftigd werd en dat jullie daar weg moeten.")
        printsleep(1.0,"zijn naam is Joshua ze zitten achter hem aan.")
        printsleep(1.0,"\na = jullie gaan naar de escape boten")
        printsleep(1.0,"b = jullie gaan naar de controleroom")
        antwoord = input("antwoord > ")
        if antwoord == "b":
            printsleep(1.0,"\n\nJullie gaan naar de controleroom mmaar vinden de octopus monsters daar.")
            printsleep(1.0,"Je rent zo snel mogelijk weg maar ze zijn ook voor en achter je.")
            printsleep(1.0,"Ze schieten jij en joshua dood.")
            printsleep(1.0,"\nYOU DIED,")
            printsleep(1.0,"probeer volgende keer een andere keuze.")
        elif antwoord == "a":
            printsleep(1.0,"\n\nJullie gaan voor de boten maar de octopus monsters zitten achter jullie aan.")
            printsleep(1.0,"Jullie vinden een wapen en schieten op hen maar het lijkt niks te doen.")
            printsleep(1.0,"Joshua zegt dat hij daar weg moet hij heeft belangrijke informatie voor de regering.")
            printsleep(1.0,"\na = je schiet hem in de benen en rent weg")        
            printsleep(1.0,"b = je gaat richting de monsters zodat Joshua weg kan komen met de informatie")    
            antwoord = input("antwoord > ")
            if antwoord == "a":
                printsleep(1.0,"\n\nJe schiet Joshua in de been en rent voor de reddingsboot.")
                printsleep(1.0,"Je ziet dat de monsters niks willen met jou en gaan voor Joshua.")
                printsleep(1.0,"Terwijl je probeert weg te komen hoor je geschreeuw van Joshua.")
                printsleep(1.0,"Je bent weggekomen maar je hebt ook iemand laten doodgaan.")
                printsleep(1.0,"\nYOU GOT THE BAD ENDING.")
            elif antwoord == "b":
                printsleep(1.0,"\n\nJe rent richting de monsters maar wordt overmeesterd door hun kracht.")
                printsleep(1.0,"je wordt door 2 monsters vastgepakt terwijl de andere achter Joshua gaan,")
                printsleep(1.0,"je ontsnapt de 2 en stopt de monsters voor jou.")
                printsleep(1.0,"Joshua is veilig weggekomen maar helaas zit jij vast en je wordt vermoord.")
                printsleep(1.0,"\nYOU GOT THE NOBLE ENDING.")