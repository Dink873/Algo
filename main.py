from collections import defaultdict, deque

def topological_sort(graph):
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result

def optimal_order(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    graph = defaultdict(list)

    for line in lines:
        tokens = line.strip().split()
        current_doc, required_doc = tokens[0], tokens[1]
        graph[required_doc].append(current_doc)

    ordered_docs = topological_sort(graph)

    with open(output_file, 'w') as out_file:
        for doc in ordered_docs:
            out_file.write(f'{doc}\n')

# Виклик функції для прикладу 1
optimal_order('../govern.in', 'govern.out')
