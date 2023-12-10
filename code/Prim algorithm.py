# 빈 리스트 생성
numbers = []

# 10번 반복하여 입력 받기
for i in range(10):
    # 사용자로부터 입력 받기
    user_input = input(f"{i+1}번: ")

    # 입력이 괄호로 시작하고 끝나는지 확인
    if user_input.startswith('(') and user_input.endswith(')'):
        # 괄호를 제외하고 내부의 문자열을 가져옴
        content = user_input[1:-1]

        # 쉼표를 기준으로 분리하고 정수로 변환하여 리스트로 만듦
        numbers_list = [int(x) for x in content.split(',')]

        # 리스트를 튜플로 변환하여 추가
        new_tuple = tuple(numbers_list)
        numbers.append(new_tuple)
    else:
        print("다시 입력하기")

# 그래프
graph = {}

# 그래프 구성
for tpl in numbers:
    node1, node2, weight = tpl

    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []

    graph[node1].append((node2, weight))
    graph[node2].append((node1, weight))

# Prim 알고리즘 수행
visited = set()
start_node = list(graph.keys())[0]  # 임의의 시작 노드 선택 (0번째)
visited.add(start_node)
minimum_spanning_tree = []

while len(visited) < len(graph):
    min_edge = None

    for node in visited:
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                if min_edge is None or weight < min_edge[2]:
                    min_edge = (node, neighbor, weight)

    node1, node2, weight = min_edge
    minimum_spanning_tree.append((node1, node2, weight))
    visited.add(node2)

# 결과 출력
print("결과:")
for i, tpl in enumerate(minimum_spanning_tree):
    print(f"{tpl}")
