from time import sleep

from MyGradre import Check_my_grade
Grade = "н/д"
while Grade == "н/д":
    Grade = Check_my_grade()
    print(Grade)
    sleep(10) #в функцию sleep установите время ожидания перед слдедующей проверкой в секундах. Лично я рекомендую 5 минут sleep(300)
print(Grade)
