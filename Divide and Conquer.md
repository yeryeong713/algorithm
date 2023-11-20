# 분할 정복 알고리즘 (Divide and Conquer)
주어진 문제의 입력을 분할하여(divide) 문제를 해결(정복, conquer)하는 방식의 알고리즘

## 합병 정렬 (Merge Sort)
- 입력이 2개인 부분 문제로 분할
- 부분 문제의 크기가 ½로 감소하는 divide and conquer 알고리즘
- 합병 과정이 문제를 정복하는 과정

- 시간 복잡도 : O(nlogn)
    - (층수) X O(n) = log2n X O(n) = O(nlogn)
    - 분할 과정 : O(1) / 합병 과정: O(m+n)
    - 합병은 입력 크기에 비례하므로 각 층에서의 비교 횟수는 O(n)
    - 층의 최대 개수 : 2^k = n >  k = log2n

- 공간 복잡도 : O(n)
    - 입력을 위한 메모리 공간과 O(1) 크기의 메모리 공간만 사용

- 예제코드
```
MergeSort(A,p,q)
입력: A[p]~A[q]
출력: 정렬된 A[p]~A[q]

1. if (p < q) { // 배열의 원소의 수가 2개 이상이면
2. k = floor((p+q)/2) // k는 중간 원소의 인덱스
3. MergeSort(A,p,k) // 앞부분 순환 호출
4. MergeSort(A,k+1,q) // 뒷부분 순환 호출
5. A[p]~A[k]와 A[k+1]~A[q]를 합병
}

# floor(a) : a보다 작은 가장 큰 정수
```
