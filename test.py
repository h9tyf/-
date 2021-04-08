def process_address(s):
    bin_address = ""
    temp = ""
    i = 0
    while i < len(s):
        if "0" <= s[i] <= "9":
            temp += s[i]
        elif s[i] == '.':
            bin_address += '{:08b}'.format(int(temp))
            temp = ""
        i += 1
    bin_address += '{:08b}'.format(int(temp))
    return bin_address


def process(s):
    bin_address = ""
    temp = ""
    i = 0
    while i < len(s):
        if "0" <= s[i] <= "9" or s[i] == '.':
            temp += s[i]
        else:
            return temp
        i += 1


f = open("1000k.txt", "r")
fo = open("test111.txt", "w")
lines = f.readlines()
fo.write("[")
i = 0
count = 0
for line in lines:
    if i % 1000 == 79 and count < 100:
        fo.write("\"" + process(line) + "\", ")
        count += 1
    i += 1
fo.write("]\n")
fo.close()
f.close()