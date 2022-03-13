from tkinter import *
from tkinter import messagebox
import pickle as pkl

width = int(450)
height = int(285)
width_offset = 550
height_offset = 250
bkcolor = '#6BA396'
textcolor = '#5A5A5A'

# 初始化
window = Tk()
window.title('Welcome to login!')
window.geometry('{}x{}+{}+{}'.format(width, height, width_offset, height_offset))

# 背景图
canvas = Canvas(window, width=width, height=height)
img = PhotoImage(file='./img/image.gif')
image = canvas.create_image(0, 0, anchor='nw', image=img)
canvas.pack(side='top')
# label+entry
x_label = 275
y_label = 70
Label(window, text="User Name:",
      fg='white', bg=bkcolor,
      font=("MS Reference Sans Serif", 13)
      ).place(x=x_label, y=y_label)

username = StringVar()
# username.set('example@qq.com')
username_entry = Entry(window, bd=3, textvariable=username, fg=textcolor)
username_entry.place(x=x_label + 5, y=y_label + 30)

Label(window, text="Password:",
      fg='white', bg='#6BA396',
      font=("MS Reference Sans Serif", 13)
      ).place(x=x_label, y=y_label + 60)

password = StringVar()
# username.set('example@qq.com')
password_entry = Entry(window, bd=3, textvariable=password, fg=textcolor, show='*')
password_entry.place(x=x_label + 5, y=y_label + 90)


def user_login():
    user_name = username.get()
    user_password = password.get()
    try:
        with open('src/users_info.pkl', 'rb') as user_file:
            users_info = pkl.load(user_file)
    except FileNotFoundError:
        with open('src/users_info.pkl', 'wb') as user_file:
            users_info = {'admin': 'admin'}
            pkl.dump(users_info, user_file)
    if user_name in users_info:  # 可以 str in map
        if user_password == users_info[user_name]:
            messagebox.showinfo(title='Login successfully', message='Welcome ' + user_name + '!')
            window.destroy()
        else:
            messagebox.showerror(title='Fail to login', message='Incorrect password!')
    else:
        if messagebox.askyesno(title='Login?', message="The account hasn't been registered.\nSign up?"):
            user_signup()
        username_entry.delete(0, END)
        password_entry.delete(0, END)


def user_signup():
    def check_sign_up():
        nn = newusername.get()
        np = newpassword.get()
        npc = confirmpassword.get()
        with open('src/users_info.pkl', 'rb') as user_file:
            exist_users_info = pkl.load(user_file)
        if len(nn) == 0 or len(np) == 0:
            messagebox.showerror(title='Error', message="Username or Password can not be empty!")
        elif np != npc:
            messagebox.showerror(title='Error', message="Password and confirm password don't match!")
        elif nn in exist_users_info:
            messagebox.showerror(title='Error', message="The account has been registered!")
        else:
            exist_users_info[nn] = np
            with open('src/users_info.pkl', 'wb') as user_file:
                pkl.dump(exist_users_info, user_file)
            messagebox.showinfo(title='Sign up successfully', message='You have successfully singed up!')
            signup_window.destroy()

    # 初始化
    signup_window = Toplevel(window)
    signup_window.geometry('{}x{}+{}+{}'.format(width, height, width_offset, height_offset))
    signup_window.title('Sign Up Window')
    signup_window.iconbitmap('./img/login.ico')

    # 背景图
    canvas = Canvas(signup_window, width=width, height=height)
    image = canvas.create_image(0, 0, anchor='nw', image=img)
    canvas.pack(side='top')

    # label+entry
    x_label = 275
    y_label = 30
    Label(signup_window, text="User Name:",
          fg='white', bg=bkcolor,
          font=("MS Reference Sans Serif", 13)
          ).place(x=x_label, y=y_label)

    newusername = StringVar()
    username_entry = Entry(signup_window, bd=3, textvariable=newusername, fg=textcolor)
    username_entry.place(x=x_label + 5, y=y_label + 30)

    Label(signup_window, text="Password:",
          fg='white', bg='#6BA396',
          font=("MS Reference Sans Serif", 13)
          ).place(x=x_label, y=y_label + 60)

    newpassword = StringVar()
    password_entry = Entry(signup_window, bd=3, textvariable=newpassword, fg=textcolor, show='*')
    password_entry.place(x=x_label + 5, y=y_label + 90)

    Label(signup_window, text="Confirm Password:",
          fg='white', bg='#6BA396',
          font=("MS Reference Sans Serif", 13)
          ).place(x=x_label, y=y_label + 120)

    confirmpassword = StringVar()
    password_entry = Entry(signup_window, bd=3, textvariable=confirmpassword, fg=textcolor, show='*')
    password_entry.place(x=x_label + 5, y=y_label + 150)

    # button
    Button(signup_window, bd=3, text='Sign Up', command=check_sign_up, font=("MS Reference Sans Serif", 10)).place(
        x=320, y=220)


# button
x_button = 280
y_button = 220

Button(window, bd=3, text='Login', command=user_login, font=("MS Reference Sans Serif", 10)).place(x=x_button,
                                                                                                   y=y_button)
Button(window, bd=3, text='Sign Up', command=user_signup, font=("MS Reference Sans Serif", 10)).place(x=x_button + 86,
                                                                                                      y=y_button)

window.iconbitmap('./img/login.ico')
window.mainloop()
