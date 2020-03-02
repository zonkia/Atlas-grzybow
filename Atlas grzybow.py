import os

print("Witaj w atlasie grzybów. Wybierz co chcesz zrobić:")
print()
print("Wpisz SPIS, aby zobaczyc spis nazw grzybów w atlasie")
print("Wpisz FILTR, aby wyświetlnić tylko interesujące Ciebie grzyby")
print("Wpisz POKAZ, aby zobaczyc wszystkie wpisy")
print("Wpisz SZUKAJ, aby wyszukac interesującego Ciebie grzyba")
print("Wpisz DODAJ, aby dodać nowego grzyba i opis")
print("Wpisz EDYTUJ, aby edytować obecny wpis")
print("Wpisz USUN, aby usunąć grzyba z atlasu")
print("Wpisz WYJDZ, aby wyjsc z atlasu")

loop = 1
loopSearch = 1
loopDelete = 1

indeksy = {}
atlas = {
            "Prawdziwek": {"Wysokość [cm]": 20, "Śr. Kapelusza [cm]": 25, "Szer. trzonu [cm]": 5, "Kolor": "Jasnobrązowy / ciemnobrązowy", "Jadalny": "Tak"},
            "Muchomor": {"Wysokość [cm]": 20, "Śr. Kapelusza [cm]": 20, "Szer. trzonu [cm]": 5, "Kolor": "Czerwony kapelusz z białymi kropkami", "Jadalny": "Nie"},
            "Kurka": {"Wysokość [cm]": 5, "Śr. Kapelusza [cm]": 8, "Szer. trzonu [cm]": 2.5, "Kolor": "Żółty / pomarańczowożółty", "Jadalny": "Tak"},
            "Purchawka": {"Wysokość [cm]": 7, "Śr. Kapelusza [cm]": 4, "Szer. trzonu [cm]": 4, "Kolor": "Biały / Brązowy", "Jadalny": "Nie"}
}

for nazwy in atlas:
    for cechy in atlas[nazwy]:
        if cechy == "Wysokość [cm]":
            x = atlas[nazwy]["Wysokość [cm]"] * atlas[nazwy]["Śr. Kapelusza [cm]"] * atlas[nazwy]["Szer. trzonu [cm]"]
            indeksy[nazwy] = x

