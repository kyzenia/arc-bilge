def readText():
    try:
        dottxt = open("text.txt", "r")
        text = dottxt.read()
        dottxt.close()
        return text
    except:
        print("Oops! >> bilge.py >> readText() >> except:")

def mainMenu():
    sharp, blank = "# "*44, ""
    title = "Welcome To Bilge v0.1"
    subtitle = "Please select among available options below (1-3):"
    slc1 = "                 1) Encrypt Text"
    slc2 = "                 2) Decrypt Text"
    exit = "                 3) Exit"
    print(f"\n{sharp}\n"f"#{blank:^85}#\n"f"#{title:^85}#\n"f"#{blank:^85}#\n"f"#{subtitle:^85}#\n"f"#{blank:^85}#\n"f"#{slc1:<85}#\n"
          f"#{slc2:<85}#\n"f"#{exit:<85}#\n"f"#{blank:^85}#\n"f"{sharp}\n")

def mainMenuSelection():
    loop, loop1, loop2, loop3 = 1, 1, 1, 1
    while loop == 1:
        try:
            while loop1 == 1:
                userChoice = int(input("Your selection: "))
                if userChoice < 1 or userChoice > 3:
                    print("\nPlease enter a valid selection!\n")
                    loop1 = 1
                else:
                    loop1 = 0
        except:
            print("\nPlease enter a valid selection!\n")
            loop = 1
        else:
            loop = 0
    if userChoice == 1:
        while loop2 == 1:
            try:
                userSeed = int(input("Enter your seed (int): "))
                uKey = int(input("Enter your key: "))
            except:
                print("\nPlease enter a valid key")
                loop2 = 1
            else:
                uKey = str(uKey)
                userKey = [num for num in uKey]
                loop2 = 0
        import encrypt
        encrypt.main(readText(), userKey, userSeed)
    elif userChoice == 2:
        while loop3 == 1:
            try:
                userSeed = int(input("Enter your seed (int): "))
                uKey = int(input("Enter your key: "))
            except:
                print("\nPlease enter a valid key")
                loop3 = 1
            else:
                uKey = str(uKey)
                userKey = [num for num in uKey]
                loop3 = 0
        import decrypt
        decrypt.main(readText(), userKey, userSeed)
    else:
        import credits
        credits.main()
        input("Have a great day!\nPlease press enter to exit the program...")

def main():
    mainMenu()
    mainMenuSelection()

if __name__ == '__main__':
    main()