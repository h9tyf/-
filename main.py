import time


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


def run(filename):
    global lines
    global head
    add_find = ["1.1.113.0", "1.23.228.0", "1.79.20.0", "1.253.81.0", "2.57.188.0", "2.95.91.0", "5.3.42.0", "5.34.66.0", "5.59.178.0", "5.117.128.0", "5.156.35.0", "5.177.214.0", "5.198.128.0", "6.41.128.0", "8.25.28.0", "8.44.208.0", "12.22.158.0", "12.152.104.0", "13.32.144.0", "14.21.252.0", "14.128.1.0", "14.167.0.0", "14.201.79.0", "14.233.128.0", "17.29.246.0", "18.3.106.0", "23.12.146.0", "23.45.47.0", "23.61.8.0", "23.94.200.0", "23.166.226.0", "23.207.200.0", "23.225.34.0", "23.247.73.0", "24.49.160.0", "24.78.28.0", "24.117.27.0", "24.151.128.0", "24.219.7.0", "24.254.114.0", "27.35.232.0", "27.68.120.0", "27.105.160.0", "27.126.96.0", "31.13.130.0", "31.42.94.0", "31.148.52.0", "31.186.173.0", "31.223.51.0", "36.39.148.0", "36.92.18.0", "36.157.254.0", "37.18.106.0", "37.52.152.0", "37.99.0.0", "37.131.224.0", "37.148.89.0", "37.214.4.0", "37.238.42.0", "38.65.149.0", "38.93.231.0", "38.109.1.0", "38.131.36.0", "39.134.60.0", "40.254.248.0", "41.69.32.0", "41.79.164.0", "41.129.145.0", "41.187.101.0", "41.206.8.0", "41.218.192.0", "41.242.29.0", "42.110.158.0", "42.201.157.0", "43.231.79.0", "43.246.197.0", "43.254.161.0", "45.5.248.0", "45.11.234.0", "45.43.57.0", "45.62.243.0", "45.71.120.0", "45.84.105.0", "45.92.132.0", "45.116.129.0", "45.125.210.0", "45.133.164.0", "45.141.72.0", "45.149.230.0", "45.157.214.0", "45.163.68.0", "45.167.97.0", "45.171.157.0", "45.175.240.0", "45.180.81.0", "45.184.163.0", "45.188.212.0", "45.196.112.0", "45.225.85.0", "45.229.156.0", ]
    for i in range(0, 1000):
        for s in add_find:
            bin_add = process_address(s)
            ans = find(bin_add)
    time_end = time.time()
    print(filename, ' time cost', time_end-time_start, 's')


files = ["100.txt", "1k.txt", "10k.txt", "100k.txt", "1000k.txt"]
for file_name in files:
    f = open(file_name, "r")
    lines = f.readlines()
    head = Node()
    create_tree()
    time_start = time.time()
    run(file_name)




