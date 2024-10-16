import matplotlib.pyplot as plt
import random

dictionary = {}
for i in range(1, 46):
    dictionary[i] = 0


# Funktion, um eine bestimmte Anzahl von Zufallszahlen aus einer Liste zu ziehen
def draw(li, how_many):
    """
    Parameter:
    - li: Liste der verfügbaren Zahlen (z.B. [1, 2, ..., 45])
    - how_many: Anzahl der zu ziehenden Zahlen
    """
    drawn_numbers = []  # Liste, um die gezogenen Zahlen zu speichern
    for j in range(how_many):
        # Wähle eine Zufallszahl aus der Liste li aus
        num = random.randint(0, len(li) - 1)
        drawn_numbers.append(li[num])  # Füge die gezogene Zahl zur Liste hinzu

        # Erhöhe die Häufigkeit der gezogenen Zahl im Wörterbuch
        dictionary[li[num]] += 1

        # Entferne die gezogene Zahl aus der Liste, um doppelte Ziehungen zu vermeiden
        li = li[:num] + li[num + 1:]

    return drawn_numbers


# Simulieren von 1000 Ziehungen von 6 Zufallszahlen
for i in range(1000):
    # Erstelle eine Liste von Zahlen von 1 bis 45
    numbers = list(range(1, 46))

    # Ziehe 6 Zufallszahlen aus der Liste numbers
    result = draw(numbers, 6)

    print(f" {i + 1}: {sorted(result)}")

# Ausgabe der Häufigkeiten der gezogenen Zahlen
print(dictionary)

# Erstellen eines Balkendiagramms, um die Häufigkeit der gezogenen Zahlen zu visualisieren
plt.bar(dictionary.keys(), dictionary.values())  # Erstelle Balken für jede Zahl
plt.xlabel('Zahlen 1-45')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der gezogenen Zahlen nach 1000 Ziehungen')
plt.show()
