def is_binary_anagram(x,y):
    binary_x = bin(x)
    binary_y = bin(y)
    print(binary_x)
    print(binary_y)
    x_zeros = binary_x.count("0")
    x_ones = binary_x.count("1")
    y_zeros = binary_y.count("0")
    y_ones = binary_y.count("1")

    if (x_zeros == y_zeros and x_ones == y_ones):
        print("%i and %i are binary anagrams!" % (x,y))
        return "true"
    else:
        print("%i and %i are not binary anagrams." % (x,y))
        return "false"
