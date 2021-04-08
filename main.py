class Node:
    def __init__(self):
        self.next = [None, None]
        self.address = None
        self.c = None
        self.line = None


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
    c = None
    bin_address = ""
    temp = ""
    i = 0
    while i < len(s):
        if "0" <= s[i] <= "9" or s[i] == '.':
            temp += s[i]
        else:
            bin_address = process_address(temp)
            temp = ""
            break
        i += 1
    while s[i] < '0' or s[i] > '9':
        i += 1
    while i < len(s):
        if "0" <= s[i] <= "9":
            temp += s[i]
        else:
            c = int(temp)
            break
        i += 1
    return bin_address, c


def add_to_tree(address, c, line):
    global head
    cur = head
    for i in range(0, c):
        if cur.next[int(address[i])] is None:
            cur.next[int(address[i])] = Node()
        cur = cur.next[int(address[i])]
    cur.address = address
    cur.c = c
    cur.line = line


def create_tree():
    global lines
    global head
    for line in lines:
        address, c = process(line)
        add_to_tree(address, c, line)


def find(add):
    global head
    cur = head
    temp = head
    for ch in add:
        if cur.line is not None:
            temp = cur
        if cur.next[int(ch)] is None:
            break
        else:
            cur = cur.next[int(ch)]
    return temp.line


f = open("routeviews-rv2-20210301-1600.pfx2as", 'r')
# f = open("test.txt", 'r')
lines = f.readlines()
head = Node()
create_tree()

add_find = "1.2.128.0"
bin_add = process_address(add_find)
ans = find(bin_add)
if ans is None:
    print("not find!")
else:
    print(ans)




