""" Inventory Manager
Aufgabenstellung

Entwickle ein Python-Programm zur Verwaltung eines kleinen Warenlagers.

Das Programm soll es ermöglichen, Produkte hinzuzufügen, Lagerbestände zu verändern und Informationen über vorhandene Produkte abzurufen.
1. Anforderungen
Der Benutzer soll über ein Menü folgende Aktionen auswählen können:
TERMINAL - MAIN MENU

===== INVENTORY MANAGER =====

1. Add product
2. Update stock
3. Remove product
4. Search product
5. Show inventory
6. Exit

Choose an option:

Option 1 - Add product

Der Benutzer gibt einen Produktnamen, einen Preis und die verfügbare Stückzahl ein.
- Produktnamen müssen eindeutig sein.
- Preise dürfen nicht negativ sein.
- Stückzahlen müssen ganze Zahlen größer oder gleich null sein.
- Doppelte Produkte dürfen nicht angelegt werden.
Option 2 - Update stock

Der Benutzer kann den Lagerbestand eines vorhandenen Produkts verändern.
- Ein Bestand kann erhöht oder verringert werden.
- Der neue Bestand darf niemals negativ sein.
- Nicht vorhandene Produkte müssen erkannt werden.
Option 3 - Remove product

Ein vorhandenes Produkt kann vollständig aus dem Lager entfernt werden.

- Bei einem unbekannten Produkt erscheint eine Fehlermeldung.

Option 4 - Search product

Der Benutzer gibt einen Produktnamen ein.

Das Programm zeigt dessen Preis, Stückzahl und gesamten Lagerwert an.

Option 5 - Show inventory

Alle gespeicherten Produkte werden angezeigt.

Zusätzlich sollen folgende Werte berechnet werden:
- Anzahl unterschiedlicher Produkte
- Gesamtzahl aller gelagerten Artikel
- Gesamtwert des gesamten Warenlagers
Option 6 - Exit

Das Programm wird mit einer Abschiedsmeldung beendet.
2. Beispielausführung
TERMINAL

Choose an option: 1
Product name: Keyboard
Price: 49.99
Quantity: 10

Product added successfully!

Choose an option: 1
Product name: Mouse
Price: 19.99
Quantity: 5

Product added successfully!

Choose an option: 5

===== INVENTORY =====
Keyboard | 49.99 € | Quantity: 10
Mouse    | 19.99 € | Quantity: 5

Different products: 2
Total quantity: 15
Total inventory value: 599.85 €

3. Zusätzliche Anforderungen
- Das Programm soll so lange laufen, bis der Benutzer Exit auswählt.
- Ungültige Menüeingaben dürfen keinen Absturz verursachen.
- Ungültige Preise und Stückzahlen müssen abgefangen werden.
- Produktnamen dürfen nicht leer sein.
- Bei der Suche nach Produkten soll Groß- und Kleinschreibung keine Rolle spielen.
- Geldbeträge sollen mit zwei Nachkommastellen angezeigt werden.
- Alle Variablennamen, Kommentare und Programmausgaben sollen auf Englisch sein.
- Die Daten müssen zunächst nur während der Programmausführung gespeichert bleiben."""

exit = False
menu = """===== INVENTORY MANAGER =====

1. Add product
2. Update stock
3. Remove product
4. Search product
5. Show inventory
6. Exit
"""
product_list = []
while not exit:
    print(menu)
    menu_option = input("Choose an option: ")
    match menu_option:
        case "1":
            product_name = input("Product name: ")
        case "2":
            continue
        case "3":
            continue
        case "4":
            continue
        case "5":
            continue
        case "6":
            exit = True
        case _:
            print("Invalid input, please try again.\n")

