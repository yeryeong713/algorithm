def heap_sort(A):
    n = len(A)

    def build_heap():
        nonlocal n
        for i in range(n // 2, 0, -1):
            down_heap(i)

    def down_heap(i):
        nonlocal n
        left = 2 * i
        right= 2 * i + 1
        bigger = i

        if left <= n and A[left - 1] > A[i - 1]:
            bigger = left

        if right <= n and A[right - 1] > A[bigger - 1]:
            bigger = right

        if bigger != i:
            A[i - 1], A[bigger - 1] = A[bigger - 1], A[i - 1]
            down_heap(bigger)

    def heap_sort_process():
        nonlocal n
        build_heap()
        for i in range(n - 1, 0, -1):
            A[i], A[0] = A[0], A[i]
            n -= 1
            down_heap(1)

    heap_sort_process()

with open("input.txt", "r") as input_file:
    unsort = [int(line.strip()) for line in input_file]

heap_sort(unsort)

with open("output.txt", "w") as output_file:
    for number in unsort:
        output_file.write(str(number) + "\n")