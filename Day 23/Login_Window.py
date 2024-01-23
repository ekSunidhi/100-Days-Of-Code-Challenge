from tkinter import *
from PIL import ImageTk, Image # pip install pillow

class LoginForm:
    def __init__(self, window):
        self.window=window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
                
        # ======= Background Image =======
        self.bg_frame=Image.open('images\\x.png')
        photo=ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel=Label(self.window, image=photo)
        self.bg_panel.image=photo
        self.bg_panel.pack(fill='both', expand='yes')
        
        # ======= Login Frame =======
        self.lgn_frame=Frame(self.window, bg='yellow', width='950', height='600')
        self.lgn_frame.place(x=200, y=70)
        
        self.txt='WELCOME'
        self.heading=Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=80, y=30, width=300, height=30)
         
        # ======= Left Side Image =======
        self.side_image=Image.open('images\\y.png')
        photo=ImageTk.PhotoImage(self.side_image)
        self.side_image_label=Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image=photo
        self.side_image_label.place(x=5, y=100)

        # ======= Sign In Image =======
        self.sign_in_image=Image.open('images\\z.png')
        photo=ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label=Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image=photo
        self.sign_in_image_label.place(x=620, y=130)
        
        self.sign_in_label=Label(self.lgn_framw, text='Sign In', bg='#040405', fg='white', 
                                 font=('yu gothic ui', 17, 'bold'))
        self.sign_in_label.place(x=650, y=240)
        
        # ======= Username =======
        self.username_label=Label(self.lgn_frame, text='Username', bg='#040405', font=('yu gothic ui', 13, 'bold'))

def page():
    window=Tk()
    LoginForm(window)
    window.mainloop()
    
if __name__=='__main__':
    page()