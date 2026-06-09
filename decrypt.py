def assign(text, userKey):
    from itertools import cycle
    cycle_it = cycle(userKey)
    list_char,list_num = [],[]
    for char in text:
        num = next(cycle_it)
        list_char.append(char)
        list_num.append(num)
    return list_char, list_num

def decrypt(pre_list_char, pre_list_num, alfabetas, rev_alfabetas):
    text_ready = []
    for i in range(len(pre_list_char)):
        pre_character = pre_list_char[i]
        pre_num = pre_list_num[i]
        char_code = alfabetas[int(pre_num)].get(pre_character)
        post_character = rev_alfabetas[0].get(char_code)
        text_ready.append(post_character)
    text_ready = "".join(text_ready)
    dottxt = open("text.txt", "w")
    dottxt.write(text_ready)
    dottxt.close()

def main(text, userKey, userSeed):
    list_char, list_num = assign(text, userKey)
    from generator import generator
    alfabetas, rev_alfabetas = generator(userSeed)
    decrypt(list_char, list_num, alfabetas, rev_alfabetas)
    print('''\nDecryption complete. Please check "text.txt"''')
    import bilge
    bilge.main()

if __name__ == '__main__':
    main()