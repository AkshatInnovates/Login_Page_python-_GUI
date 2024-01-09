from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'jn.akshat.11@gmail.com' and password =='1234':
        messagebox.showinfo('Login Successful')
    else:
        messagebox.showerror('Error','Login Failed')

root = Tk()
root.title('Login Window')
root.geometry('350x500')
root.iconbitmap('icons8_linkedin_16_sgX_icon.ico')
root.config(bg='#1F51FF')

img = Image.open('Blue Minimalist Media Company Logo.png')
resized_img= img.resize((100,100))
img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack()

label=Label(root,text='Welcome to Login Window',bg='#1F51FF',fg='white')
label.config(font=('bold'))
label.pack(pady=(10,10))

email_label=Label(root,text='Enter Email',fg='white',bg='#1F51FF')
email_label.config(font=('bold',12))
email_label.pack(pady=(20,20))

email_input= Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label = Label(root,text='Enter Password',fg='white',bg='#1F51FF')
password_label.config(font=('bold',12))
password_label.pack(pady=(20,20))

password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root,text="Login Here",bg='white',fg='black',command=handle_login)
# login_btn.config(font=('bold'))
login_btn.pack(pady=(10,20))
root.mainloop()