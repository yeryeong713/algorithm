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

        # 맨 앞 숫자와 중간 숫자(vertex a 와 vertex b)를 오름차순으로 정렬
        numbers_list[0], numbers_list[1] = min(numbers_list[0], numbers_list[1]), max(numbers_list[0], numbers_list[1])

        # 리스트를 튜플로 변환하여 추가
        new_tuple = tuple(numbers_list)
        numbers.append(new_tuple)
    else:
        print("다시 입력하기")

# () 안의 마지막 숫자(가중치)를 기준으로 정렬
numbers.sort(key=lambda x: (x[-1], x[0]))

# 부모 노드
parent = {}

# 루트 노드를 찾는 함수
def find_root(node):
    if parent[node] != node:
        parent[node] = find_root(parent[node])
    return parent[node]

# 두 개의 노드를 연결하는 함수
def line(node1, node2):
    root1 = find_root(node1)
    root2 = find_root(node2)
    parent[root2] = root1

# 최소 신장 트리를 저장할 리스트
minimum_spanning_tree = []

# Kruskal 알고리즘 수행
for tpl in numbers:
    node1, node2, weight = tpl
    if node1 not in parent:
        parent[node1] = node1
    if node2 not in parent:
        parent[node2] = node2

    if find_root(node1) != find_root(node2):
        line(node1, node2)
        minimum_spanning_tree.append(tpl)

# 결과 출력
print("결과:")
for i, tpl in enumerate(minimum_spanning_tree):
    print(f"{tpl}")
