inp1 = input('ввод1: ')
inp2 = input('ввод2: ')

if (ord(inp1[0]) + int(inp1[1])) % 2 == (ord(inp2[0]) + int(inp2[1])) % 2:
    print('да')
else:
    print('нет')
    
# ввод1: a3
# ввод2: b4
# да

# ввод1: a3
# ввод2: b3
# нет