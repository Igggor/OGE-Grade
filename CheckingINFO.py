from time import sleep

from MyGradre import Check_my_grade
Grade = "н/д"
while Grade == "н/д":
    Grade = Check_my_grade()
    print(Grade)
    sleep(10)
print(Grade)
