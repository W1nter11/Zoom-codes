import os


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
print("--------------")


lessons = ["Илюша", "Физика", "Матеша", "Технологии", "Инглиш", "Укр.мова,літ", "Химия", "Биология", "Информатика"]
two_group_teachers = ["1. Наталия Вадимовна ","2. Ирина Олеговна ","1. Инна ","2. Лиля ","1. Татьяна Ткачова ","2. Дарья Евгеньевна "]
codes = ["856 443 7134","717 7405 4453","762 646 9234","783 6085 9503","793 1912 0930","379 853 5977","477 262 1065","560 686 4530","7381071026","4931440227","712 5230 4808","787 1770 4362"]
passwords = ["925830", "JtReP1", "441021", "K41fvD", "7tdLkB", "111", "864128", "537607", "123456", "981083", "YFqV2p", "3Ux5s9"]
teacher_of_the_lesson = ["Учитель по инглишу: ","Учитель по укр.яз/лит: ","Учитель по информатике: "]


def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)


def lessonwithoneteacher(a, b):
  if lesson == a :
    print("--------------")
    print('' + lessons[b])
  

def idntpswrdfirst(a, b):
  print("1. Скопировать идентефикатор ")
  print("2. Скопировать пароль ")
  print("--------------")
  idntpswrd0 = int(input('Что скопировать?: '))
  if idntpswrd0 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[a])
    idntpswrd0 = 0
  if idntpswrd0 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[b])
    idntpswrd0 = 0


def lessonwithtwoteachers(a, b, c, d, e, f, g, h, i):
  if lesson == a :
    print("--------------")
    print('' + lessons[b])
    print('' + two_group_teachers[c])
    print('' + two_group_teachers[d])
    print("--------------")
    teacher0 = int(input('' + teacher_of_the_lesson[e]))
  if teacher0 == 1:
    idntpswrdfirst(f, g)
  if teacher0 == 2:
    idntpswrdfirst(h, i)
  

u = 0
lesson = 0
teacher0 = 0
teacher1 = 0
teacher2 = 0
idntpswrd0 = 0


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
  




