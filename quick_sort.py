import pandas as pd

file_path = 'C:/Users/demon/Desktop/inupt_quick_sort.xlsx'

df = pd.read_excel(file_path, engine='openpyxl', header=None)

list = df.values.tolist()

# 정렬 후 pivot 반환
def split(list, first, end):
    # pivot을 위한 맨 왼쪽, 맨 오른쪽, 중간 선택
    left = list[first]
    right = list[end]
    middle = list[(first + end) // 2]

    # 정렬 후 중간값을 pivot으로 선택
    sorted_values = sorted([left, right, middle])
    pivot = sorted_values[1]

    # pivot과 맨 왼쪽 교환
    pivot_index = list.index(pivot)
    list[first], list[pivot_index] = list[pivot_index], list[first]

    # 정렬 후 왼쪽 오른쪽 분할을 위한 pivot값 반환
    while first <= end:
        while list[first] < pivot:
            first += 1
        while list[end] > pivot:
            end -= 1
        if first <= end:
            list[first], list[end] = list[end], list[first]
            first += 1
            end -= 1

    return first

# 퀵 정렬
def quick_sort(list, first, end):
    if first < end:
        # split 함수를 통해 정렬 후 pivot 반환
        pivot_index = split(list, first, end)

        # pivot을 기준으로 왼쪽, 오른쪽 부분에 대한 반복
        quick_sort(list, first, pivot_index - 1)
        quick_sort(list, pivot_index, end)

# 퀵 정렬 호출
quick_sort(list, 0, len(list) - 1)

# 결과 출력
print(list)