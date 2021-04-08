def process(s):
    temp = s.split(" ")
    address = None
    c = None
    for i in temp:
        if i != "" and address is None:
            address = i
        elif i != "" and address is not None:
            c = i
            break
    temp = address.split(".")
    bin_add = ""
    for num in temp:
        bin_add += '{:08b}'.format(int(num))
    return bin_add, c


s = "1.3.0.255   24 12345"
a, b = process(s)
print(a)
print(b)
