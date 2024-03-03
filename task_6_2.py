import networkx as nx

# Створення та налаштування графа
G = nx.Graph()

# Додавання з'єднань для Київського метро
G.add_edges_from([
    # Червона лінія
    ("Академмістечко", "Житомирська"), ("Житомирська", "Святошин"), ("Святошин", "Нивки"),
    ("Нивки", "Берестейська"), ("Берестейська", "Шулявська"), ("Шулявська", "Політехнічний інститут"),
    ("Політехнічний інститут", "Вокзальна"), ("Вокзальна", "Університет"), ("Університет", "Золоті ворота<->Театральна"),
    ("Золоті ворота<->Театральна", "Хрещатик<->Майдан Незалежності"), ("Хрещатик<->Майдан Незалежності", "Арсенальна"),
    ("Арсенальна", "Дніпро"), ("Дніпро", "Гідропарк"), ("Гідропарк", "Лівобережна"),
    ("Лівобережна", "Дарниця"), ("Дарниця", "Чернігівська"), ("Чернігівська", "Лісова"),
    # Синя лінія
    ("Героїв Дніпра", "Мінська"), ("Мінська", "Оболонь"), ("Оболонь", "Почайна"),
    ("Почайна", "Тараса Шевченка"), ("Тараса Шевченка", "Контрактова площа"), ("Контрактова площа", "Поштова площа"),
    ("Поштова площа", "Хрещатик<->Майдан Незалежності"), ("Хрещатик<->Майдан Незалежності", "Палац спорту<->Площа Українських Героїв"),
    ("Палац спорту<->Площа Українських Героїв", "Олімпійська"), ("Олімпійська", "Палац «Україна»"),
    ("Палац «Україна»", "Либідська"), ("Либідська", "Деміївська"), ("Деміївська", "Голосіївська"),
    ("Голосіївська", "Васильківська"), ("Васильківська", "Виставковий центр"), ("Виставковий центр", "Іподром"),
    ("Іподром", "Теремки"),
    # Зелена лінія
    ("Сирець", "Дорогожичі"), ("Дорогожичі", "Лук'янівська"), ("Лук'янівська", "Золоті ворота<->Театральна"),
    ("Золоті ворота<->Театральна", "Палац спорту<->Площа Українських Героїв"), ("Палац спорту<->Площа Українських Героїв", "Кловська"),
    ("Кловська", "Печерська"), ("Печерська", "Звіринецька"), ("Звіринецька", "Видубичі"),
    ("Видубичі", "Славутич"), ("Славутич", "Осокорки"), ("Осокорки", "Позняки"),
    ("Позняки", "Харківська"), ("Харківська", "Вирлиця"), ("Вирлиця", "Бориспільська"),
    ("Бориспільська", "Червоний хутір")
])

def dfs(graph, start, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    if parent:
        path.append((parent, start))
    for next_node in graph.neighbors(start):
        if next_node not in visited:
            dfs(graph, next_node, visited, path, start)
    return path

def bfs(graph, start):
    visited, queue = set([start]), [start]
    path = []
    
    while queue:
        vertex = queue.pop(0)
        for neighbour in graph.neighbors(vertex):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))
    return path

# Виконання DFS та BFS
dfs_path = dfs(G, "Академмістечко")
bfs_path = bfs(G, "Академмістечко")

print(f"DFS path: {dfs_path}")
print(f"BFS path: {bfs_path}")
