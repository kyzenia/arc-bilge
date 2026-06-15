def assign(text, userKey):
    from itertools import cycle
    cycle_it = cycle(userKey)
    list_char,list_num = [],[]
    for char in text:
        num = next(cycle_it)
        list_char.append(char)
        list_num.append(num)
    return list_char, list_num

def assignNum(text, userKey):
    from itertools import cycle
    cycle_it = cycle(userKey)
    list_num = []
    for char in text:
        num = next(cycle_it)
        list_num.append(num)
    return list_num

def encrypt(userKey, alfabetas, rev_alfabetas, text):
    try:
        text_ready, pre_list_char = [], []
        post_list_num = assignNum(text, userKey)
        for char in text:
            pre_list_char.append(char)
        for i in range(len(pre_list_char)):
            text_ready.append(rev_alfabetas[int(post_list_num[i])][alfabetas[0].get(pre_list_char[i])])
    except KeyError:
        print("\nFailed to encrypt your text due to unsupported characters! Supported characters as of now are:")
        import generator
        print(generator.base)
        return 0
    else:
        text_ready = "".join(text_ready)
        dottxt = open("text.txt", "w", encoding="utf-8")
        dottxt.write(text_ready)
        dottxt.close()

def decrypt(pre_list_char, pre_list_num, alfabetas, rev_alfabetas):
    text_ready = []
    for i in range(len(pre_list_char)):
        text_ready.append(rev_alfabetas[0].get(alfabetas[int(pre_list_num[i])].get(pre_list_char[i])))
    try:
        text_ready = "".join(text_ready)
        dottxt = open("text.txt", "w", encoding="utf-8")
        dottxt.write(text_ready)
        dottxt.close()
    except TypeError:
        print("\nFailed to decrypt your text due to unsupported characters! Supported characters as of now are:")
        import generator
        print(generator.base)
        return 0

def main(text, userKey, userSeed, userChoice):
    if userChoice == 1:
        from generator import generator
        alfabetas, rev_alfabetas = generator(userSeed)
        if encrypt(userKey, alfabetas, rev_alfabetas, text) == 0:
            import bilge
            bilge.main()
        else:
            print('''\nEncryption complete. Please check "text.txt"''')
            import bilge
            bilge.main()
    else:
        list_char, list_num = assign(text, userKey)
        from generator import generator
        alfabetas, rev_alfabetas = generator(userSeed)
        if decrypt(list_char, list_num, alfabetas, rev_alfabetas) == 0:
            import bilge
            bilge.main()
        else:
            print('''\nDecryption complete. Please check "text.txt"''')
            import bilge
            bilge.main()

if __name__ == '__main__':
    main()