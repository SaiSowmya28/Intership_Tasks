# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    score=sorted(set(student[1] for student in students))
    second_lowest=score[1]
    names=[student[0] for student in students if student[1]==second_lowest]
    for i  in sorted(names):
        print(i)
