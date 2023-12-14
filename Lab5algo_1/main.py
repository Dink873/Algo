from collections import defaultdict

def topological_sort_dfs(graph):
    # Ініціалізація множини відвіданих вершин та списку для зберігання впорядкованої послідовності
    visited = set()
    result = []

    def dfs(node):
        # Додаємо поточний вузол до відвіданих
        visited.add(node)
        # Рекурсивно викликаємо dfs для сусідів поточного вузла
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        # Додаємо поточний вузол до результату після відвідування всіх сусідів
        result.append(node)

    # Копіюємо словник для ітерації
    for node in list(graph):
        # Якщо вершина ще не була відвідана, викликаємо dfs для неї
        if node not in visited:
            dfs(node)

    return result

def optimal_order(input_file, output_file):
    # Зчитуємо вміст вхідного файлу
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Ініціалізуємо словник суміжності для зберігання графу документів
    graph = defaultdict(list)

    # Заповнюємо граф із вхідних даних
    for line in lines:
        tokens = line.strip().split()
        current_doc, required_doc = tokens[0], tokens[1]
        # Додаємо ребро в граф: required_doc -> current_doc
        graph[required_doc].append(current_doc)

    # Викликаємо функцію топологічного сорту для отримання оптимального порядку документів
    ordered_docs = topological_sort_dfs(graph)

    # Записуємо результат у вихідний файл
    with open(output_file, 'w') as out_file:
        for doc in ordered_docs:
            out_file.write(f'{doc}\n')

# Приклад виклику функції для ілюстрації
optimal_order('../govern.in', 'govern.out')
