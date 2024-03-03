
# Побудова графа Київського метро по координатах 

import matplotlib.pyplot as plt
import networkx as nx

# Coordinates for the stations of each line
red_line_coords = {
    "Академмістечко": (-10, 0), "Житомирська": (-9, 0), "Святошин": (-8, 0), "Нивки": (-7, 0),
    "Берестейська": (-6, 0), "Шулявська": (-5, 0), "Політехнічний інститут": (-4, 0), "Вокзальна": (-3, 0),
    "Університет": (-2, 0), "Золоті ворота<->Театральна": (-1, 0), "Хрещатик<->Майдан Незалежності": (0, 0),
    "Арсенальна": (1, 0), "Дніпро": (2, 0), "Гідропарк": (3, 0), "Лівобережна": (4, 0),
    "Дарниця": (5, 0), "Чернігівська": (6, 0), "Лісова": (7, 0)
}

blue_line_coords = {
    "Героїв Дніпра": (0, 7), "Мінська": (0, 6), "Оболонь": (0, 5), "Почайна": (0, 4),
    "Тараса Шевченка": (0, 3), "Контрактова площа": (0, 2), "Поштова площа": (0, 1),
    "Хрещатик<->Майдан Незалежності": (0, 0), "Палац спорту<->Площа Українських Героїв": (0, -1),
    "Олімпійська": (0, -2), "Палац «Україна»": (0, -3), "Либідська": (0, -4), "Деміївська": (0, -5),
    "Голосіївська": (0, -6), "Васильківська": (0, -7), "Виставковий центр": (0, -8),
    "Іподром": (0, -9), "Теремки": (0, -10)
}

green_line_coords = {
    "Сирець": (-4, 3), "Дорогожичі": (-3, 2), "Лук'янівська": (-2, 1), "Золоті ворота<->Театральна": (-1, 0),
    "Палац спорту<->Площа Українських Героїв": (0, -1), "Кловська": (1, -2), "Печерська": (2, -3),
    "Звіринецька": (3, -4), "Видубичі": (4, -5), "Славутич": (5, -6), "Осокорки": (6, -7),
    "Позняки": (7, -8), "Харківська": (8, -9), "Вирлиця": (9, -10), "Бориспільська": (10, -11),
    "Червоний хутір": (11, -12)
}

# Combine all coordinates into a single dict for easier access
all_coords = {**red_line_coords, **blue_line_coords, **green_line_coords}

# Create a graph
G = nx.Graph()

# Add edges for each metro line
for station_list in [list(red_line_coords.keys()), list(blue_line_coords.keys()), list(green_line_coords.keys())]:
    edges = [(station_list[i], station_list[i+1]) for i in range(len(station_list)-1)]
    G.add_edges_from(edges)

# Set the position for each node based on its coordinates
pos = {station: (coords[0], coords[1]) for station, coords in all_coords.items()}

# Draw the graph with adjusted label positions
plt.figure(figsize=(25, 10))

# Draw the metro lines with specific colors
# Red line
nx.draw_networkx_edges(G, pos, edgelist=[(list(red_line_coords.keys())[i], list(red_line_coords.keys())[i+1]) for i in range(len(red_line_coords)-1)], width=2, edge_color='red')
# Blue line
nx.draw_networkx_edges(G, pos, edgelist=[(list(blue_line_coords.keys())[i], list(blue_line_coords.keys())[i+1]) for i in range(len(blue_line_coords)-1)], width=2, edge_color='blue')
# Green line
nx.draw_networkx_edges(G, pos, edgelist=[(list(green_line_coords.keys())[i], list(green_line_coords.keys())[i+1]) for i in range(len(green_line_coords)-1)], width=2, edge_color='green')

# Draw the nodes for all stations
nx.draw_networkx_nodes(G, pos, node_size=300, node_color="skyblue")

# Draw labels for each station
for station, (x, y) in pos.items():
    if station in red_line_coords:
        plt.text(x, y, station, rotation=45, ha='center', va='center', fontsize=9, fontweight='bold', color='darkred')
    elif station in blue_line_coords:
        plt.text(x, y, station, rotation=0, ha='center', va='center', fontsize=9, fontweight='bold', color='darkblue')
    elif station in green_line_coords:
        plt.text(x, y, station, rotation=0, ha='center', va='center', fontsize=9, fontweight='bold', color='darkgreen')
    else:
        plt.text(x, y + 0.1, station, fontsize=9, fontweight='bold', ha='center', va='bottom')

plt.title("Київське метро")
plt.axis("on")
plt.show()