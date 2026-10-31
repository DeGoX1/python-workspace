""" Password Validator
Aufgabenstellung

Entwickle ein Python-Programm, das ein eingegebenes Passwort anhand festgelegter Regeln überprüft.
Anforderungen
1. Der Benutzer gibt ein Passwort ein.
2. Das Passwort ist nur gültig, wenn es sämtliche Bedingungen erfüllt:
   - Mindestens 10 Zeichen lang
   - Mindestens einen Großbuchstaben
   - Mindestens einen Kleinbuchstaben
   - Mindestens eine Ziffer (0-9)
   - Mindestens eines dieser Sonderzeichen: ! @ # $ % &
   - Keine Leerzeichen
3. Das Programm soll für jede nicht erfüllte Bedingung eine verständliche englische Fehlermeldung ausgeben.
4. Wenn sämtliche Bedingungen erfüllt sind, soll Password accepted! erscheinen.
5. Der Benutzer darf beliebig oft neue Passwörter eingeben, bis ein gültiges Passwort gefunden wurde.
Beispielausführung
TERMINAL

Enter password: hello

Password must contain at least 10 characters.
Password must contain an uppercase letter.
Password must contain a digit.
Password must contain a special character.

Enter password: Hello12345!

Password accepted!

Zusatzanforderungen
- Verwende ausschließlich englische Variablennamen und Ausgaben.
- Das Programm muss alle verletzten Regeln melden, nicht nur den ersten Fehler.
- Die Reihenfolge der Fehlermeldungen ist frei wählbar.
- Ein ungültiges Passwort darf das Programm nicht beenden.
"""
password_accepted = False
digit_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_char_list = ["!", "@", "#", "$", "%", "&"]

while not password_accepted:
    accepted_check = True
    contain_upper = False
    contain_lower = False
    contain_digit = False
    contain_special_char = False
    contain_whitespace = False
    
    password = input("Enter password: ")
    print()
    
    if len(password) < 10:
        print("Password must contain at least 10 characters.")
        accepted_check = False

    # Checks each character and tracks whether the required character types are present.
    for character in password:
        if character.isupper() and not contain_upper:
            contain_upper = True
        if character.islower() and not contain_lower:
            contain_lower = True
        if character in digit_list and not contain_digit:
            contain_digit = True
        if character in special_char_list and not contain_special_char:
            contain_special_char = True
        if character.isspace() and not contain_whitespace:
            contain_whitespace = True
     

    if not contain_upper:
        print("Password must contain an uppercase letter.")
        accepted_check = False

    if not contain_lower:
        print("Password must contain a lowercase letter.")
        accepted_check = False

    if not contain_digit:
        print("Password must contain a digit.")
        accepted_check = False

    if not contain_special_char:
        print("Password must contain a special character.")
        accepted_check = False

    if contain_whitespace:
        print("Password must not contain any whitespace characters.")
        accepted_check = False

    
    if accepted_check:
        password_accepted = True
    else:
        print()

print("Password accepted!")