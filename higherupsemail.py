from tkinter import *
from tkinter import Toplevel
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pickle
import os.path

class Address:
    def __init__(self, name, email, department, level):
        self.name = name
        self.email = email
        self.department = department
        self.level = level


class HigherUpsEmail:
    def __init__(self):
        window = Tk()
        window.title("E-mail Your Higher Ups")

        self.ports =  [587,587,587,465, 465, 465, 465, 465, 25, 25, 587, 465, 465, 25, 25, 25, 25, 25, 25, 465, 25, 587, 587, 587, 587, 465, 587, 465, 465, 465]
        self.servername = ["Chose your email provider","gmail","outlook","office365","Yahoo", "Yahoo Mail Plus", "Yahoo Uk"
                           "Yahoo Deutschland", "Yahoo AU/NZ", "O2", "AOL", "AT&T", "NTL @ntlworld.com", "BT Connect",
                           "BT Openworld", "BT Internet", "Orange", "Orange.uk", "Wandoo UK", "Hotmail", "O2 Online Deutschland", "T-Online Deutschland",
                           "1&1 (1and1)", "1&1 Deutschland", "Comcast", "Verizon", "Verizon (Yahoo Hosted)", "Zoho Mail", "Mail.com", "GMX.com"]
        self.server = ["smtp.gmail.com", "smtp.outlook.com", "smtp.office365.com", "smtp.mail.yahoo.com", "plus.smtp.mail.yahoo.com", "smtp.mail.yahoo.co.uk"
                       , "smtp.mail.yahoo.com", "smtp.mail.yahoo.com.au", "smtp.o2.ie", "smtp.o2.co.uk", "smtp.aol.com", "smtp.att.yahoo.com", "smtp.ntlworld.com"
                       , "mail.btconnect.com", "mail.btopenworld.com", "mail.btinternet.com", "smtp.orange.net", "smtp.orange.co.uk", "smtp.wandoo.co.uk", "smtp.live.com",
                       "mail.o2online.de", "secure.smtp.t-online.de", "smtp.1and1.com", "smtp.1und1.de", "smtp.comcast.net", "outgoing.verizon.net",
                       "outgoing.yahoo.verizon.net", "smtp.zoho.com", "smtp.mail.com", "smtp.gmx.com"]
        self.emailEndings = ["gmail.com", "outlook.com", "office365.com", "yahoo.com", "yahoo.com", "yahoo.co.uk", "yahoo.com", "yahoo.com.au", "o2.ie", "o2.co.uk",
                             "aol.com", "att.yahoo.com", "ntlworld.com", "btconnect.com", "btopenworld.com.", "btinternet.com", "orange.net", "orange.co.uk",
                             "wandoo.co.uk", "hotmail.com", "o2online.de", "t-online.de", "1and1.com", "1und1.de", "comcast.net", "verizon.net", "yahoo.verizon.net",
                             "zoho.com", "gmx.com"]
        self.index = 0
        
        
        # Create a menu bar
        menubar = Menu(window)
        window.config(menu = menubar) # Display the menu bar
        
        # create a pulldown menu, and add it to the menu bar
        userMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Users", menu = userMenu)
        userMenu.add_command(label = "Login",  command = self.userLogin)
        
        self.password = StringVar()
        self.email = StringVar()
        

        
        
        
        self.addressInformation = self.loadAddress()
        self.dep = set()
        for i in range(len(self.addressInformation)):
            self.dep.add(self.addressInformation[i].department)
        self.dpt = []
        for i in self.dep:
            self.dpt.append(i)
        self.dpt.insert(0, "Choose a Department")
        print(self.dpt)
        
        self.levl = []
        for i in range(len(self.dpt)):
            self.levl.append({"Choose a Level"})
            for j in range(len(self.addressInformation)):
                if self.addressInformation[j].department == self.dpt[i]:
                    self.levl[i].add(self.addressInformation[j].level)
        self.lvl = []
        for i in range(len(self.levl)):
            self.lvl.append([])
            for j in self.levl[i]:
                self.lvl[i].append(j)



        self.f1 = Frame(window)
        self.f1.pack()
        f2 = Frame(window)
        f2.pack()
        

        Label(self.f1, text = "From: ").grid(row = 1, column = 1)
        Entry(self.f1, textvariable = self.email, state = DISABLED, width = 50).grid(row = 1, column = 2)
        Button(self.f1, text = "Send", command = self.send).grid(row = 1, column = 3, rowspan = 3)
        Label(self.f1, text = "To: ").grid(row = 2, column = 1)
        self.targetDepartment = StringVar()
        self.targetDepartment.set(self.dpt[0])
        self.chosenDepartment = OptionMenu(self.f1, self.targetDepartment, *self.dpt, command = self.setLevels)
        self.chosenDepartment.grid(row = 2, column = 2)
        self.targetLevel = StringVar()
        self.targetLevel.set(self.lvl[0][0])
        self.chosenLevel = OptionMenu(self.f1, self.targetLevel, *self.lvl[0])
        self.chosenLevel.grid(row = 3, column = 2)
        self.subject = StringVar()
        Label(self.f1, text = "Subject: ").grid(row = 4, column = 1)
        Entry(self.f1, textvariable = self.subject, width = 50).grid(row = 4, column = 2)
        self.message = Text(self.f1, width = 80)
        self.message.grid(row=5, column = 1, columnspan = 4)

        Button(f2, text = "Clear", command = self.clearEmail).pack()


        

        

        
        window.mainloop()

    def userLogin(self):
        #make popup window
        self.w = Toplevel()
        self.w.title("Log in Information")

        #frame1 will be used to make the entry forms
        frame1 = Frame(self.w)
        frame1.pack()
        #frame2 will house the buttons 
        frame2 = Frame(self.w)
        frame2.pack()

        
        #log in location
        Label(frame1, text="Email:").grid(row = 1, column = 1)
        Entry(frame1, width = 25, textvariable = self.email).grid(row = 1, column = 2)
        Label(frame1, text = "@").grid(row = 1, column = 3)
        self.provider = StringVar()
        self.provider.set(self.servername[0])
        OptionMenu(frame1, self.provider, *self.servername, command = self.emailProvider).grid(row = 1, column = 4)
        Label(frame1, text = "Password:").grid(row = 2, column = 1)
        Entry(frame1, width = 25, textvariable = self.password, show = "*").grid(row = 2, column = 2)

        #set buttons
        Button(frame2, text = "Login", command = self.login).pack(side = LEFT)
        Button(frame2, text = "Clear", command = self.clear).pack(side = LEFT)
        

    def login(self):
        useremail = self.email.get()+"@"+self.emailEndings[self.index]
        self.email.set(useremail)
        self.w.destroy()

    def clear(self):
        self.email.set("")
        self.password.set("")
        self.subject.set("")
        

    def setLevels(self, x):
        self.index = self.dpt.index(x)
        self.chosenLevel = OptionMenu(self.f1, self.targetLevel, *self.lvl[self.index])
        self.chosenLevel.grid(row = 3, column = 2)

    def loadAddress(self):
        if not os.path.isfile("emails.dat"):
            return [] # Return an empty list

        try:
            infile = open("emails.dat", "rb")
            addressList = pickle.load(infile)
        except EOFError:
            addressList = []
            
        infile.close()
        return addressList

    def clearEmail(self):
        self.toEmail.set("")
        self.subject.set("")
        self.message.delete(1.0, END)

    def emailProvider(self, provider):
        self.index = self.servername.index(provider)
        self.index -=1
        

    def send(self):
        self.msg = MIMEMultipart()
        server = smtplib.SMTP(self.server[self.index], self.port[self.index])
        server.ehlo()
        server.starttls()
        server.login(self.email.get(), self.password.get())
        for i in range(len(self.addressInformation)):
            if self.addressInformation[i].department == self.targetDepartment.get():
                self.msg['From'] = self.email.get()
                self.msg['To'] = self.addressInformation[i].email
                self.msg['Subject'] = self.subject.get()
                self.msg.attach(MIMEText(self.message.get("1.0",END), 'plain'))
                self.txt = self.msg.as_string()
                server.sendmail(self.email.get(), self.toEmail.get(), self.txt)
        server.quit()
        self.clearEmail()

HigherUpsEmail()
