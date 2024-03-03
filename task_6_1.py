import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання станцій метро як вершин
stations_red = ["Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська", "Шулявська", 
                "Політехнічний інститут", "Вокзальна", "Університет", "Золоті ворота<->Театральна", 
                "Хрещатик<->Майдан Незалежності", "Арсенальна", "Дніпро", "Гідропарк", "Лівобережна", 
                "Дарниця", "Чернігівська", "Лісова"]

stations_blue = ["Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка", "Контрактова площа", 
                 "Поштова площа", "Хрещатик<->Майдан Незалежності", "Палац спорту<->Площа Українських Героїв", 
                 "Олімпійська", "Палац «Україна»", "Либідська", "Деміївська", "Голосіївська", "Васильківська", 
                 "Виставковий центр", "Іподром", "Теремки"]

stations_green = ["Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота<->Театральна", 
                  "Палац спорту<->Площа Українських Героїв", "Кловська", "Печерська", "Звіринецька", 
                  "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", 
                  "Червоний хутір"]

G.add_nodes_from(stations_red)
G.add_nodes_from(stations_blue)
G.add_nodes_from(stations_green)

# Додавання з'єднань між станціями як ребер
connections_red = [(stations_red[i], stations_red[i + 1]) for i in range(len(stations_red) - 1)]
connections_blue = [(stations_blue[i], stations_blue[i + 1]) for i in range(len(stations_blue) - 1)]
connections_green = [(stations_green[i], stations_green[i + 1]) for i in range(len(stations_green) - 1)]

G.add_edges_from(connections_red)
G.add_edges_from(connections_blue)
G.add_edges_from(connections_green)

# Візуалізація графа
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # За допомогою spring_layout можна спробувати розташувати вершини більш чітко
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", font_size=10, node_size=2500)
plt.title("Граф Київського метро")
plt.show()

# Аналіз основних характеристик
print(f"Кількість станцій (вершин): {G.number_of_nodes()}")
print(f"Кількість з'єднань (ребер): {G.number_of_edges()}")
print("Ступінь кожної станції:", dict(G.degree()))
