import random
from pathlib import Path
from itertools import cycle
DATA_CHUNKS = 16 * 1024

def main():
    print("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                                       #")
    print("#                      Bilge v2.1.1                     #")
    print("#                                                       #")
    print("#   Please select among available options below (1-3):  #")
    print("#                                                       #")
    print("#                   1) Encrypt Text                     #")
    print("#                   2) Decrypt Text                     #")
    print("#                   3) Exit                             #")
    print("#                                                       #")
    print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")

    user_choice = get_user_choice()
    if user_choice == 3:
        credits()
        input("Have a great day!\nPlease press enter to exit the program...")
        return
    user_seed, user_key = get_user_seed_and_key()
    alfabetas, rev_alfabetas = key_gen(user_seed)
    if user_choice == 1:
        if encrypt(user_key, alfabetas, rev_alfabetas) == 0:
            credits()
            clean_up()
            print(f'''Encryption complete. Please check "text.txt"\n''')
        else:
            credits()
            print("Failed to encrypt your text due to unsupported characters!\n")
    elif user_choice == 2:
        if decrypt(user_key, alfabetas, rev_alfabetas) == 0:
            credits()
            clean_up()
            print(f'''Decryption complete. Please check "text.txt"\n''')
        else:
            credits()
            print("Failed to decrypt your text due to unsupported characters!\n")
    input("Have a great day! Please press enter to exit the program...")

def get_user_choice():
    while True:
        try:
            user_choice = int(input("Your selection: "))
            if 1 <= user_choice <= 3:
                return user_choice
        except ValueError:
            pass
        print("\nPlease enter a valid selection!\n")

def get_user_seed_and_key():
    while True:
        try:
            user_seed = int(input("Enter your seed (integer): "))
            user_key = abs(int(input("Enter your key (positive integer): ")))
            return user_seed, [int(i) for i in str(user_key)]
        except ValueError:
            print("\nPlease enter a valid seed/key!\n")

def encrypt(user_key, alfabetas, rev_alfabetas):
    CHUNK = DATA_CHUNKS
    alfabeta0 = alfabetas[0]
    rev = rev_alfabetas
    key = user_key
    key_iter = cycle(key)
    check = True
    while check:
        try:
            with open("text.txt", "r", encoding="utf-8") as file_in, open("temp.txt", "w", encoding="utf-8") as file_out:
                read = file_in.read
                write = file_out.write
                while data_chunk := read(CHUNK):
                    data_ready = []
                    append = data_ready.append
                    for value in data_chunk:
                        append(rev[next(key_iter)][alfabeta0[value]])
                    write("".join(data_ready))
        except FileNotFoundError:
            with open("text.txt", "w", encoding="utf-8") as file_create:
                file_create.write('''This is a test message. Please replace the contents of the file "text.txt" with your own before using Bilge again.''')
                check = True
        except KeyError:
            file = Path("temp.txt")
            if file.exists():
                file.unlink()
            return 1
        except KeyboardInterrupt:
            file = Path("temp.txt")
            if file.exists():
                file.unlink()
            return 1
        else:
            check = False
            return 0

def decrypt(user_key, alfabetas, rev_alfabetas):
    CHUNK = DATA_CHUNKS
    rev_alfabeta0 = rev_alfabetas[0]
    alfabe = alfabetas
    key = user_key
    key_iter = cycle(key)
    check = True
    while check:
        try:
            with open("text.txt", "r", encoding="utf-8") as file_in, open("temp.txt", "w", encoding="utf-8") as file_out:
                read = file_in.read
                write = file_out.write
                while data_chunk := read(CHUNK):
                    data_ready = []
                    append = data_ready.append
                    for value in data_chunk:
                        append(rev_alfabeta0[alfabe[next(key_iter)][value]])
                    write("".join(data_ready))
        except FileNotFoundError:
            with open("text.txt", "w", encoding="utf-8") as file_create:
                file_create.write('''This is a test message. Please replace the contents of the file "text.txt" with your own before using Bilge again.''')
                check = True
        except KeyError:
            file = Path("temp.txt")
            if file.exists():
                file.unlink()
            return 1
        except KeyboardInterrupt:
            file = Path("temp.txt")
            if file.exists():
                file.unlink()
            return 1
        else:
            check = False
            return 0

def key_gen(user_seed):
    base = list('''\n !"“”#%&'‘’()*+,-./0123456789:;<=>?@ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ[]^_`abcçdefgğhıijklmnoöpqrsştuüvwxyz{|}~«»\\''')
    alfabetas, rev_alfabetas = [], []
    dict_alfabeta = {key: item for item, key in enumerate(base)}
    alfabetas.append(dict_alfabeta)
    rev_alfabetas.append({key: item for item, key in dict_alfabeta.items()})
    for i in range(9):
        chars = base.copy()
        seedset = random.Random(int(user_seed)+i)
        seedset.shuffle(chars)
        dict_alfabeta = {key: item for item, key in enumerate(chars)}
        alfabetas.append(dict_alfabeta)
        rev_alfabetas.append({key: item for item, key in dict_alfabeta.items()})
    return tuple(alfabetas), tuple(rev_alfabetas)

def clean_up():
    with open("temp.txt", "r", encoding="utf-8") as file_in, open("text.txt", "w", encoding="utf-8") as file_out:
        while data_chunk := file_in.read(DATA_CHUNKS):
            file_out.write(data_chunk)
    file = Path("temp.txt")
    if file.exists():
        file.unlink()

def credits():
    print("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                                       #")
    print("#                           #                           #")
    print("#                         #                             #")
    print("#                       #                               #")
    print("#                     #                                 #")
    print("#           #       #               #                   #")
    print("#           #     #               # #                   #")
    print("#           #   #               #   #   #               #")
    print("#           # #               #     # #                 #")
    print("#           #       #       #       #       #           #")
    print("#           # #       #           # #     #             #")
    print("#           #   #       #       #   #   #               #")
    print("#           #     #       #   #     # #                 #")
    print("#           #       #       #       #                   #")
    print("#                     #     #                           #")
    print("#                       #   #                           #")
    print("#                         # #                           #")
    print("#                           #                           #")
    print("#                                                       #")
    print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")

if __name__ == '__main__':
    main()