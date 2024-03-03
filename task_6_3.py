import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

# Створення графа Київського метро з вагами для кожної лінії
G = nx.Graph()

# Червона лінія
red_line_stations = [
    "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська",
    "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет",
    "Золоті ворота<->Театральна", "Хрещатик<->Майдан Незалежності", "Арсенальна",
    "Дніпро", "Гідропарк", "Лівобережна", "Дарниця", "Чернігівська", "Лісова"
]
red_line_weight = 1.26

# Синя лінія
blue_line_stations = [
    "Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка",
    "Контрактова площа", "Поштова площа", "Хрещатик<->Майдан Незалежності",
    "Палац спорту<->Площа Українських Героїв", "Олімпійська", "Палац «Україна»",
    "Либідська", "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр",
    "Іподром", "Теремки"
]
blue_line_weight = 1.16

# Зелена лінія
green_line_stations = [
    "Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота<->Театральна",
    "Палац спорту<->Площа Українських Героїв", "Кловська", "Печерська",
    "Звіринецька", "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська",
    "Вирлиця", "Бориспільська", "Червоний хутір"
]
green_line_weight = 1.49

# Функція для додавання ребер з вагами для кожної лінії
def add_edges_with_weights(line_stations, weight):
    for i in range(len(line_stations) - 1):
        G.add_edge(line_stations[i], line_stations[i + 1], weight=weight)

# Додавання ребер для кожної лінії
add_edges_with_weights(red_line_stations, red_line_weight)
add_edges_with_weights(blue_line_stations, blue_line_weight)
add_edges_with_weights(green_line_stations, green_line_weight)

# Візуалізація графа
pos = nx.spring_layout(G, seed=420)
nx.draw(G, pos, with_labels=True, node_size=100, node_color="skyblue", font_size=8, width=1)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()


# Реалізація алгоритму Дейкстри

def dijkstra(graph, start):
    # Ініціалізація відстаней та попередників
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    previous_nodes = {vertex: None for vertex in graph.nodes}
    distances[start] = 0

    # Черга пріоритетів для зберігання вершин за відстанню
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        current_distance, current_vertex = pq.get()

        # Проходимося по сусіднім вершинам поточної вершини
        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + weight

            # Якщо знайдено коротший шлях, оновлюємо відстань та попередника
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                pq.put((distance, neighbor))

    return distances, previous_nodes

# Знаходимо найкоротші шляхи від "Академмістечко"
distances, previous_nodes = dijkstra(G, "Академмістечко")

# Показуємо відстані від "Академмістечко" до всіх інших станцій
for station, distance in distances.items():
    print(f"Відстань від Академмістечко до {station}: {distance:.2f} км")

# Приклад отримання шляху від "Академмістечко" до "Червоний хутір"
destination = "Червоний хутір"
path = []
while destination is not None:
    path.append(destination)
    destination = previous_nodes[destination]
path.reverse()

print("\nШлях від Академмістечко до Червоний хутір:")
print(" -> ".join(path))