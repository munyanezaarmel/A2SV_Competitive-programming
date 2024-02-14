
students=[]
for _ in range(int(input())):
  name = input()
  score = float(input())
  students.append([name,score])
scores=[]
final=[]
for student in range(len(students)):
   scores.append(students[student][1])
print(scores)
new_score=set(scores)
new_score2=sorted(list(new_score))
print(new_score2)
for i in range(len(students)):
    if students[i][1]==new_score2[1]:
       final.append(students[i][0])
print("\n".join(sorted(final)))

