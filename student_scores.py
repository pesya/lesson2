#Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.
import numpy as np


assessments = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '4b', 'scores': [5,4,5,2]},
                {'school_class': '4c', 'scores': [2,3,5,5,2,4,3]},
                {'school_class': '4d', 'scores': [3,4,3,5,5]}]


all_scores = []
count_all = 0
sum_all = 0
for i in assessments:
    class_number = i.get('school_class')
    class_scores = i.get('scores')
    all_scores.append(class_scores)
    class_scores = np.mean(class_scores)
    print('Class', class_number, 'avg score is', class_scores)
for j in all_scores:
    count_all = count_all + len(j)
    sum_all = sum_all+ sum(j)
print('School avg score is', sum_all/count_all)
