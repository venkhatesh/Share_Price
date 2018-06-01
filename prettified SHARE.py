#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import xlwt
from bs4 import BeautifulSoup
import requests
import os
import sys
import smtplib
import mimetypes
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

from optparse import OptionParser
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#flag = 0
#conn = sqlite3.connect(u_name.get() + '.db')
#c = conn.cursor()


# user_name = input('Enter User Name')
# email = input("Enter Email")

def vp_start_gui():
    '''Starting point when module is the main routine.'''

    global val, w, root
    root = Tk()
    top = New_Toplevel(root)
    current_main_support.init(root, top)
    root.mainloop()


w = None


def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''

    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel(w)
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
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font9 = \
            '-family Sylfaen -size 18 -weight bold -slant roman -underline 0 -overstrike 0'

        top.geometry('526x701+650+141')
        top.title('New Toplevel')
        top.configure(background='#d9d9d9')
        top.configure(highlightbackground='#d9d9d9')
        top.configure(highlightcolor='black')

        self.Header = Label(top)
        self.Header.place(relx=0.02, rely=0.01, height=186, width=502)
        self.Header.configure(activebackground='#f9f9f9')
        self.Header.configure(activeforeground='#000000')
        self.Header.configure(background='#d9d9d9')
        self.Header.configure(disabledforeground='#a3a3a3')
        self.Header.configure(font=font9)
        self.Header.configure(foreground='#000000')
        self.Header.configure(highlightbackground='#d9d9d9')
        self.Header.configure(highlightcolor='black')
        self.Header.configure(text='''Share Market Scraper''')

        self.username = Label(top)
        self.username.place(relx=0.02, rely=0.3, height=36, width=122)
        self.username.configure(activebackground='#f9f9f9')
        self.username.configure(activeforeground='black')
        self.username.configure(background='#d9d9d9')
        self.username.configure(disabledforeground='#a3a3a3')
        self.username.configure(foreground='#000000')
        self.username.configure(highlightbackground='#d9d9d9')
        self.username.configure(highlightcolor='black')
        self.username.configure(text='''Username :''')

        self.mailid = Label(top)
        self.mailid.place(relx=0.04, rely=0.37, height=36, width=102)
        self.mailid.configure(activebackground='#f9f9f9')
        self.mailid.configure(activeforeground='black')
        self.mailid.configure(background='#d9d9d9')
        self.mailid.configure(disabledforeground='#a3a3a3')
        self.mailid.configure(foreground='#000000')
        self.mailid.configure(highlightbackground='#d9d9d9')
        self.mailid.configure(highlightcolor='black')
        self.mailid.configure(text='''Email :''')

        self.phoneno = Label(top)
        self.phoneno.place(relx=0.04, rely=0.44, height=26, width=102)
        self.phoneno.configure(activebackground='#f9f9f9')
        self.phoneno.configure(activeforeground='black')
        self.phoneno.configure(background='#d9d9d9')
        self.phoneno.configure(disabledforeground='#a3a3a3')
        self.phoneno.configure(foreground='#000000')
        self.phoneno.configure(highlightbackground='#d9d9d9')
        self.phoneno.configure(highlightcolor='black')
        self.phoneno.configure(text='''Phone :''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.02, rely=0.51, height=26, width=120)
        self.Label5.configure(activebackground='#f9f9f9')
        self.Label5.configure(activeforeground='black')
        self.Label5.configure(background='#d9d9d9')
        self.Label5.configure(disabledforeground='#a3a3a3')
        self.Label5.configure(foreground='#000000')
        self.Label5.configure(highlightbackground='#d9d9d9')
        self.Label5.configure(highlightcolor='black')
        self.Label5.configure(text='''Company Name :''')

        self.u_name = Entry(top)
        self.u_name.place(relx=0.29, rely=0.3, height=24, relwidth=0.69)
        self.u_name.configure(background='white')
        self.u_name.configure(disabledforeground='#a3a3a3')
        self.u_name.configure(font='TkFixedFont')
        self.u_name.configure(foreground='#000000')
        self.u_name.configure(highlightbackground='#d9d9d9')
        self.u_name.configure(highlightcolor='black')
        self.u_name.configure(insertbackground='black')
        self.u_name.configure(selectbackground='#c4c4c4')
        self.u_name.configure(selectforeground='black')

        self.mail_id = Entry(top)
        self.mail_id.place(relx=0.29, rely=0.37, height=24,
                           relwidth=0.69)
        self.mail_id.configure(background='white')
        self.mail_id.configure(disabledforeground='#a3a3a3')
        self.mail_id.configure(font='TkFixedFont')
        self.mail_id.configure(foreground='#000000')
        self.mail_id.configure(highlightbackground='#d9d9d9')
        self.mail_id.configure(highlightcolor='black')
        self.mail_id.configure(insertbackground='black')
        self.mail_id.configure(selectbackground='#c4c4c4')
        self.mail_id.configure(selectforeground='black')

        self.ph_no = Entry(top)
        self.ph_no.place(relx=0.29, rely=0.44, height=24, relwidth=0.69)
        self.ph_no.configure(background='white')
        self.ph_no.configure(disabledforeground='#a3a3a3')
        self.ph_no.configure(font='TkFixedFont')
        self.ph_no.configure(foreground='#000000')
        self.ph_no.configure(highlightbackground='#d9d9d9')
        self.ph_no.configure(highlightcolor='black')
        self.ph_no.configure(insertbackground='black')
        self.ph_no.configure(selectbackground='#c4c4c4')
        self.ph_no.configure(selectforeground='black')

        self.company_name = Entry(top)
        self.company_name.place(relx=0.29, rely=0.51, height=24,
                                relwidth=0.69)
        self.company_name.configure(background='white')
        self.company_name.configure(disabledforeground='#a3a3a3')
        self.company_name.configure(font='TkFixedFont')
        self.company_name.configure(foreground='#000000')
        self.company_name.configure(highlightbackground='#d9d9d9')
        self.company_name.configure(highlightcolor='black')
        self.company_name.configure(insertbackground='black')
        self.company_name.configure(selectbackground='#c4c4c4')
        self.company_name.configure(selectforeground='black')

        def datafetch():
            website_ref = \
                requests.get('https://in.finance.yahoo.com/quote/'
                             + self.company_name.get() + '.NS?p='
                             + self.company_name.get() + '.NS')
            soup = BeautifulSoup(website_ref.content, 'html.parser')
            self.share_value = soup.find('span', class_='Trsdu(0.3s)'
                                    ).get_text().replace(',', '')
            self.output = Label(top,text=self.share_value)
            self.output.place(relx=0.53, rely=0.6, height=56, width=232)
            self.output.configure(background='#d9d9d9')
            self.output.configure(disabledforeground='#a3a3a3')
            self.output.configure(foreground='#000000')
            self.output.configure(width=232)
            #self.output = Label(top,text=share_value.get())
            #print(self.share_value)

        self.MyButton1 = Button(top, command=datafetch)
        self.MyButton1.place(relx=0.02, rely=0.6, height=63, width=246)
        self.MyButton1.configure(activebackground='#d9d9d9')
        self.MyButton1.configure(activeforeground='#000000')
        self.MyButton1.configure(background='#d9d9d9')
        self.MyButton1.configure(disabledforeground='#a3a3a3')
        self.MyButton1.configure(foreground='#000000')
        self.MyButton1.configure(highlightbackground='#d9d9d9')
        self.MyButton1.configure(highlightcolor='black')
        self.MyButton1.configure(pady='0')
        self.MyButton1.configure(text='''Search''')

        def write_db():
            flag = 0
            conn = sqlite3.connect(u_name.get() + '.db')
            c = conn.cursor()


            try:
                c.execute('''create table ''' + u_name.get()
                          + '''(company text,price real)''')
            except:
                c.execute('insert into ' + u_name.get()
                          + '(company,price)values(?,?)',
                          (company_name, share_value))
            flag = 1
            if flag == 0:
                c.execute('insert into ' + u_name.get()
                          + '(company,price)values(?,?)',
                          (company_name, share_value))
            c.execute('select * from ' + u_name.get())
            wb = xlwt.Workbook()
            ws = wb.add_sheet('sample sheet')
            ws.write(0, 0, 'Company')
            ws.write(0, 1, 'Share Price')
            x = 1
            for row in c.fetchall():
                print (row[0], row[1])
                ws.write(x, 0, row[0])
                ws.write(x, 1, row[1])
                x += 1
            wb.save(u_name.get() + '.xls')
            conn.commit()
            conn.close()

        self.MyButton2 = Button(top, command=write_db)
        self.MyButton2.place(relx=0.51, rely=0.7, height=63, width=246)
        self.MyButton2.configure(activebackground='#d9d9d9')
        self.MyButton2.configure(activeforeground='#000000')
        self.MyButton2.configure(background='#d9d9d9')
        self.MyButton2.configure(disabledforeground='#a3a3a3')
        self.MyButton2.configure(foreground='#000000')
        self.MyButton2.configure(highlightbackground='#d9d9d9')
        self.MyButton2.configure(highlightcolor='black')
        self.MyButton2.configure(pady='0')
        self.MyButton2.configure(text='''Add to database''')

        def send_mail():
            fromaddr = 'oslproject18@gmail.com'
            toaddr = self.mail_id.get()
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = 'Hello World'
            body = \
                'Here is Your Share Market Company History \n Sent Using Python Script'
            msg.attach(MIMEText(body, 'plain'))
            filename = u_name.get() + '.xls'
            attachment = open('C:/OsL/' + u_name.get() + '.xls', 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename= %s' % filename)
            msg.attach(part)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, 'oslproject@18')
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

        self.MyButton3 = Button(top, command=send_mail)
        self.MyButton3.place(relx=0.02, rely=0.7, height=63, width=246)
        self.MyButton3.configure(activebackground='#d9d9d9')
        self.MyButton3.configure(activeforeground='#000000')
        self.MyButton3.configure(background='#d9d9d9')
        self.MyButton3.configure(disabledforeground='#a3a3a3')
        self.MyButton3.configure(foreground='#000000')
        self.MyButton3.configure(highlightbackground='#d9d9d9')
        self.MyButton3.configure(highlightcolor='black')
        self.MyButton3.configure(pady='0')
        self.MyButton3.configure(text='''Send as mail''')
        self.MyButton3.configure(width=246)



# def datafetch():
# ....company_name = input("Enter Company Name  :   ")
# ....website_ref = requests.get('https://in.finance.yahoo.com/quote/'+ company_name + '.NS?p=' + company_name + '.NS')
# ....soup = BeautifulSoup(website_ref.content,'html.parser')
# ....share_value=soup.find('span',class_='Trsdu(0.3s)').get_text().replace(',','')

# def snd_mail():
#    fromaddr = "oslproject18@gmail.com"
#    toaddr = email

#    msg = MIMEMultipart()
#    msg['From'] = fromaddr
#    msg['To'] = toaddr
#    msg['Subject'] = "Hello World"
#    body = "Here is Your Share Market Company History \n Sent Using Python Script"
#    msg.attach(MIMEText(body, 'plain'))
#    filename = user_name + ".xls"
#    attachment = open("C:/OsL/"+user_name+".xls", "rb")
#    part = MIMEBase('application', 'octet-stream')
#    part.set_payload((attachment).read())
#    encoders.encode_base64(part)
#    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#    msg.attach(part)
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.starttls()
#    server.login(fromaddr, "oslproject@18")
#    text = msg.as_string()
#    server.sendmail(fromaddr, toaddr, text)
#    server.quit()

# try:
#    c.execute('''create table ''' + user_name + '''(company text,price real)''')
# except:
#    c.execute("insert into " + user_name + "(company,price)values(?,?)",(company_name,share_value))
#    flag=1
# if flag==0:
#    c.execute("insert into " + user_name + "(company,price)values(?,?)",(company_name,share_value))

# c.execute("select * from " + user_name)
# wb = xlwt.Workbook()
# ws = wb.add_sheet('sample sheet')
# ws.write(0, 0, "Comapny")
# ws.write(0, 1, "Share Price")
# x=1
# for row in c.fetchall():
#    print(row[0],row[1])
#    ws.write(x,0,row[0])
#    ws.write(x,1,row[1])
#    x+=1
# wb.save(user_name +'.xls')
# snd_mail()

#conn.commit()
#conn.close()

if __name__ == '__main__':
    vp_start_gui()


			
