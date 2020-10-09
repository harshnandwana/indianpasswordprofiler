import random
from tkinter import *
import os
def d(outp):
	op1=open("d.txt","w")
	op1.write(outp)
root = Tk()
root.title("Indian password Cracker")
label = Label(root, text= "@Viruss &")
label1 = Label(root, text="@infernorobotics")
def old():
	old = Toplevel()
	old.title("Enter Old target Details") 
	Label(old, text='First Name').grid(row=0) 
	Label(old, text='Last Name').grid(row=1)
	e1 = Entry(old) 
	e2 = Entry(old)
	def clickold():
		out=e1.get()+"_"+e2.get()+"_details.txt"
		d(out)
		old.destroy()
		root.destroy()
	button3 = Button(old, text='Submit', command=clickold)
	e1.grid(row=0, column=1) 
	e2.grid(row=1, column=1)
	button3.grid(row=2, column=1)  
def new():
	master = Toplevel()
	master.title("Enter target Details") 
	Label(master, text='First Name').grid(row=0) 
	Label(master, text='Last Name').grid(row=1) 
	Label(master, text='Date').grid(row=2) 
	Label(master, text='Month').grid(row=3) 
	Label(master, text='Year').grid(row=4)
	Label(master, text='Mobile Number').grid(row=5) 
	Label(master, text='Nickname').grid(row=6)  
	e1 = Entry(master) 
	e2 = Entry(master)
	e3 = Entry(master) 
	e4 = Entry(master)
	e5 = Entry(master) 
	e6 = Entry(master)
	e7 = Entry(master)
	def clicked():
	   ip=open(e1.get()+"_"+e2.get()+"_details.txt","w")
	   ip.write(e1.get()+"\n")
	   ip.write(e2.get()+"\n")
	   ip.write(e3.get()+"\n")
	   ip.write(e4.get()+"\n")
	   ip.write(e5.get()+"\n")
	   ip.write(e6.get()+"\n")
	   ip.write(e7.get()+"\n")
	   out=e1.get()+"_"+e2.get()+"_details.txt"
	   d(out)
	   master.destroy()
	   root.destroy()
	button = Button(master, text='Submit', command=clicked)  
	e1.grid(row=0, column=1) 
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1) 
	e4.grid(row=3, column=1)
	e5.grid(row=4, column=1) 
	e6.grid(row=5, column=1)
	e7.grid(row=6, column=1)
	button.grid(column=1, row=7)
	master.mainloop()
button1 = Button(root, text='New Target', command=new)
button2 = Button(root, text='Old Target', command=old) 
label.grid(row=1, column=1)
label1.grid(row=1, column=2)
button1.grid(row=2, column=1) 
button2.grid(row=2, column=2)
root.mainloop()
print("                    uuuuuuu                                                   ")
print("                  uu$$$$$$$$$$$uu                                                ")
print("               uu$$$$$$$$$$$$$$$$$uu                                             ")
print("              u$$$$$$$$$$$$$$$$$$$$$u                                            ")
print("             u$$$$$$$$$$$$$$$$$$$$$$$u                                           ")
print("            u$$$$$$$$$$$$$$$$$$$$$$$$$u                   				       ")
print("            u$$$$$$$$$$$$$$$$$$$$$$$$$u                                          ")
print("            u$$$$$$*   *$$$*   *$$$$$$u                        G O             ")
print("             $$$u       u$u       u$$$                         O N            ")
print("             $$$u      u$$$u      u$$$                                           ")
print("              *$$$$uu$$$   $$$uu$$$$*                         T R Y             ")
print("               *$$$$$$$*   *$$$$$$$*                                             ")
print("                 u$$$$$$$u$$$$$$$u                           T H I S             ")
print("                  u$*$*$*$*$*$*$u                                                ")
print("       uuu        $$u$ $ $ $ $u$$       uuu                                      ")
print("      u$$$$        $$$$$u$u$u$$$       u$$$$                                     ")
print("       $$$$$uu      *$$$$$$$$$*     uu$$$$$$                                     ")
print("     u$$$$$$$$$$$uu    **#**    uuuu$$$$$$$$$$                                   ")
print("     *$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*                                   ")
print("      ***      **$$$$$$$$$$$uu **$***                                            ")
print("                uuuu **$$$$$$$$$$uuu                                             ")
print("       u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$                                    ")
print("       $$$$$$$$$$****           ***$$$$$$$$$$$*               @Viruss          ")
print("        *$$$$$*                      **$$$$**           					       ")
print("          $$$*                         $$$$*                                    ")
print("                                                                          ")
print("********************************************************************************")
d=open("d.txt","r")
output=d.readline()
os.remove("d.txt")
op=open(output,"r")
name=op.readline()
name=name.rstrip("\n")
sname=op.readline()
sname=sname.rstrip("\n")
db= op.readline()
db=db.rstrip("\n")
mb=op.readline()
mb=mb.rstrip("\n")
yb=op.readline()
yb=yb.rstrip("\n")
mob=op.readline()
mob=mob.rstrip("\n")
nm=op.readline()
nm=nm.rstrip("\n")
print("*********************************************************************************")
mn=list()
sc=["@","!","$","%","^","*","_","-"]
f=open(name+sname+".txt","w")
for words in sc:
	password=name.capitalize()+words+db+mb+"\n"
	f.write(password)
for words in sc:
	password=name.capitalize()+db+mb+words+"\n"
	f.write(password)
for words in sc:
	password=name.capitalize()+words+db+"\n"
	f.write(password)
for words in sc:
	password=name+words+db+mb+"\n"
	f.write(password)
for words in sc:
	password=nm.capitalize()+words+db+mb+"\n"
	f.write(password)
for words in sc:
	password=nm.capitalize()+words+db+"\n"
	f.write(password)
for words in sc:
	password=nm+words+db+mb+"\n"
	f.write(password)
for words in sc:
	password=name.capitalize()+words+yb+"\n"
	f.write(password)
for words in sc:
	password=name+words+yb+"\n"
	f.write(password)
for words in sc:
	password=sname.capitalize()+words+db+mb+"\n"
	f.write(password)
for words in sc:
	password=sname.capitalize()+words+yb+"\n"
	f.write(password)
for words in mob:
	mn.append(words)
abc=[name+db+"@",name+"_"+sname,sname+"_"+name,name.capitalize()+db+"@",sname+name,name+sname,name.capitalize()+sname.capitalize(),name.capitalize()+"@123",name.capitalize()+mn[6]+mn[7]+mn[8]+mn[9]]
for data in abc:
	f.write(data)
	f.write("\n")
print("check",name+sname+".txt","in file location")
f.write(mob)


f.close()