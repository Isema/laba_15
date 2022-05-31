'''
работа 19
'''
import pandas as pd
import matplotlib.pyplot as plt
df3=[0.0]*891
konec={"k","m"}
df = pd.read_csv('../coursera_data.csv')#Ввод из scv файла
#Убираем к и m из списка(тысчи и миллионы) и вставляем 000 у к и 000000 у m
gate=df['course_students_enrolled']
n=len(df['course_students_enrolled'])
for i in range(n):
    gate[i]=gate[i].replace("k", "")+'000'
    gate[i]=gate[i].replace("m", "")+'000000'
#Преобразуем в gloat
for i in range(n):
    df3[i]=float(gate[i])
#Добавляем столбец 'students' В файл
df['students']=df3
#Группировка по course_difficulty(создаём отдел.таблицу) и добавляем сумму зач.студентов
df1=df.groupby('course_difficulty')['students'].sum().sort_values(ascending=True)
print(df1)
# Составляем диаграмму
plt.plot(df1)
# Выводим диаграмму
plt.show()
#Группировка по course_difficulty(создаём отдел.таблицу) и сред.значение рейтинга по группе
df2=df.groupby('course_difficulty')['course_rating'].mean().sort_values(ascending=True)
print(df2)
plt.plot(df2)
plt.show()
