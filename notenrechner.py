def note_eingeben(nummer):
    while True:
        try:
            note = int(input(f"Note {nummer}: "))

            if 0 <= note <= 15:
                return note
            else:
                print("Bitte gib eine Note zwischen 0 und 15 ein.")

        except ValueError:
            print("Bitte gib eine Zahl ein.")

print("Willkommen beim Notenrechner!")

anzahl_noten = int(input("Wie viele Noten möchtest du eingeben? "))

summe = 0
gesamt_gewichtung = 0

for i in range(anzahl_noten):
    note = note_eingeben(i + 1)
    gewichtung = int(input(f"Gewichtung für Note {i + 1}: "))
    summe += note * gewichtung
    gesamt_gewichtung += gewichtung

durchschnitt = summe / gesamt_gewichtung

print(f"Dein Durchschnitt beträgt: {durchschnitt:.2f}")