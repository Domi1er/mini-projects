import random

print("===== Python Quiz =====")
print("Willkommen zum Quiz!")

fragen = [
    {
        "frage": "Was ist die Hauptstadt von Deutschland?",
        "antwort": "Berlin"
    },
    {
        "frage": "Wie viele Kontinente gibt es?",
        "antwort": "7"
    },
    {
        "frage": "Wie viel ist 5 + 7?",
        "antwort": "12"
    }
]
random.shuffle(fragen)
punkte = 0

for frage in fragen:
    print(frage["frage"])

    antwort = input("Deine Antwort: ")

    if antwort.lower() == frage["antwort"].lower():
        print(" ✓ Richtig!")
        punkte += 1
    else:
        print(f" ✗ Falsch! ")
        print(f"Die richtige Antwort ist: {frage['antwort']}")

prozent = (punkte / len(fragen)) * 100

print()
print("==== Ergebnis ====")
print(f"{punkte}/{len(fragen)} richtig - {prozent: .1f} %")