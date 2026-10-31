""" Temperature Analyzer
Entwickle ein Python-Programm, das die Temperatur eines Raumes analysiert und 
anhand bestimmter Bedingungen eine Bewertung ausgibt.

Anforderungen
    1. Der Benutzer soll eine Temperatur in Grad Celsius eingeben können.
    2. Das Programm soll die Temperatur einer der folgenden Kategorien zuordnen:
Temperatur	                    Ausgabe
Unter 16 °C	                    Too cold
16 °C bis unter 20 °C	        Cool
20 °C bis einschließlich 24 °C	Comfortable
Über 24 °C bis 28 °C	        Warm
Über 28 °C	                    Too hot

3. Zusätzlich soll das Programm die eingegebene Temperatur in Fahrenheit umrechnen und ausgeben.
Beispielausführung

TERMINAL

Enter temperature in Celsius: 22

Category: Comfortable
Fahrenheit: 71.6 °F

Zusatzanforderungen
- Dein Programm muss auch negative Temperaturen verarbeiten können.
- Dezimalzahlen müssen unterstützt werden.
- Schreibe sämtliche Variablen und Ausgaben auf Englisch.
- Der Code soll gut lesbar sein.
"""

temperature_celsius = float(input("Temperature in C°: "))

if temperature_celsius > 28.0:
    print("\nCategory: Too hot")
elif temperature_celsius > 24.0:
    print("\nCategory: Warm")
elif temperature_celsius >= 20.0:
    print("\nCategory: Comfortable")
elif temperature_celsius >= 16.0:
    print("\nCategory: Cool")
else:
    print("\nCategory: Too cold")

temperature_fahrenheit = 1.8 * temperature_celsius + 32
print("Fahrenheit:", temperature_fahrenheit, "°F")