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

atlas = {
            "Prawdziwek": {"Wysokość [cm]": 20, "Śr. Kapelusza [cm]": 25, "Szer. trzonu [cm]": 5, "Kolor": "Jasnobrązowy / ciemnobrązowy", "Jadalny": "Tak"},
            "Muchomor": {"Wysokość [cm]": 20, "Śr. Kapelusza [cm]": 20, "Szer. trzonu [cm]": 5, "Kolor": "Czerwony kapelusz z białymi kropkami", "Jadalny": "Nie"},
            "Kurka": {"Wysokość [cm]": 5, "Śr. Kapelusza [cm]": 8, "Szer. trzonu [cm]": 2.5, "Kolor": "Żółty / pomarańczowożółty", "Jadalny": "Tak"},
            "Purchawka": {"Wysokość [cm]": 7, "Śr. Kapelusza [cm]": 4, "Szer. trzonu [cm]": 4, "Kolor": "Biały / Brązowy", "Jadalny": "Nie"},
            "Maślak": {"Wysokość [cm]": 10, "Śr. Kapelusza [cm]": 10, "Szer. trzonu [cm]": 2, "Kolor": "Brązowy", "Jadalny": "Tak"},
}

maleGrzyby = [
                nazwy
                for nazwy in atlas
                if atlas[nazwy]["Wysokość [cm]"] * atlas[nazwy]["Śr. Kapelusza [cm]"] * atlas[nazwy]["Szer. trzonu [cm]"] < 150
]

srednieGrzyby = [
                nazwy
                for nazwy in atlas
                if atlas[nazwy]["Wysokość [cm]"] * atlas[nazwy]["Śr. Kapelusza [cm]"] * atlas[nazwy]["Szer. trzonu [cm]"] > 150 and atlas[nazwy]["Wysokość [cm]"] * atlas[nazwy]["Śr. Kapelusza [cm]"] * atlas[nazwy]["Szer. trzonu [cm]"] < 1000
]

duzeGrzyby = [
                nazwy
                for nazwy in atlas
                if atlas[nazwy]["Wysokość [cm]"] * atlas[nazwy]["Śr. Kapelusza [cm]"] * atlas[nazwy]["Szer. trzonu [cm]"] > 1000
]

jadalne = [
            nazwy
            for nazwy in atlas
            if atlas[nazwy]["Jadalny"] == "Tak"
]

niejadalne = [
            nazwy
            for nazwy in atlas
            if atlas[nazwy]["Jadalny"] == "Nie"
]

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
            filtr = str(input("Jeśli chcesz zastosować podwójny filtr wpisz DWA. Jeśli chcesz zastosować filtr pojedynczy wpisz jakie grzyby chcesz wyfiltrować: JADALNE, NIEJADALNE, MALE, SREDNIE, DUZE: ").upper())
            if (filtr == "JADALNE"):
                kolejnoscFiltr = str(input("Czy lista jadalnych grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista jadalnych grzybów od A->Z:")
                    for nazwy in sorted(jadalne):
                        print(nazwy, ", Jadalny: ", atlas[nazwy]["Jadalny"])
                    break
                else:
                    print()
                    print("Lista jadalnych grzybów od Z->A:")
                    for nazwy in sorted(jadalne, reverse = True):
                        print(nazwy, ", Jadalny: ", atlas[nazwy]["Jadalny"])
                    break

            elif (filtr == "NIEJADALNE"):
                kolejnoscFiltr = str(input("Czy lista niejadalnych grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista niejadalnych grzybów od A->Z:")
                    for nazwy in sorted(niejadalne):
                        print(nazwy, ", Jadalny: ", atlas[nazwy]["Jadalny"])
                    break
                else:
                    print()
                    print("Lista jadalnych grzybów od Z->A:")
                    for nazwy in sorted(niejadalne, reverse = True):
                        print(nazwy, ", Jadalny: ", atlas[nazwy]["Jadalny"])
                    break

            elif (filtr == "MALE"):
                kolejnoscFiltr = str(input("Czy lista malych grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista malych grzybów od A->Z:")
                    for grzyby in sorted(maleGrzyby):
                        print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break
                else:
                    print()
                    print("Lista malych grzybów od Z->A:")
                    for grzyby in sorted(maleGrzyby, reverse = True):
                        print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break

            elif (filtr == "SREDNIE"):
                kolejnoscFiltr = str(input("Czy lista srednich grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista srednich grzybów od A->Z:")
                    for grzyby in sorted(srednieGrzyby):
                        print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break
                else:
                    print()
                    print("Lista srednich grzybów od Z->A:")
                    for grzyby in sorted(srednieGrzyby, reverse = True):
                        print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break

            elif (filtr == "DUZE"):
                kolejnoscFiltr = str(input("Czy lista duzych grzybów ma być wyświetlona od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Lista duzych grzybów od A->Z:")
                    for grzyby in sorted(duzeGrzyby):
                        print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break
                else:
                    print()
                    print("Lista duzych grzybów od Z->A:")
                    for grzyby in sorted(duzeGrzyby, reverse = True):
                        print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"])
                    break

            elif (filtr == "DWA"):
                while True:
                    zbior = []
                    print()
                    filtrRozmiar = str(input("Najpierw podaj czy chcesz wyfiltrować MALE, SREDNIE czy DUZE grzyby: ").upper())
                    if filtrRozmiar == "MALE" or filtrRozmiar == "SREDNIE" or filtrRozmiar == "DUZE":
                        filtrJadalne = str(input("Czy wyfiltrowane grzyby mają być jadalne? TAK/NIE: ").capitalize())
                        if filtrJadalne == "Tak" or filtrJadalne == "Nie":
                            break
                        else:
                            print("Błąd spróbuj ponownie")
                            continue
                    else:
                        print("Błąd spróbuj ponownie")
                        continue
                kolejnoscFiltr = str(input("Czy wyniki filtrowania mają być wyświetlone od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    if filtrRozmiar == "MALE":
                        for nazwy in maleGrzyby:
                            if atlas[nazwy]["Jadalny"] == filtrJadalne:
                                zbior.append(nazwy)
                    elif filtrRozmiar == "SREDNIE":
                        for nazwy in srednieGrzyby:
                            if atlas[nazwy]["Jadalny"] == filtrJadalne:
                                zbior.append(nazwy)
                    elif filtrRozmiar == "DUZE":
                        for nazwy in duzeGrzyby:
                            if atlas[nazwy]["Jadalny"] == filtrJadalne:
                                zbior.append(nazwy)
                    for grzyby in zbior:
                        print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"], ", Kolor:", atlas[grzyby]["Kolor"],", Jadalny:", atlas[grzyby]["Jadalny"])
                    break

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