color_value = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
color_multi = {
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 1000,
    'yellow': 10000,
    'green': 100000,
    'blue': 1000000,
    'violet': 10000000,
    'grey': 100000000,
    'white': 1000000000
}

color_lst = [input() for _ in range(3)]

color1 = color_value.index(color_lst[0])
color2 = color_value.index(color_lst[1])
color3 = color_multi[color_lst[2]]

print((color1*10 + color2)*color3)

