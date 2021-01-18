import os
import webbrowser


os.startfile(r'C:\Users\User\AppData\Roaming\Zoom\bin\Zoom.exe')


print("Предмет")
print("--------")
print("1. Илюша")
print("2. Физика")
print("3. Матеша")
print("4. Технологии")
print("5. Инглиш")
print("6. Укр.мова,літ")
print("7. Химия") 
print("8. Биология")
print("9. Информатика")
print("10. LSE")
print("--------------")

s="https://us04web.zoom.us/j/code?#success"
lessons = ["Илюша", "Физика", "Матеша", "Технологии", "Инглиш", "Укр.мова,літ", "Химия", "Биология", "Информатика","LSE"]
two_group_teachers = ["1. Наталия Вадимовна ","2. Ирина Олеговна ","1. Инна ","2. Лиля ","1. Татьяна Ткачова ","2. Дарья Евгеньевна "]
codes = ["8564437134","71774054453","7626469234","78360859503","79319120930","3798535977","4772621065","5606864530","7381071026","4931440227","71252304808","78717704362","96589277755"]
passwords = ["925830", "JtReP1", "441021", "K41fvD", "7tdLkB", "111", "864128", "537607", "123456", "981083", "YFqV2p", "3Ux5s9","Без пароля"]
teacher_of_the_lesson = ["Учитель по инглишу: ","Учитель по укр.яз/лит: ","Учитель по информатике: "]


def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)


def lessonwithoneteacher(l_number, l_name):
  if lesson == l_number :
    print("--------------")
    print('' + lessons[l_name])
  

def idntpswrdfirst(l_code, l_password):
  pswrd0 = 0
  print("--------------")
  print('1. Да ')
  print('2. Нет ')
  idnt0 = int(input('Открыть ссылку на конференцию?: '))
  if idnt0 == 1 : 
    s1=s.replace("code", codes[l_code] )
    webbrowser.open(s1, new=2)
    idnt0 = 0
    print("--------------")
    print('Пароль скопирован в буфер обмена ')
    print("--------------")
    addToClipBoard('' + passwords[l_password])
  else:
    lesson = 0


def lessonwithtwoteachers(l_number, l_name, t_first, t_sec, l_teacher, l_code1, l_password1, l_code2, l_password2):
  if lesson == l_number :
    print("--------------")
    print('' + lessons[l_name])
    print('' + two_group_teachers[t_first])
    print('' + two_group_teachers[t_sec])
    print("--------------")
    teacher0 = int(input('' + teacher_of_the_lesson[l_teacher]))
  if teacher0 == 1:
    idntpswrdfirst(l_code1, l_password1)
  if teacher0 == 2:
    idntpswrdfirst(l_code2, l_password2)
  

u = 0
lesson = 0
teacher0 = 0


while u == 0:
  lesson = int(input('Номер урока: '))
  if lesson == 1 :
    lessonwithoneteacher(1, 0)
    idntpswrdfirst(0, 0)
  if lesson == 2 :
    lessonwithoneteacher(2, 1)
    idntpswrdfirst(1, 1)
  if lesson == 3 :
    lessonwithoneteacher(3, 2)
    idntpswrdfirst(2, 2)
  if lesson == 4 :
    lessonwithoneteacher(4, 3)
    idntpswrdfirst(3, 3)
  if lesson == 5 :
    lessonwithtwoteachers(5, 4, 0, 1, 0, 4, 4, 5, 5)
  if lesson == 6 :
    lessonwithtwoteachers(6, 5, 2, 3, 1, 6, 6, 7, 7)
  if lesson == 7 :
    lessonwithoneteacher(7, 6)
    idntpswrdfirst(8, 8)
  if lesson == 8 :
    lessonwithoneteacher(8, 7)
    idntpswrdfirst(9, 9)
  if lesson == 9 :
    lessonwithtwoteachers(9, 8, 4, 5, 2, 10, 10, 11, 11)
  if lesson == 10:
    lessonwithoneteacher(10, 9)
    idntpswrdfirst(12, 12)
  if lesson == 0:
    lesson = int(input('Номер урока: '))