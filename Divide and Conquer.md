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

## 퀵 정렬 (Quick Sort)
- 문제를 2개의 부분 문제로 분할
- 각 부분 문제의 크기가 일정하지 않은 형태의 divide and conquer 알고리즘
  
- Pivot 선정 방법
    - 랜덤
    - 가장 왼쪽 숫자, 중간 숫자, 가장 오른쪽 숫자 중에서 중앙값으로 pivot 결정
    - Median-of-Medians : 3 등분 후, 각 부분에서 가장 왼쪽 숫자, 중간 숫자, 가장 오른쪽 숫자 중에 중앙값을 찾은 후, 세 중앙값들 중에서 중앙값을 pivot으로 선정
          
- 특징
    - 큰 입력(n)에 대해 가장 좋은 성능(pivot)을 보임

- 시간 복잡도 : 최악의 경우: O(n^2) / 최선의 경우: O(nlogn)
    - pivot 선택에 의해 결정
    - 최악의 경우 :  (n-1)+(n-2)+(n-3)+ + 2+1 = n(n-1)/2 = O(n^2)
    - 최선의 경우
        - 각 층에서 비교 횟수 : O(n)
        - O(n) X (층수) = O(n) X logn = O(nlogn)

- 공간 복잡도 : O(n)
    - 입력을 위한 메모리 공간과 O(1) 크기의 메모리 공간만 사용

- 예제코드
```
QuickSort(A, left, right)
입력: 배열 A[left]~A[right]
출력: 정렬된 배열 A[left]~A[right]

1. if (left < right) {
2. 피봇을 A[left]~A[right]에서 선택하고, 피봇을 A[left]와 자리를 바꾼 후, 피봇과 배열의 각 원소를 비교하여 피봇보다 작은 숫자들은 A[left]~A[p-1]으로 옮기고, 피봇보다 큰 숫자들은 A[p+1]~A[right]으로 옮기며, 피봇은 A[p]에 놓는다.
3. QuickSort(A, left, p-1) // 피봇보다 작은 그룹
4. QuickSort(A, p+1, right) // 피봇보다 큰 그룹
}
```
## 선택 (Selection) 문제
- 전체 n개의 숫자들 중에서 k 번째로 작은 숫자를 찾는 문제(정렬X)
    - 퀵 정렬에서 선택 받지 못한 부분은 버림
    - 선택(Selection) 문제는 divide and conquer 알고리즘이기도 하고 랜덤(random) 알고리즘 이기도 함(pivot 랜덤)

- Good/bad 분할 정의
    - 분할된 두 그룹 중의 하나의 크기가 입력 크기의 ¾과 같거나 그 보다 크면 나쁜 (bad) 분할이라고 정의

 - 시간복잡도 : O(n)
     - n + 3n/4 + (3/4)2n + (3/4)3n + … +(3/4)i-1n+(3/4)in 
= n[1 + 3/4 + (3/4)2 + (3/4)3 + …+ (3/4)i-1 + (3/4)i]≤ 4n = O(n)

- 선택 알고리즘과 이진 탐색 비교
    - 이진탐색 : 정렬된 입력의 중간에 있는 숫자와 찾고자 하는 숫자를 비교함으로써, 입력을 1/2로 나눈 두 부분에서 한 부분만 검색
    - 유사성
        - 이진 탐색은 분할 과정을 진행하면서 범위를 ½씩 좁혀가며 찾고자 하는 숫자를 탐색
        - 선택 알고리즘은 pivot으로 분할하여 범위를 좁혀감
    - 공통점
        - 부분 문제들을 취합하는 과정이 별도로 필요 없음
- 예제코드
  ```
    Selection(A, left, right, k)
    input: A[left]~A[right]와 k, 단, 1≤k≤|A|, |A|=right-left+1
    output: A[left]~A[right]에서 k번째 작은 원소
    
    1. pivot을 A[left]~A[right]에서 랜덤하게 선택하고, pivot과 A[left]의 자리를 바꾼 후, pivot과 배열의 각 원소를 비교하여 pivot 보다 작은 숫자는 A[left]~A[p-1]로 옮기고, pivot 보다 큰 숫자는 A[p+1]~A[right]로 옮기며, pivot은 A[p]에 놓음
    2. S = (p-1)-left+1 // S = Small group의 크기
    3. If (k ≤ S) Selection(A, left, p-1, k) // Small group에서 찾기
    4. else if (k = S + 1) return A[p] // pivot = k번째 작은 숫자
    5. else Selection(A, p+1, right, k-S-1) // Large group에서 찾기
  ```
## 최근접 점의 쌍 찾기
- 2차원 평면상의 n개의 점이 입력으로 주어질 때, 거리가 가장 가까운 한 쌍의 점을 찾는 문제

- 간단한 방법
    - 모든 점에 대하여 각각의 두 점 사이의 거리를 계산하여 가장 가까운 점의 쌍을 찾음 > 시간복잡도 : O(n^2)
- 효율적 방법
    - n개의 점을 1/2로 분할하여 각각의 부분 문제에서 최근접 점의 쌍을 찾고, 2개의 부분 해 중에서 짧은 거리를 가진 점의 쌍을 일단 찾음
 
- 중간 영역 찾는 방법
    - 중간 값 전의 최소 값을 왼쪽, 오른쪽 부분에 각각 더하고 뺀 값을 포함시킴

- 시간 복잡도 : O(n(logn)^2)
  
- 복잡도 줄이는 방법
      - y-좌표에 대한 정렬을 전처리 과정에서 한번만 진행 > 시간 복잡도 : O(nlogn)

```
ClosestPair(S)
입력: x 좌표의 오름차순으로 정렬된 배열 S에 있는 i개의 점 (단, 각 점은 (x,y)로 표현)
출력: S에 있는 점들 중 최근접 점의 쌍의 거리

1. if(i<=3) return (2 or 3개의 점들 사이의 최근접 쌍)
2. 정렬된 S를 같은 크기의 S_L과 S_R로 분할. |S|가 홀수이면 |S_L| = |S_R|+1이 되도록 분할
3. CP_L = ClosestPair(S_L) // CP_L은 S_L에서의 최근접 점의 쌍
4. CP_R = ClosestPair(S_R) // CP_R은 S_R에서의 최근접 점의 쌍
5. d = min(dist(CP_L), dist(CP_R))일 때, 중간 영역에 속하는 점들 중에서 최근접 점의 쌍을 찾아서 이를 CP_C라고 하자. 단, dist()는 두 점 사이의 거리
6. return (CP_L, CP_C, CP_R 중에서 거리가 가장 짧은 쌍)
```
