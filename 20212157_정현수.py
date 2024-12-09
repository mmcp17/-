
# coding: utf-8

# In[2]:


import random
import string

def generate_student_data(num_students=30):
    students = []
    for _ in range(num_students):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))  # 두 글자 이름
        age = random.randint(18, 22)  # 나이 18~22
        score = random.randint(0, 100)  # 성적 0~100
        students.append({"이름": name, "나이": age, "성적": score})
    return students
# 선택 정렬
def selection_sort(students, key, reverse=False):
    n = len(students)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if (students[j][key] < students[min_index][key]) != reverse:
                min_index = j
        students[i], students[min_index] = students[min_index], students[i]

# 삽입 정렬
def insertion_sort(students, key, reverse=False):
    for i in range(1, len(students)):
        key_student = students[i]
        j = i - 1
        while j >= 0 and (key_student[key] < students[j][key]) != reverse:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_student

# 퀵 정렬
def quick_sort(students, key, reverse=False):
    if len(students) <= 1:
        return students
    pivot = students[len(students) // 2]
    left = [x for x in students if (x[key] < pivot[key]) != reverse]
    middle = [x for x in students if x[key] == pivot[key]]
    right = [x for x in students if (x[key] > pivot[key]) != reverse]
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)

# 기수 정렬
def counting_sort(students, key):
    max_score = max(student[key] for student in students)
    count = [0] * (max_score + 1)
    output = [None] * len(students)

    for student in students:
        count[student[key]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for student in reversed(students):
        output[count[student[key]] - 1] = student
        count[student[key]] -= 1
    return output
def display_students(students):
    for student in students:
        print(student)

def main():
    students = generate_student_data()
    print("생성된 학생 정보:")
    display_students(students)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
        choice = input("선택하세요: ")

        if choice == '4':
            break

        key_map = {'1': '이름', '2': '나이', '3': '성적'}
        key = key_map.get(choice)
        if key is None:
            print("잘못된 선택입니다.")
            continue

        sort_choice = input("정렬 알고리즘 선택 (1: 선택 정렬, 2: 삽입 정렬, 3: 퀵 정렬, 4: 기수 정렬): ")
        if sort_choice == '1':
            selection_sort(students, key)
        elif sort_choice == '2':
            insertion_sort(students, key)
        elif sort_choice == '3':
            students = quick_sort(students, key)
        elif sort_choice == '4' and key == '성적':
            students = counting_sort(students, key)
        else:
            print("잘못된 선택입니다.")
            continue

        print("정렬된 학생 정보:")
        display_students(students)

if __name__ == "__main__":
    main()

