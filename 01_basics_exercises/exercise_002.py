""" Number Analyzer
Entwickle ein Python-Programm, das eine beliebige Anzahl ganzer Zahlen analysiert.
Anforderungen
1. Der Benutzer gibt nacheinander ganze Zahlen ein.
2. Mit der Eingabe done wird die Eingabe beendet.
3. Anschließend soll das Programm folgende Werte ausgeben:
   - Anzahl der eingegebenen Zahlen
   - Summe aller Zahlen
   - Durchschnitt aller Zahlen
   - Kleinste Zahl
   - Größte Zahl
   - Anzahl positiver, negativer und der Zahlen mit dem Wert null
4. Das Programm muss auch funktionieren, wenn der Benutzer sofort done eingibt. Es darf dabei nicht abstürzen.
Beispielausführung
TERMINAL

Enter number (or 'done'): 10
Enter number (or 'done'): -5
Enter number (or 'done'): 0
Enter number (or 'done'): 15
Enter number (or 'done'): done

Count: 4
Sum: 20
Average: 5.0
Minimum: -5
Maximum: 15
Positive: 2
Negative: 1
Zero: 1

Zusatzanforderungen
- Verwende englische Variablennamen.
- Der Benutzer muss beliebig viele Zahlen eingeben können.
- Der Durchschnitt soll mit zwei Nachkommastellen ausgegeben werden.
- Falls keine Zahlen eingegeben wurden, soll eine verständliche Meldung erscheinen.
"""

number_list = []
number = 0
while number != "done":
   number = input("Enter number (or 'done'): ")
   try:
      number_list.append(int(number))
   except ValueError:
      if number != "done":
         print("Invalid input! Pleaser enter integer numbers only.")

if number_list:
   count = len(number_list)
   print("\nCount:", count)

   sum_list = sum(number_list)
   print("Sum:", sum_list)

   average = sum_list / len(number_list)
   print(f"Average: {average:.2f}")

   minimum = min(number_list)
   print("Minimum:", minimum)

   maximum = max(number_list)
   print("Maximum:", maximum)

   positive = 0
   negative = 0
   zero = 0
   for n in number_list:
      if n > 0:
         positive += 1
      elif n < 0:
         negative += 1
      else:
         zero += 1
      
   print("Positive:", positive)
   print("Negative:", negative)
   print("Zero:", zero)
else:
   print("No numbers were entered.")