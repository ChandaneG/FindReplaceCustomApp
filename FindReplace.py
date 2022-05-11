import os, fnmatch
from datetime import date
from tkinter import *
from tkinter import messagebox
from shutil import copyfile
import configparser

fields = 'Folder', 'Search', 'Replace', 'FilePattern'

def fetch(entvals):
#    print entvals
#    print ents
    entItems = entvals.items()
    for entItem in entItems:
        field = entItem[0]
        text  = entItem[1].get()
        print('%s: "%s"' % (field, text))

def findReplace(entvals):
#    print ents
    directory = entvals.get("Folder").get()
    find = entvals.get("Search").get()
    replace = entvals.get("Replace").get()
    filePattern = entvals.get("FilePattern").get()

    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    f= open("Test.txt","a+")
    f.writelines("File pattern found on DATE : " + d1 + "\n")

    for path, dirs,files in os.walk(os.path.abspath(directory)):
        #print(len(fnmatch.filter(files, filePattern)))        
        for filename in fnmatch.filter(files, filePattern):
#            print filename
            filepath = os.path.join(path, filename)
# Can be commented out --  used for confirmation            
            print(filepath)
            copyfile(filepath, path + "\\" + today.strftime("%d_%m_%Y") + "_" + filename)
            #messagebox.showinfo(filepath, "Information")             
            f= open("Test.txt","a+")
            f.writelines(filepath + "\n")
            
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

def makeform(root, fields):
    entvals = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=17, text=field+": ", anchor='w')
        ent = Entry(row)
        
        if field == "Folder":
            ent.insert(END, os.getcwd())
        
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entvals[field] = ent
        print(ent)
    return entvals

if __name__ == '__main__':
    root = Tk()
    root.title("Recursive S&R")
    ents = makeform(root, fields)
#    print ents
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)

    b2 = Button(root, text='Execute', command=(lambda e=ents: findReplace(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
       
    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=LEFT, padx=5, pady=5)

    lab = Label(root,width=81, text="For Suggestions : gokul.chandane@kantar.com", anchor='w')
    lab.pack(side=LEFT)
   
    root.mainloop()