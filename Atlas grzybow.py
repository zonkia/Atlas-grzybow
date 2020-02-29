print("Witaj w atlasie grzybów. Wybierz co chcesz zrobić:")
print("Wpisz POKAZ, aby zobaczyc wszystkie wpisy")
print("Wpisz SZUKAJ, aby wyszukac interesującego Ciebie grzyba")
print("Wpisz DODAJ, aby dodać nowego grzyba i opis")
print("Wpisz USUN, aby usunąć grzyba z atlasu")

loop = 1
loopSearch = 1
loopDelete = 1

atlas = {
            "Prawdziwek": {"Rozmiar": "Śr. Kapelusza: 6 - 25cm; Wys. trzonu: 20cm; Szer. trzonu: 1,5 - 10cm", "Kolor": "Jasnobrązowy / ciemnobrązowy", "Jadalny": "Tak"},
            "Muchomor": {"Rozmiar": "Śr. Kapelusza: do 20cm; Wys. trzonu: 20cm; Szer. trzonu: do 3cm", "Kolor": "Czerwony kapelusz z białymi kropkami", "Jadalny": "Nie"},
            "Kurka": {"Rozmiar": "Śr. Kapelusza: 1 - 12cm; Wys. trzonu: 3 -6cm; Szer. trzonu: do 2,5cm", "Kolor": "Żółty / pomarańczowożółty", "Jadalny": "Tak"}
}

while (loop == 1):
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
                else:
                    break

    elif (wybor == "DODAJ"):
        NazwaGrzyba = str(input("Podaj nazwę grzyba: ").capitalize())
        RozmiarGrzyba = str(input("Podaj wymiary kapelusza i trzonka: "))
        KolorGrzyba = str(input("Podaj jaki kolor i cechy ma kapelusz: "))
        JadalnoscGrzyba = str(input("Czy grzyb jest jadalny? TAK/NIE ").capitalize())
        atlas[NazwaGrzyba] = {"Rozmiar":RozmiarGrzyba, "Kolor":KolorGrzyba, "Jadalny":JadalnoscGrzyba}
        wpis = str(input("Dodano grzyba do atlasu. Czy chcesz zobaczyć wpis? TAK/NIE ").upper())
        if (wpis == "TAK"):
            print()
            print(NazwaGrzyba)
            for grzyby in atlas:
                for cechy in atlas[grzyby]:
                    if grzyby == NazwaGrzyba:
                        print(cechy,":",atlas[grzyby][cechy])
                    else:
                        pass
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
    else:
        print("Nie wpisałeś prawidłowej komendy. Możliwe komendy: POKAZ / SZUKAJ / DODAJ / USUN")
        continue