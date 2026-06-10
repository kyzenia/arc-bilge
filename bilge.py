def readText():
    loop = 1
    while loop == 1:
        try:
            dottxt = open("text.txt", "r")
            text = dottxt.read()
            dottxt.close()
            loop = 0
            return text
        except FileNotFoundError:
            dottxt = open("text.txt", "w")
            text = '''This is a test message. Please replace the contents of the file "text.txt" with your own before using Bilge again.'''
            dottxt.write(text)
            dottxt.close()
            loop = 1
        except:
            print("Oops! >> bilge.py >> readText() >> except:")

def mainMenu():
    sharp, blank = "# "*44, ""
    title = "Welcome To Bilge v0.2.5"
    subtitle = "Please select among available options below (1-3):"
    slc1 = "                 1) Encrypt Text"
    slc2 = "                 2) Decrypt Text"
    exit = "                 3) Exit"
    print(f"\n{sharp}\n"f"#{blank:^85}#\n"f"#{title:^85}#\n"f"#{blank:^85}#\n"f"#{subtitle:^85}#\n"f"#{blank:^85}#\n"f"#{slc1:<85}#\n"
          f"#{slc2:<85}#\n"f"#{exit:<85}#\n"f"#{blank:^85}#\n"f"{sharp}\n")

def mainMenuSelection():
    loop, loop1, loop2, loop3, userChoice = 1, 1, 1, 1, None
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
                userSeed = int(input("Enter your seed (integer): "))
                uKey = int(input("Enter your key (positive integer): "))
            except:
                print("\nPlease enter a valid seed/key!")
                loop2 = 1
            else:
                if uKey < 0:
                    uKey = (uKey * (-1))
                uKey = str(uKey)
                userKey = [num for num in uKey]
                loop2 = 0
        import encrypt_decrypt
        encrypt_decrypt.main(readText(), userKey, userSeed, userChoice)
    elif userChoice == 2:
        while loop3 == 1:
            try:
                userSeed = int(input("Enter your seed (integer): "))
                uKey = int(input("Enter your key (positive integer): "))
            except:
                print("\nPlease enter a valid seed/key!")
                loop3 = 1
            else:
                if uKey < 0:
                    uKey = (uKey * (-1))
                uKey = str(uKey)
                userKey = [num for num in uKey]
                loop3 = 0
        import encrypt_decrypt
        encrypt_decrypt.main(readText(), userKey, userSeed, userChoice)
    else:
        from credits import credits
        credits()
        input("Have a great day!\nPlease press enter to exit the program...")

def main():
    mainMenu()
    mainMenuSelection()

if __name__ == '__main__':
    main()