# Du ska skapa klassen Account och implementera menyn så att användaren kan skapa konto och logga in på kontot.

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
