def assign(text, userKey="0"):
    from itertools import cycle
    cycle_it = cycle(userKey)
    list_char,list_num = [],[]
    for char in text:
        num = next(cycle_it)
        list_char.append(char)
        list_num.append(num)
    return list_char, list_num

def encrypt(pre_list_char, pre_list_num, userKey, alfabetas, rev_alfabetas, text):
    try:
        text_ready = []
        for i in range(len(pre_list_char)):
            pre_character = pre_list_char[i]
            char_code = alfabetas[0].get(pre_character)
            post_list_char, post_list_num = assign(text, userKey)
            post_number = post_list_num[i]
            post_number = int(post_number)
            post_character = rev_alfabetas[post_number][char_code]
            text_ready.append(post_character)
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
        pre_character = pre_list_char[i]
        pre_num = pre_list_num[i]
        char_code = alfabetas[int(pre_num)].get(pre_character)
        post_character = rev_alfabetas[0].get(char_code)
        text_ready.append(post_character)
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
        list_char, list_num = assign(text)
        from generator import generator
        alfabetas, rev_alfabetas = generator(userSeed)
        if encrypt(list_char, list_num, userKey, alfabetas, rev_alfabetas, text) == 0:
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