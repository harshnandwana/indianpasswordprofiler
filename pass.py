import random
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
name=input("first name	>>/	")
sname=input("last name	>>/	")
db= input("date		>>/	")
mb=input("month		>>/	")
yb=input("year		>>/	")
mob=input("enter mobile number	>>/	")
nm=input("enter nickname	>>/	")
print("*********************************************************************************")
mn=list()
sc=["@","!","$","%","^","*","_","-"]
f=open(name+sname+".txt","w")
for words in sc:
	password=name.capitalize()+words+db+mb+"\n"
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