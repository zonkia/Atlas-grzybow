import os
import ast
import json
os.chdir(os.path.dirname(__file__))

with open("atlas.json", "r", encoding="UTF-8-sig") as atlas_file_json:
    atlas = json.load(atlas_file_json)

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

while True:
    print()
    wybor = str(input("Twoja komenda: ").upper())

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

    if (wybor == "POKAZ"):
        for grzyby in atlas:
            print()
            print(grzyby)
            for cechy in atlas[grzyby]:
                print(cechy,":",atlas[grzyby][cechy])
        continue
                
    elif (wybor == "SZUKAJ"):
        while True:
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
        jadalnoscGrzyba = str(input("Czy grzyb jest jadalny? TAK/NIE ").capitalize())
        kolorGrzyba = str(input("Podaj jaki kolor i cechy ma kapelusz: "))
        szerGrzyba = float(input("Podaj szerokość trzonu: "))
        wysGrzyba = float(input("Podaj wysokość grzyba: "))
        srGrzyba = float(input("Podaj średnicę kapelusza: "))
        while True:
            if jadalnoscGrzyba == "Tak" or jadalnoscGrzyba == "Nie":
                break
            else:
                print("Błąd. Jadalność grzyba może być tylko TAK lub NIE. Spróbuj ponownie")
                jadalnoscGrzyba = str(input("Czy grzyb jest jadalny? TAK/NIE ").capitalize())
                continue

        with open("atlas.json", "w", encoding="UTF-8-sig") as new_atlas:
            atlas[nazwaGrzyba] = {"Jadalny":jadalnoscGrzyba, "Kolor":kolorGrzyba, "Szer. trzonu [cm]":szerGrzyba, "Wysokość [cm]":wysGrzyba, "Śr. Kapelusza [cm]": srGrzyba}
            json.dump(atlas, new_atlas, ensure_ascii=False, indent=4)

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
        while True:
            doUsuniecia = str(input("Podaj nazwę grzyba do usunięcia z atlasu: ").capitalize())
            try:
                del(atlas[doUsuniecia])
                with open("atlas.json", "w", encoding="UTF-8-sig") as new_atlas:
                    json.dump(atlas, new_atlas, ensure_ascii=False, indent=4)

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
                            print("Jadalność może być tylko TAK lub NIE. Spróbuj ponownie")
                            continue
                    else:
                        print("Błąd w nazwie spróbuj ponownie")
                        continue
                kolejnoscFiltr = str(input("Czy wyniki filtrowania mają być wyświetlone od A->Z? TAK/NIE ").upper())
                if kolejnoscFiltr == "TAK":
                    print()
                    print("Poniżej lista od A->Z grzybów:",filtrRozmiar,", Jadalne:", filtrJadalne.upper())
                    if filtrRozmiar == "MALE":
                        for nazwy in sorted(maleGrzyby):
                            if atlas[nazwy]["Jadalny"] == filtrJadalne:
                                zbior.append(nazwy)
                    elif filtrRozmiar == "SREDNIE":
                        for nazwy in sorted(srednieGrzyby):
                            if atlas[nazwy]["Jadalny"] == filtrJadalne:
                                zbior.append(nazwy)
                    elif filtrRozmiar == "DUZE":
                        for nazwy in sorted(duzeGrzyby):
                            if atlas[nazwy]["Jadalny"] == filtrJadalne:
                                zbior.append(nazwy)
                    for grzyby in zbior:
                        print(grzyby,"- Wysokość [cm]:", atlas[grzyby]["Wysokość [cm]"], ", Śr. Kapelusza [cm]:", atlas[grzyby]["Śr. Kapelusza [cm]"],", Szer. trzonu [cm]:", atlas[grzyby]["Szer. trzonu [cm]"], ", Kolor:", atlas[grzyby]["Kolor"],", Jadalny:", atlas[grzyby]["Jadalny"])
                    break
                else:
                    print()
                    print("Poniżej lista od Z->A grzybów:",filtrRozmiar,", Jadalne:", filtrJadalne.upper())
                    if filtrRozmiar == "MALE":
                        for nazwy in sorted(maleGrzyby, reverse = True):
                            if atlas[nazwy]["Jadalny"] == filtrJadalne:
                                zbior.append(nazwy)
                    elif filtrRozmiar == "SREDNIE":
                        for nazwy in sorted(srednieGrzyby, reverse = True):
                            if atlas[nazwy]["Jadalny"] == filtrJadalne:
                                zbior.append(nazwy)
                    elif filtrRozmiar == "DUZE":
                        for nazwy in sorted(duzeGrzyby, reverse = True):
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
                jadalnoscEdytowana = str(input("Czy grzyb jest jadalny? TAK/NIE: ").capitalize())
                atlas[edytowanaNazwa]["Kolor"] = str(input("Podaj kolor kapelusza: "))
                atlas[edytowanaNazwa]["Szer. trzonu [cm]"] = float(input("Podaj szerokość trzonu: "))
                atlas[edytowanaNazwa]["Wysokość [cm]"] = float(input("Podaj wysokość grzyba: "))
                atlas[edytowanaNazwa]["Śr. Kapelusza [cm]"] = float(input("Podaj średnicę kapelusza: "))
                while True:
                    if (jadalnoscEdytowana == "Tak") or (jadalnoscEdytowana == "Nie"):
                        atlas[edytowanaNazwa]["Jadalny"] = jadalnoscEdytowana
                        break
                    else:
                        print("Błąd. Jadalność grzyba może być tylko TAK lub NIE. Spróbuj ponownie")
                        jadalnoscEdytowana = str(input("Czy grzyb jest jadalny? TAK/NIE: ").capitalize())
                        continue
                print()
                with open("atlas.json", "w", encoding="UTF-8-sig") as new_atlas:
                    json.dump(atlas, new_atlas, ensure_ascii=False, indent=4)
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