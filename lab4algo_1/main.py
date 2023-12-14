from collections import deque

def min_depth(adj_list, root):
    # Ініціалізуємо чергу з кореневим вузлом та його глибиною
    queue = deque([(root, 1)])
    # Ініціалізуємо множину для відстеження відвіданих вузлів
    visited = set()

    # Продовжуємо цикл, доки черга не стане порожньою
    while queue:
        # Вибираємо лівий вузол та його глибину з черги
        node, depth = queue.popleft()
        # Позначаємо вузол як відвіданий
        visited.add(node)

        # Отримуємо сусідів поточного вузла зі списку суміжності
        neighbors = adj_list.get(node, [])
        # Припускаємо, що поточний вузол є листом
        is_leaf = True

        # Проходимо сусідів поточного вузла
        for neighbor in neighbors:
            # Якщо сусід не був відвіданий, додаємо його в чергу зі збільшеною глибиною
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))
                # Поточний вузол не є листом, оскільки у нього є невідвіданий сусід
                is_leaf = False

        # Якщо поточний вузол є листом, повертаємо його глибину
        if is_leaf:
            return depth

    # Повертаємо глибину останнього обробленого вузла (корінь, якщо граф є одним вузлом)
    return depth

# Ініціалізуємо порожній список суміжності
adj_list = {}

# Зчитуємо вхідні дані з файлу з ім'ям 'input.txt'
with open('input.txt', 'r') as file:
    # Зчитуємо перший рядок для отримання кореневого вузла
    lines = file.readlines()
    root = int(lines[0].strip())

    # Обробляємо решту рядків для побудови списку суміжності
    for line in lines[1:]:
        src, dest = map(int, line.strip().split(','))
        if src not in adj_list:
            adj_list[src] = []
        adj_list[src].append(dest)

# Викликаємо функцію min_depth для знаходження мінімальної глибини дерева
result = min_depth(adj_list, root)

# Записуємо результат у вихідний файл з ім'ям 'output.txt'
with open('output.txt', 'w') as output_file:
    output_file.write(f'Мінімальна глибина: {result}')

# Виводимо результат на консоль
print(f'Мінімальна глибина дерева: {result}')
