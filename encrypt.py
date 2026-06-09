userText = ""
def pre_assign(text, userKey=0):
    from itertools import cycle
    cycle_it = cycle(str(userKey))
    list_char,list_num = [],[]
    for char in text:
        num = next(cycle_it)
        list_char.append(char)
        list_num.append(num)
    return list_char, list_num

def assign(text, userKey):
    from itertools import cycle
    cycle_it = cycle(userKey)
    list_char,list_num = [],[]
    for char in text:
        num = next(cycle_it)
        list_char.append(char)
        list_num.append(num)
    return list_char, list_num

def encrypt(pre_list_char, pre_list_num, userKey, alfabetas, rev_alfabetas):
    text_ready = []
    for i in range(len(pre_list_char)):
        pre_character = pre_list_char[i]
        char_code = alfabetas[0].get(pre_character)
        post_list_char, post_list_num = assign(userText, userKey)
        post_number = post_list_num[i]
        post_number = int(post_number)
        post_character = rev_alfabetas[post_number][char_code]
        text_ready.append(post_character)
    text_ready = "".join(text_ready)
    dottxt = open("text.txt", "w")
    dottxt.write(text_ready)
    dottxt.close()

def main(text, userKey, userSeed):
    global userText
    userText = text
    list_char, list_num = pre_assign(text)
    from generator import generator
    alfabetas, rev_alfabetas = generator(userSeed)
    encrypt(list_char, list_num, userKey, alfabetas, rev_alfabetas)
    print('''\nEncryption complete. Please check "text.txt"''')
    import bilge
    bilge.main()

if __name__ == '__main__':
    main()