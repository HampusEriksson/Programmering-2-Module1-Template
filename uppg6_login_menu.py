# Du ska skapa klassen Account och implementera menyn sa att anvandaren kan skapa konto och logga in pa kontot.
# Krav pa Account:
# - username (str)
# - password (str)
# - balance (int eller float)
# - __str__-metod som skriver ut username och saldo
#
# Krav pa menyn:
# 1) Skapa konto: lagg till ett Account-objekt i listan accounts.
# 2) Logga in: anvandaren far hogst 3 forsok.
#    Om inloggning lyckas ska anvandaren kunna gora MINST en sak:
#    - andras password, eller
#    - satta in/ta ut pengar.
# 3) Avsluta program.

# Loginmeny
# Skelettkod till uppgiften

accounts = []


class Account:
    def __init__(self) -> None:
        # TODO Skriv metoden
        pass

    def __str__(self) -> str:
        pass


while True:
    menyval = input("1. Skapa konto\n" "2. Logga in\n" "3. Avsluta program\n")

    if menyval == "1":
        # TODO Skapa ett konto genom att lägga till ett Account-objekt i listan accounts
        pass

    elif menyval == "2":
        # TODO Användaren ska få logga in med username och password
        # Om de lyckas logga in ska användaren kunna ändra på något med kontot, t.ex. användarnamn, lösenord eller pengar på kontot.
        # Ge användaren ett visst antal försök att logga in. Om de går över det antalet försök ska programmet avslutas.
        pass

    elif menyval == "3":
        break

    else:
        print("Det menyvalet finns ej.")
