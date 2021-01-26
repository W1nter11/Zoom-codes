from tkinter import *


main = Tk()
main['bg'] = '#fafafa'
main.title('Zoom Codes')
main.wm_attributes('-alpha', 0.7)
main.geometry('400x350')
main.resizable(width=False, height=False)

framemain = Frame(main, bg='#FFA07A', bd=5)
framemain.place(relx=0, rely=0, relwidth=1.5, relheight=1)
frameside = Frame(main, bg='#4682B4', bd=5)
frameside.place(relx=0, rely=0, relwidth=0.5, relheight=1)

cityField = Entry(frameside, bg='white', font=0)
cityField.pack()

info = Label(frameside, text='Предмет\n1. Илюша\n2. Физика\n3. Матеша\n4. Технологии\n5. Инглиш\n6. Укр.мова,літ\n7. Химия\n8. Биология\n9. Информатика\n10. LSE\nНомер урока:', bg='#B0C4DE', font=40)
info.pack()
main.mainloop()
