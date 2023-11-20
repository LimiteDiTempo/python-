import random

sorted_list = []  # 합병정렬 할 때


# 선택 정렬
def selection_sort(lst):
    for i in range(len(lst)):         # 가장 작은 요소 인덱스 값 가져오기
        min_idx = i         # 가장 작은 요소 인덱스 값 가져오기
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]: # 현재 요소가 이전에 찾은 가장 작은 요소보다 작으면, 그 요소의 인덱스를 저장
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i] # 가장 작은 요소를 현재 요소와 교환
    return lst #리스트 반환


# 삽입 정렬
def insertion_sort(lst):
    for i in range(1, len(lst)): # 리스트의 첫 번째 요소부터 마지막 요소까지 순회
        key = lst[i]         # 현재 요소 저장
        j = i - 1 # 키의 이전 요소부터 시작하여, 키보다 큰 요소를 오른쪽으로 이동
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key # 키를 정렬된 위치에 삽입
    # 정렬된 리스트 반환
    return lst


# 버블 정렬
def bubble_sort(lst):
    for i in range(len(lst)):  # 리스트의 마지막 꺼 부터 첫 번째 꺼 까지 반대로 순회
        for j in range(0, len(lst) - i - 1): # 첫 번째 꺼부터 마지막에서 i 뺀거 까지 순회
            if lst[j] > lst[j + 1]:             # j(현재)가 j+1(뒤에 꺼)보다 크면 두 요소를 교환
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst            #리스트 반환


# 퀵 정렬
def quick_sort(A, left, right):
    # A: 정렬할 입력 배열
    # left: 정렬할 범위의 왼쪽 인덱스
    # right: 정렬할 범위의 오른쪽 인덱스

    if left < right:
        # 포인터 초기화
        i = left + 1
        j = right
        pivot = A[left]

        # 파티션 단계
        while i <= j:
            while i <= right and A[i] <= pivot:
                i += 1
            while j >= left and A[j] > pivot:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]

        # 피벗을 올바른 위치로 이동
        A[left], A[j] = A[j], A[left]

        # 두 파티션에 대한 재귀 호출
        quick_sort(A, left, j - 1)
        quick_sort(A, j + 1, right)


# 합병 정렬
def merge_sort(A, left, right):
    global sorted_list
    if left < right:
        mid = (left + right) // 2  # 분할
        merge_sort(A, left, mid)  # 분할
        merge_sort(A, mid + 1, right)  # 분할
        sorted_list = [0] * len(A)  # 0으로 초기화
        merge(A, left, mid, right)  # 합병


def merge(A, left, mid, right):
    i = left  # 왼쪽 리스트의 첫 번째 꺼
    j = mid + 1  # 오른쪽 리스트의 첫 번째 꺼
    k = left  # 정렬될 리스트의 첫 번째 꺼
    # 분할된 리스트의 합병
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted_list[k] = A[i]
            i, k = i + 1, k + 1
        else:
            sorted_list[k] = A[j]
            j, k = j + 1, k + 1
    # 남아있는 리스트의 복사
    while i <= mid:
        sorted_list[k] = A[i]
        i, k = i + 1, k + 1
    while j <= right:
        sorted_list[k] = A[j]
        j, k = j + 1, k + 1
    # sorted_list를 원래 리스트로 복사
    A[left: right + 1] = sorted_list[left: right + 1]


# 힙 정렬 1
def heapify(lst, n, i):
    # 가장 큰 값을 찾기 위해 현재 요소를 largest로 설정
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    # 왼쪽 자식이 존재하고 현재 요소보다 크면 왼쪽 자식 인덱스를 largest로 설정
    if l < n and lst[i] < lst[l]:
        largest = l
    # 오른쪽 자식이 존재하고 largest보다 크면 오른쪽 자식 인덱스를 largest로 설정
    if r < n and lst[largest] < lst[r]:
        largest = r
    # largest가 현재 요소의 인덱스가 아니면 largest와 현재 요소를 교환
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        # 교환 후 largest를 루트로 하는 하위 힙을 재정렬
        heapify(lst, n, largest)


# 힙정렬 2
def heap_sort(lst):
    n = len(lst)
    for i in range(n, -1, -1):     # 리스트를 최대힙 만들기
        heapify(lst, n, i)
    for i in range(n - 1, 0, -1): #뒤에서부터 순회
        lst[i], lst[0] = lst[0], lst[i]         # 현재 꺼와 루트를 교환
        heapify(lst, i, 0)  # 바꾸고 나머지 리스트 최대 힙으로 재정렬
    return lst #리스트 반환

# 메뉴
def print_option():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("****************")
    print("*1. 선택 정렬  *")
    print("*2. 삽입 정렬  *")
    print("*3. 버블 정렬  *")
    print("*4. 퀵  정렬   *")
    print("*5. 합병 정렬  *")
    print("*6. 힙 정렬    *")
    print("*7. 종료       *")
    print("****************")


# 메인 함수
def main():
    while True:
        lst = random.sample(range(101), 25)  #랜덤 숫자로 리스트 생성
        print_option()
        selectNum = input("번호를 선택하세요: ")
        if selectNum == "1":
            print("<선택 정렬>")
            print("정렬 전: ", lst)
            print("정렬 후: ", selection_sort(lst))
        elif selectNum == "2":
            print("<삽입 정렬>")
            print("정렬 전: ", lst)
            print("정렬 후: ", insertion_sort(lst))
        elif selectNum == "3":
            print("<버블 정렬>")
            print("정렬 전: ", lst)
            print("정렬 후: ", bubble_sort(lst))
        elif selectNum == "4":
            print("<퀵 정렬>")
            print("정렬 전: ", lst)
            quick_sort(lst, 0, len(lst) - 1)
            print("정렬 후: ", lst)
        elif selectNum == "5":
            print("<합병 정렬>")
            print("정렬 전: ", lst)
            merge_sort(lst, 0, len(lst) - 1)
            print("정렬 후: ", lst)
        elif selectNum == "6":
            print("<힙 정렬>")
            print("정렬 전: ", lst)
            print("정렬 후: ", heap_sort(lst))
        elif selectNum == "7":
            exit("<종료>")
        else:
            print('<번호 오류>')


if __name__ == "__main__":
    main()