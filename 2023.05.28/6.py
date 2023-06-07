inp1 = input('ввод1: ')
inp2 = input('ввод2: ')

if int(inp1[1]) - int(inp2[1]) > 1 or int(inp2[1]) - int(inp1[1]) > 1:
    print('нет')
else:
    print('да')
    
# ввод1: e2
# ввод2: d3
# да

# ввод1: d3
# ввод2: d5
# нет