def generator(userSeed):
    import random
    alfabetas, rev_alfabetas = [], []
    base = '''\n !"#%&'()*+,-./0123456789:;<=>?@ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ[]^_`abcçdefgğhıijklmnoöpqrsştuüvwxyz{|}~'''
    list_char = list(base)
    dict_alfabeta = {key: item for item, key in enumerate(list_char)}
    alfabetas.append(dict_alfabeta)
    rev_dict_alfabeta = {key: item for item, key in dict_alfabeta.items()}
    rev_alfabetas.append(rev_dict_alfabeta)
    for i in range(9):
        seedset = random.Random(int(userSeed)+i)
        seedset.shuffle(list_char)
        dict_alfabeta = {key: item for item, key in enumerate(list_char)}
        alfabetas.append(dict_alfabeta)
        rev_dict_alfabeta = {key: item for item, key in dict_alfabeta.items()}
        rev_alfabetas.append(rev_dict_alfabeta)
    alfabetas, rev_alfabetas = tuple(alfabetas), tuple(rev_alfabetas)
    return alfabetas, rev_alfabetas

def main():
    pass

if __name__ == '__main__':
    main()