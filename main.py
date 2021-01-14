teacher0 = 0
teacher1 = 0
teacher2 = 0
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

codes = ["Ідентифікатор: 856 443 7134","Ідентифікатор: 717 7405 4453","Ідентифікатор: 762 646 9234","Ідентифікатор: 783 6085 9503","Ідентифікатор: 793 1912 0930","Ідентифікатор: 379 853 5977","Ідентифікатор: 477 262 1065","Ідентифікатор: 560 686 4530","Ідентифікатор: 7381071026","Ідентифікатор: 4931440227","Ідентифікатор: 712 5230 4808","Ідентифікатор: 787 1770 4362"]
passwords = ["Пароль: 925830","Пароль: JtReP1","Пароль: 441021","Пароль: K41fvD","Пароль: 7tdLkB","Пароль: 111","Пароль: 864128","Пароль: 537607","Пароль: 123456","Пароль: 981083","Пароль: YFqV2p","Пароль: 3Ux5s9"]

i = True
while i == True :

  lesson = int(input('Номер урока: '))
  if lesson == 1 :
    print("--------------")
    print('' + codes[0])
    print('' + passwords[0])
    print("--------------")
  elif lesson == 2 :
    print("--------------")
    print('' + codes[1])
    print('' + passwords[1])
    print("--------------")
  elif lesson == 3 :
    print("--------------")
    print('' + codes[2])
    print('' + passwords[2])
    print("--------------")
  elif lesson == 4 :
    print("--------------")
    print('' + codes[3])
    print('' + passwords[3])
    print("--------------")
  elif lesson == 5 :
    print("--------------")
    print("1. Наталия Вадимовна ")
    print("2. Ирина Олеговна ")
    print("--------------")
    teacher1 = int(input('Учитель по инглишу: '))
  if teacher1 == 1 :
    print("--------------")
    print('' + codes[4])
    print('' + passwords[4])
    print("--------------")
    teacher1 = 0
  if teacher1 == 2 :
    print("--------------")
    print('' + codes[5])
    print('' + passwords[5])
    print("--------------")
    teacher1 = 0  
  elif lesson == 6 :
    print("--------------")
    print("1. Инна ")
    print("2. Лиля ")
    print("--------------")
    teacher0 = int(input('Учитель по укр.яз/лит: '))
  if teacher0 == 1:
    print("--------------")
    print('' + codes[6])
    print('' + passwords[6])
    print("--------------")
    teacher0 = 0
  if teacher0 == 2:
    print("--------------")
    print('' + codes[7])
    print('' + passwords[7])
    print("--------------")
    teacher0 = 0
  elif lesson == 7 :
    print("--------------")
    print('' + codes[8])
    print('' + passwords[8])
    print("--------------")
  elif lesson == 8 :
    print("--------------")
    print('' + codes[9])
    print('' + passwords[9])
    print("--------------")
  elif lesson == 9 :
    print("--------------")
    print("Татьяна Ткачова")
    print("Дарья Евгеньевна ")
    print("--------------")
    teacher2 = int(input('Учитель по информатике: '))
  if teacher2 == 1 :
    print("--------------")
    print('' + codes[10])
    print('' + passwords[10])
    print("--------------")
    teacher2 = 0
  if teacher2 == 2 :
    print("--------------")
    print('' + codes[11])
    print('' + passwords[11])
    print("--------------")
    teacher2 = 0


  







