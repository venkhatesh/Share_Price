#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Apr 19, 2018 02:07:38 AM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import current_main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    current_main_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    current_main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family Sylfaen -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("526x701+650+141")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Header = Label(top)
        self.Header.place(relx=0.02, rely=0.01, height=186, width=502)
        self.Header.configure(activebackground="#f9f9f9")
        self.Header.configure(activeforeground="#000000")
        self.Header.configure(background="#d9d9d9")
        self.Header.configure(disabledforeground="#a3a3a3")
        self.Header.configure(font=font9)
        self.Header.configure(foreground="#000000")
        self.Header.configure(highlightbackground="#d9d9d9")
        self.Header.configure(highlightcolor="black")
        self.Header.configure(text='''Share Market Scraper''')

        self.username = Label(top)
        self.username.place(relx=0.02, rely=0.3, height=36, width=122)
        self.username.configure(activebackground="#f9f9f9")
        self.username.configure(activeforeground="black")
        self.username.configure(background="#d9d9d9")
        self.username.configure(disabledforeground="#a3a3a3")
        self.username.configure(foreground="#000000")
        self.username.configure(highlightbackground="#d9d9d9")
        self.username.configure(highlightcolor="black")
        self.username.configure(text='''Username :''')

        self.mailid = Label(top)
        self.mailid.place(relx=0.04, rely=0.37, height=36, width=102)
        self.mailid.configure(activebackground="#f9f9f9")
        self.mailid.configure(activeforeground="black")
        self.mailid.configure(background="#d9d9d9")
        self.mailid.configure(disabledforeground="#a3a3a3")
        self.mailid.configure(foreground="#000000")
        self.mailid.configure(highlightbackground="#d9d9d9")
        self.mailid.configure(highlightcolor="black")
        self.mailid.configure(text='''Email :''')

        self.phoneno = Label(top)
        self.phoneno.place(relx=0.04, rely=0.44, height=26, width=102)
        self.phoneno.configure(activebackground="#f9f9f9")
        self.phoneno.configure(activeforeground="black")
        self.phoneno.configure(background="#d9d9d9")
        self.phoneno.configure(disabledforeground="#a3a3a3")
        self.phoneno.configure(foreground="#000000")
        self.phoneno.configure(highlightbackground="#d9d9d9")
        self.phoneno.configure(highlightcolor="black")
        self.phoneno.configure(text='''Phone :''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.02, rely=0.51, height=26, width=120)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Company Name :''')

        self.u_name = Entry(top)
        self.u_name.place(relx=0.29, rely=0.3,height=24, relwidth=0.69)
        self.u_name.configure(background="white")
        self.u_name.configure(disabledforeground="#a3a3a3")
        self.u_name.configure(font="TkFixedFont")
        self.u_name.configure(foreground="#000000")
        self.u_name.configure(highlightbackground="#d9d9d9")
        self.u_name.configure(highlightcolor="black")
        self.u_name.configure(insertbackground="black")
        self.u_name.configure(selectbackground="#c4c4c4")
        self.u_name.configure(selectforeground="black")

        self.mail_id = Entry(top)
        self.mail_id.place(relx=0.29, rely=0.37,height=24, relwidth=0.69)
        self.mail_id.configure(background="white")
        self.mail_id.configure(disabledforeground="#a3a3a3")
        self.mail_id.configure(font="TkFixedFont")
        self.mail_id.configure(foreground="#000000")
        self.mail_id.configure(highlightbackground="#d9d9d9")
        self.mail_id.configure(highlightcolor="black")
        self.mail_id.configure(insertbackground="black")
        self.mail_id.configure(selectbackground="#c4c4c4")
        self.mail_id.configure(selectforeground="black")

        self.ph_no = Entry(top)
        self.ph_no.place(relx=0.29, rely=0.44,height=24, relwidth=0.69)
        self.ph_no.configure(background="white")
        self.ph_no.configure(disabledforeground="#a3a3a3")
        self.ph_no.configure(font="TkFixedFont")
        self.ph_no.configure(foreground="#000000")
        self.ph_no.configure(highlightbackground="#d9d9d9")
        self.ph_no.configure(highlightcolor="black")
        self.ph_no.configure(insertbackground="black")
        self.ph_no.configure(selectbackground="#c4c4c4")
        self.ph_no.configure(selectforeground="black")

        self.company_name = Entry(top)
        self.company_name.place(relx=0.29, rely=0.51,height=24, relwidth=0.69)
        self.company_name.configure(background="white")
        self.company_name.configure(disabledforeground="#a3a3a3")
        self.company_name.configure(font="TkFixedFont")
        self.company_name.configure(foreground="#000000")
        self.company_name.configure(highlightbackground="#d9d9d9")
        self.company_name.configure(highlightcolor="black")
        self.company_name.configure(insertbackground="black")
        self.company_name.configure(selectbackground="#c4c4c4")
        self.company_name.configure(selectforeground="black")

        self.MyButton1 = Button(top)
        self.MyButton1.place(relx=0.02, rely=0.6, height=63, width=246)
        self.MyButton1.configure(activebackground="#d9d9d9")
        self.MyButton1.configure(activeforeground="#000000")
        self.MyButton1.configure(background="#d9d9d9")
        self.MyButton1.configure(disabledforeground="#a3a3a3")
        self.MyButton1.configure(foreground="#000000")
        self.MyButton1.configure(highlightbackground="#d9d9d9")
        self.MyButton1.configure(highlightcolor="black")
        self.MyButton1.configure(pady="0")
        self.MyButton1.configure(text='''Search''')

        self.MyButton2 = Button(top)
        self.MyButton2.place(relx=0.51, rely=0.7, height=63, width=246)
        self.MyButton2.configure(activebackground="#d9d9d9")
        self.MyButton2.configure(activeforeground="#000000")
        self.MyButton2.configure(background="#d9d9d9")
        self.MyButton2.configure(disabledforeground="#a3a3a3")
        self.MyButton2.configure(foreground="#000000")
        self.MyButton2.configure(highlightbackground="#d9d9d9")
        self.MyButton2.configure(highlightcolor="black")
        self.MyButton2.configure(pady="0")
        self.MyButton2.configure(text='''Add to database''')

        self.MyButton3 = Button(top)
        self.MyButton3.place(relx=0.02, rely=0.7, height=63, width=246)
        self.MyButton3.configure(activebackground="#d9d9d9")
        self.MyButton3.configure(activeforeground="#000000")
        self.MyButton3.configure(background="#d9d9d9")
        self.MyButton3.configure(disabledforeground="#a3a3a3")
        self.MyButton3.configure(foreground="#000000")
        self.MyButton3.configure(highlightbackground="#d9d9d9")
        self.MyButton3.configure(highlightcolor="black")
        self.MyButton3.configure(pady="0")
        self.MyButton3.configure(text='''Send as mail''')
        self.MyButton3.configure(width=246)

        self.output = Label(top)
        self.output.place(relx=0.53, rely=0.6, height=56, width=232)
        self.output.configure(background="#d9d9d9")
        self.output.configure(disabledforeground="#a3a3a3")
        self.output.configure(foreground="#000000")
        self.output.configure(width=232)






if __name__ == '__main__':
    vp_start_gui()


