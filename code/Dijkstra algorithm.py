import heapq
import time

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def all_pairs_shortest_path(edges):
    graph = {}
    for source, target, weight in edges:
        if source not in graph:
            graph[source] = {}
        if target not in graph:
            graph[target] = {}
        graph[source][target] = weight
        graph[target][source] = weight

    result = {}

    for vertex in graph:
        result[vertex] = dijkstra(graph, vertex)

    return result

def print_result(distances):
    vertices = sorted(distances.keys())
    print('\t' + '\t'.join(vertices))

    for i in range(len(vertices)):
        source = vertices[i]
        print(source, end='\t')
        for j in range(len(vertices)):
            target = vertices[j]
            if j > i:
                print(distances[source][target], end='\t')
            else:
                print('', end='\t')
        print()

edges = [
    ('서울', '원주', 15),
    ('서울', '천안', 12),
    ('원주', '강릉', 21),
    ('원주', '대구', 7),
    ('강릉', '포항', 25),
    ('대구', '포항', 19),
    ('대구', '부산', 9),
    ('부산', '포항', 5),
    ('천안', '논산', 4),
    ('천안', '대전', 10),
    ('논산', '대전', 3),
    ('대전', '대구', 10),
    ('논산', '광주', 13),
    ('광주', '부산', 15)
]

start_time = time.time()

result = all_pairs_shortest_path(edges)

end_time = time.time()

print_result(result)

execution_time = end_time - start_time
print(f'실행 시간: {execution_time:.6f} 초')

def floyd_warshall(edges):

    vertices = set()
    distance = {}

    for edge in edges:
        source, target, weight = edge
        vertices.add(source)
        vertices.add(target)
        distance[(source, target)] = weight
        distance[(target, source)] = weight

    for vertex in vertices:
        distance[(vertex, vertex)] = 0

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if (i, j) not in distance:
                    distance[(i, j)] = float('inf')
                if distance[(i, j)] > distance[(i, k)] + distance[(k, j)]:
                    distance[(i, j)] = distance[(i, k)] + distance[(k, j)]

    return distance

def print_result(distances):
    vertices = sorted(set(v for u, v in distances.keys()))
    print('\t' + '\t'.join(vertices))

    for i in range(len(vertices)):
        source = vertices[i]
        print(source, end='\t')
        for j in range(len(vertices)):
            target = vertices[j]
            if j > i:
                print(distances[(source, target)], end='\t')
            else:
                print('', end='\t')
        print()

edges = [
    ('서울', '원주', 15),
    ('서울', '천안', 12),
    ('원주', '강릉', 21),
    ('원주', '대구', 7),
    ('강릉', '포항', 25),
    ('대구', '포항', 19),
    ('대구', '부산', 9),
    ('부산', '포항', 5),
    ('천안', '논산', 4),
    ('천안', '대전', 10),
    ('논산', '대전', 3),
    ('대전', '대구', 10),
    ('논산', '광주', 13),
    ('광주', '부산', 15)
]

start_time = time.time()

result = floyd_warshall(edges)

end_time = time.time()

print_result(result)

execution_time = end_time - start_time
print(f'실행 시간: {execution_time:.6f} 초')

