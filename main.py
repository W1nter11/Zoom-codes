import os
def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)

lesson = 0
teacher0 = 0
teacher1 = 0
teacher2 = 0
idntpswrd0 = 0
idntpswrd1 = 0






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

codes = ["856 443 7134","717 7405 4453","762 646 9234","783 6085 9503","793 1912 0930","379 853 5977","477 262 1065","560 686 4530","7381071026","4931440227","712 5230 4808","787 1770 4362"]
passwords = ["925830","JtReP1","441021","K41fvD","7tdLkB","111","864128","537607","123456","981083","YFqV2p","3Ux5s9"]

i = 1
while i == 1 :
  
  lesson = int(input('Номер урока: '))

  if lesson == 1 :
    print("--------------")
    print("Илюша")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd0 = int(input('?: '))
  if idntpswrd0 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[0])
    idntpswrd0 = 0
  if idntpswrd0 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[0])
    idntpswrd0 = 0
  if lesson == 2 :
    print("--------------")
    print("Физика")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd0 = int(input('?: '))
  if idntpswrd0 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[1])
    idntpswrd0 = 0
  if idntpswrd0 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[1])
    idntpswrd0 = 0
  if lesson == 3 :
    print("--------------")
    print("Матеша")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd0 = int(input('?: '))
  if idntpswrd0 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[2])
    idntpswrd0 = 0
  if idntpswrd0 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[2])
    idntpswrd0 = 0
  if lesson == 4 :
    print("--------------")
    print("Технологии")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd0 = int(input('?: '))
  if idntpswrd0 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[3])
    idntpswrd0 = 0
  if idntpswrd0 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[3])
    idntpswrd0 = 0
  if lesson == 5 :
    print("--------------")
    print("1. Наталия Вадимовна ")
    print("2. Ирина Олеговна ")
    print("--------------")
    teacher0 = int(input('Учитель по инглишу: '))
  if teacher0 == 1:
    print("--------------")
    print("Инглиш (Наталия Вадимовна)")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd1 = int(input('?: '))
  if idntpswrd1 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[4])
    idntpswrd1 = 0
  if idntpswrd1 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[4])
    idntpswrd1 = 0
  if teacher0 == 2:
    print("--------------")
    print("Инглиш (Ирина Олеговна)")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd1 = int(input('?: '))
  if idntpswrd1 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[5])
    idntpswrd1 = 0
  if idntpswrd1 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[5])
    idntpswrd1 = 0
  if lesson == 6 :
    print("--------------")
    print("1. Инна ")
    print("2. Лиля ")
    print("--------------")
    teacher1 = int(input('Учитель по укр.яз/лит: '))
  if teacher1 == 1:
    print("--------------")
    print("Укр.мова,літ (Инна)")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd1 = int(input('?: '))
  if idntpswrd1 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[6])
    idntpswrd1 = 0
  if idntpswrd1 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[6])
    idntpswrd1 = 0
  if teacher1 == 2:
    print("--------------")
    print("Укр.мова,літ (Лиля)")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd1 = int(input('?: '))
  if idntpswrd1 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[7])
    idntpswrd1 = 0
  if idntpswrd1 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[7])
    idntpswrd1 = 0
  if lesson == 7 :
    print("--------------")
    print("Химия")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd0 = int(input('?: '))
  if idntpswrd0 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[8])
    idntpswrd0 = 0
  if idntpswrd0 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[8])
    idntpswrd0 = 0
  if lesson == 8 :
    print("--------------")
    print("Биология")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd0 = int(input('?: '))
  if idntpswrd0 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[9])
    idntpswrd0 = 0
  if idntpswrd0 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[9])
    idntpswrd0 = 0
  if lesson == 9 :
    print("--------------")
    print("Татьяна Ткачова")
    print("Дарья Евгеньевна")
    print("--------------")
    teacher2 = int(input('Учитель по информатике: '))
  if teacher2 == 1:
    print("--------------")
    print("Информатика (Татьяна Ткачова)")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd1 = int(input('?: '))
  if idntpswrd1 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[10])
    idntpswrd1 = 0
  if idntpswrd1 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[10])
    idntpswrd1 = 0
  if teacher2 == 2:
    print("--------------")
    print("Информатика (Дарья Евгеньевна)")
    print("1. Скопировать идентефикатор ")
    print("2. Скопировать пароль ")
    print("--------------")
    idntpswrd1 = int(input('?: '))
  if idntpswrd1 == 1 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + codes[11])
    idntpswrd1 = 0
  if idntpswrd1 == 2 : 
    print("Скопировано в буфер обмена")
    addToClipBoard('' + passwords[11])
    idntpswrd1 = 0




