from tkinter import *
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('member.db')

c = conn.cursor()

def submitMember(*args):

    try:
        # print (firstName)
        # print (lastName)
        print('entered try')
        if  not firstName.get():
            statusLabel.config(text = 'Please supply a First Name!')
        elif  not lastName.get():
            statusLabel.config(text = 'Please supply a Last Name!')
        elif  not primaryPhone.get():
            statusLabel.config(text = 'Please supply a Phone Number or write None!')
        elif  not primaryEmail.get():
            statusLabel.config(text = 'Please supply a Email or write None!')
        elif  not canText.get():
            statusLabel.config(text = 'Please select a text status!')
        elif  not sex.get():
            statusLabel.config(text = 'Please select the sex!')
        elif  not marriedStatus.get():
            statusLabel.config(text = 'Please select the marital status. Choose Single if unknown!')
        else:
            statusLabel.config(text = 'All Criteria Valid')
            print('firstName:',firstName.get(),'aa')
            print('lastName:',lastName.get())
            print('primaryphone:',primaryPhone.get())
            print('text:',canText.get())
            print('email:',primaryEmail.get())
            print('sex:',sex.get())
            print('marriedstatus:',marriedStatus.get())
    except ValueError:
        pass


root = Tk()
root.title("Add a New Member")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

firstName = StringVar()
lastName = StringVar()
primaryPhone = StringVar()
canText = StringVar()
primaryEmail = StringVar()
sex= StringVar()
marriedStatus = StringVar()

firstName_entry = ttk.Entry(mainframe, width=12, textvariable=firstName)
firstName_entry.grid(column=2, row=1, sticky=(W, E))
lastName_entry = ttk.Entry(mainframe, width=12, textvariable=lastName)
lastName_entry.grid(column=2, row=2, sticky=(W, E))
primaryPhone_entry = ttk.Entry(mainframe, width=12, textvariable=primaryPhone)
primaryPhone_entry.grid(column=2, row=3, sticky=(W, E))
primaryEmail_entry = ttk.Entry(mainframe, width=30, textvariable=primaryEmail)
primaryEmail_entry.grid(column=2, row=4, sticky=(W, E),columnspan=3)
canTextBtn1 = ttk.Radiobutton(mainframe, text='Yes', variable=canText, value='yes')
canTextBtn1.grid(column=2, row=5, sticky=(W, E))
canTextBtn2 = ttk.Radiobutton(mainframe, text='No', variable=canText, value='no')
canTextBtn2.grid(column=3, row=5, sticky=(W, E))
sexBtn1  = ttk.Radiobutton(mainframe, text='Male', variable=sex, value='male')
sexBtn1.grid(column=2, row=6, sticky=(W, E))
sexBtn2 = ttk.Radiobutton(mainframe, text='Female', variable=sex, value='female')
sexBtn2.grid(column=3, row=6, sticky=(W, E))

#marriedStatusCmb = ttk.Entry(mainframe, width=7, textvariable=marriedStatus)
marriedStatusCmb = ttk.Combobox(mainframe, state="readonly", textvariable=marriedStatus, values = ('Single', 'Engaged', 'Married', 'Divorced'))
#marriedStatusCmb.values = ('Single', 'Engaged', 'Married', 'Divorced')
marriedStatusCmb.grid(column=2, row=7, sticky=(W, E))

ttk.Label(mainframe, text="First Name").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Last Name").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Primary Phone").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Primary Email").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Can Text?").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Sex").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Married?").grid(column=1, row=7, sticky=W)

statusLabel = ttk.Label(mainframe, text = 'Please fill in the fields')
statusLabel.grid(column=1, row=8, columnspan=3, sticky=(W,E))
ttk.Button(mainframe, text="Save Member", command=submitMember).grid(column=2, row=9, sticky=(W,E),columnspan=2)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
#lines that I might need in some form shortly
#feet_entry.focus()
root.bind('<Return>', submitMember)

root.mainloop()
print('passed mainloop')