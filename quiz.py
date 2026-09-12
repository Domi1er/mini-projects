import random

print("===== Python Quiz =====")
print("Willkommen zum Quiz!")

fragen = [
    {
        "frage": "Was gibt len('Hallo') zurück?",
        "antwort": "5",
        "kategorie": "Python"
    },
    {
        "frage": "Was ist eine Variable?",
        "antwort": "Speicherplatz für einen Wert",
        "kategorie": "Python"
    },
    {
        "frage": "Wie viel ist 5 + 7?",
        "antwort": "12",
        "kategorie": "Mathematik"
    },
    {
        "frage": "Wie viel ist 8 * 6?",
        "antwort": "48",
        "kategorie": "Mathematik"
    }
]
while True:
    print()
    print("Wähle eine Kategorie:")
    print("1 - Python")
    print("2 - Mathematik")

    auswahl = input("Deine Auswahl: ")

    if auswahl == "1":
        kategorie = "Python"
        break
    elif auswahl == "2":
        kategorie = "Mathematik"
        break
    else:
        print("Ungültige Auswahl. Bitte wähle 1 oder 2.")    

fragen = [frage for frage in fragen if frage["kategorie"] == kategorie]

random.shuffle(fragen)
punkte = 0

def ergebnis_anzeiggen(punkte, anzahl_fragen):
    prozent = punkte / anzahl_fragen * 100

    print()
    print("==== Ergebnis ====")
    print(f"{punkte}/{anzahl_fragen} richtig - {prozent:.1f} %")

    if prozent == 100:
        print("Perfekt! 🎉")
    elif prozent >= 80:
        print("Sehr gut! 👍")
    elif prozent >= 60:
        print("Gut gemacht!")
    else:
        print("Strend dich mal an! 😅")

for frage in fragen:
    print(frage["frage"])

    antwort = input("Deine Antwort: ")

    if antwort.lower() == frage["antwort"].lower():
        print(" ✓ Richtig!")
        punkte += 1
    else:
        print(f" ✗ Falsch! ")
        print(f"Die richtige Antwort ist: {frage['antwort']}")

ergebnis_anzeiggen(punkte, len(fragen))