while True:
    print()
    wybor = str(input("Twoja komenda: ").upper())

    if (wybor == "POKAZ"):
        for grzyby in atlas:
            print()
            print(grzyby)
            for cechy in atlas[grzyby]:
                print(cechy,":",atlas[grzyby][cechy])
        continue
                
    elif (wybor == "SZUKAJ"):
        while loopSearch == 1:
            szukany = str(input("Szukaj grzyba: ").capitalize())
            try:
                print()
                print(szukany)
                for cechyGrzyba in atlas[szukany]:
                    print(cechyGrzyba,":",atlas[szukany][cechyGrzyba])
                print()
                ponowneSzukanie = str(input("Czy chcesz spróbować ponownie wyszukać inną nazwę? TAK/NIE ").upper())
                if ponowneSzukanie == "TAK":
                    continue
                else:
                    break
            except:
                ponowneSzukanie = str(input("Nie ma takiego grzyba. Czy chcesz spróbować ponownie wyszukać inną nazwę? TAK/NIE ").upper())
                if ponowneSzukanie == "TAK":
                    continue

    elif (wybor == "DODAJ"):
        nazwaGrzyba = str(input("Podaj nazwę grzyba: ").capitalize())
        rozmiarGrzyba = str(input("Podaj wymiary kapelusza i trzonka: "))
        kolorGrzyba = str(input("Podaj jaki kolor i cechy ma kapelusz: "))
        jadalnoscGrzyba = str(input("Czy grzyb jest jadalny? TAK/NIE ").capitalize())
        while True:
            if jadalnoscGrzyba == "Tak" or jadalnoscGrzyba == "Nie":
                break
            else:
                print("Błąd. Jadalność grzyba może być tylko TAK lub NIE. Spróbuj ponownie")
                jadalnoscGrzyba = str(input("Czy grzyb jest jadalny? TAK/NIE ").capitalize())
                continue
        atlas[nazwaGrzyba] = {"Rozmiar":rozmiarGrzyba, "Kolor":kolorGrzyba, "Jadalny":jadalnoscGrzyba}
        wpis = str(input("Dodano grzyba do atlasu. Czy chcesz zobaczyć wpis? TAK/NIE ").upper())
        if (wpis == "TAK"):
            print()
            print(nazwaGrzyba)
            for grzyby in atlas:
                for cechy in atlas[grzyby]:
                    if grzyby == nazwaGrzyba:
                        print(cechy,":",atlas[grzyby][cechy])
        else:
            continue

    elif (wybor == "USUN"):
        while loopDelete == 1:
            doUsuniecia = str(input("Podaj nazwę grzyba do usunięcia z atlasu: ").capitalize())
            try:
                del(atlas[doUsuniecia])
                print()
                wpis = str(input("Usunięto grzyba z atlasu. Czy chcesz zobaczyć aktualny atlas? TAK/NIE ").upper())
                if (wpis == "TAK"):
                    for grzyby in atlas:
                        print()
                        print(grzyby)
                        for cechy in atlas[grzyby]:
                            print(cechy,":",atlas[grzyby][cechy])
                print()
                usunPonownie = str(input("Czy chcesz usunąć kolejnego grzyba? TAK/NIE ").upper())
                if usunPonownie == "TAK":
                    continue
                else:
                    break
            except:
                print()
                usunPonownie = str(input("Nie ma takiego grzyba w atlasie. Czy chcesz spróbować ponownie? TAK/NIE ").upper())
                if usunPonownie == "TAK":
                    continue
                else:
                    break

    elif (wybor == "SPIS"):
        rosnacaLista = str(input("Czy lista ma być wyświetlona od A->Z? TAK/NIE ").upper())
        print()
        if rosnacaLista == "TAK":
            print("Lista grzybów od A->Z:")
            for nazwy in sorted(atlas.keys()):
                print(nazwy)
        else:
            print("Lista grzybów od Z->A:")
            for nazwy in sorted(atlas.keys(), reverse = True):
                print(nazwy)

    elif (wybor == "FILTR"):
        while True:
            filtr = str(input("Wpisz jakie chcesz wyfiltrować grzyby: JADALNE, NIEJADALNE, MALE, SREDNIE, DUZE: ").upper())
            if (filtr == "JADALNE"):
                kolejnoscFiltr = str(input("Czy lista jadalnych grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista jadalnych grzybów od A->Z:")
                    for nazwy in sorted(atlas.keys()):
                        for cechy in atlas[nazwy]:
                            if (atlas[nazwy][cechy] == "Tak"):
                                print(nazwy,", Jadalny: ",atlas[nazwy][cechy])
                    break          
                else:
                    print()
                    print("Lista jadalnych grzybów od Z->A:")
                    for nazwy in sorted(atlas.keys(), reverse = True):
                        for cechy in atlas[nazwy]:
                            if (atlas[nazwy][cechy] == "Tak"):
                                print(nazwy,", Jadalny: ",atlas[nazwy][cechy])
                    break

            elif (filtr == "NIEJADALNE"):
                kolejnoscFiltr = str(input("Czy lista jadalnych grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista niejadalnych grzybów od A->Z:")
                    for nazwy in sorted(atlas.keys()):
                        for cechy in atlas[nazwy]:
                            if (atlas[nazwy][cechy] == "Nie"):
                                print(nazwy,", Jadalny: ",atlas[nazwy][cechy])
                    break
                else:
                    print()
                    print("Lista niejadalnych grzybów od Z->A:")
                    for nazwy in sorted(atlas.keys(), reverse = True):
                        for cechy in atlas[nazwy]:
                            if (atlas[nazwy][cechy] == "Nie"):
                                print(nazwy,", Jadalny: ",atlas[nazwy][cechy])
                    break

            elif (filtr == "MALE"):
                kolejnoscFiltr = str(input("Czy lista małych grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista małych grzybów od A->Z:")
                    for grzyby in sorted(indeksy.keys()):
                        if (indeksy[grzyby] < 500):
                            print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break
                    print()
                else:
                    print()
                    print("Lista małych grzybów od Z->A:")
                    for grzyby in sorted(indeksy.keys(), reverse = True):
                        if (indeksy[grzyby] < 500):
                            print(grzyby, "- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break
                    print()
            
            elif (filtr == "SREDNIE"):
                kolejnoscFiltr = str(input("Czy lista średnich grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista średnich grzybów od A->Z:")
                    for grzyby in sorted(indeksy.keys()):
                        if (indeksy[grzyby] > 500) and (indeksy[grzyby] < 1000):
                            print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break
                    print()
                else:
                    print()
                    print("Lista średnich grzybów od Z->A:")
                    for grzyby in sorted(indeksy.keys(), reverse = True):
                        if (indeksy[grzyby] < 500):
                            print(grzyby, "- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break
                    print()

            elif (filtr == "DUZE"):
                kolejnoscFiltr = str(input("Czy lista dużych grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista dużych grzybów od A->Z:")
                    for grzyby in sorted(indeksy.keys()):
                        if (indeksy[grzyby] > 1000):
                            print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break
                    print()
                else:
                    print()
                    print("Lista dużych grzybów od Z->A:")
                    for grzyby in sorted(indeksy.keys(), reverse = True):
                        if (indeksy[grzyby] < 500):
                            print(grzyby, "- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break
                    print()

            else:
                print("Błąd w komendzie. Spróbój ponownie.")
                continue

    elif (wybor == "EDYTUJ"):
        while True:
            edytowanaNazwa = str(input("Podaj nazwę grzyba, którego chcesz edytować: ").capitalize())
            if edytowanaNazwa in atlas:
                print()
                atlas[edytowanaNazwa]["Rozmiar"] = str(input("Podaj wymiary trzonka i kapelusza: "))
                atlas[edytowanaNazwa]["Kolor"] = str(input("Podaj kolor kapelusza: "))
                jadalnoscEdytowana = str(input("Czy grzyb jest jadalny? TAK/NIE: ").capitalize())
                while True:
                    if (jadalnoscEdytowana == "Tak") or (jadalnoscEdytowana == "Nie"):
                        atlas[edytowanaNazwa]["Jadalny"] = jadalnoscEdytowana
                        break
                    else:
                        print("Błąd. Jadalność grzyba może być tylko TAK lub NIE. Spróbuj ponownie")
                        jadalnoscEdytowana = str(input("Czy grzyb jest jadalny? TAK/NIE: ").capitalize())
                        continue
                print()
                wpis = str(input("Edycja zapisana w atlasie. Czy chcesz zobaczyć aktualny wpis dotyczący wpisu: " + edytowanaNazwa + " TAK/NIE ").upper())
                if (wpis == "TAK"):
                    print()
                    print(edytowanaNazwa)
                    for grzyby in atlas:
                        for cechy in atlas[grzyby]:
                            if grzyby == edytowanaNazwa:
                                print(cechy,":",atlas[grzyby][cechy])
                break
            else:
                print("Nie ma takiego grzyba w atlasie")
                    
    elif (wybor == "WYJDZ"):
        os._exit(0)

    else:
        print("Nie wpisałeś prawidłowej komendy. Możliwe komendy: SPIS / FILTR / POKAZ / SZUKAJ / DODAJ / EDYTUJ / USUN / WYJDZ ")
        continue