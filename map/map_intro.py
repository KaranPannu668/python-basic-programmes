import timeit
text = "what have the romans ever done for us"


def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


# Use map
def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals

def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words


# Use map
def map_words():
    map_w = list(map(str.upper, text.split(' ')))
    return map_w


if __name__ == '__main__':
    print(comp_caps())
    print(map_caps())
    print(map_words())
    print(map_words())
    # print(timeit.timeit("comp_caps()", setup="from map_intro import comp_caps", number=10000))
    print(timeit.timeit(comp_caps, number=10000))
    print(timeit.timeit(map_caps, number=10000))
    print(timeit.timeit(comp_words, number=10000))
    print(timeit.timeit(map_words, number=10000))