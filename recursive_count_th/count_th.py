'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    if word == "":
        return count
    letterlist = list(word)
    print('letterlist', letterlist)
    nlist = letterlist[:2]
    twolet = "".join(nlist)
    print('twolet', twolet)
    if twolet == 'th':
        count +=1
        del letterlist[0]
        count_th("".join(letterlist))
    elif twolet != 'th':
        del letterlist[0]
        count_th("".join(letterlist))
    return count
    


print(count_th("thhtthht"))


def count_th(word):
    count = 0
    if word == "":
        return count
    letterlist = list(word)
    print('letterlist', letterlist)
    nlist = letterlist[:2]
    twolet = "".join(nlist)
    print('twolet, lentwolet', twolet, len(two))
    if len(twolet) > 1:
        if twolet == 'th':
            count +=1
            del letterlist[0]
            count_th("".join(letterlist))
        elif twolet != 'th':
            del letterlist[0]
            count_th("".join(letterlist))
    else:
        return count
