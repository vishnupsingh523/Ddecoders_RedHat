import os
print("""\t\t\t\t\tHELLO DEAR
        \t\t\tWELCOME TO OUR TUI SYSTEM""")
print("-----------------------------------------------------------------------------")

print("""\t\tHII WHICH WORK YOU WANT TO DO CHOOSE FROM THE GIVEN OPTIONS BELOW

Press 1: To see the date
Press 2: To check cal
Press 3: conf web server
Press 4: To create user
Press 5: To delete user
Press 6: Operations on files
Press 7: To setup n/w
Press 8: To exit
Press 9: to reboot the system

\t\t\t\t\tEnter your choise : """)
ch=input()

if int(ch)==1:
	os.system("date")
elif int(ch)==2:
	os.system("cal")
elif int(ch)==3:
	os.system("yum install httpd")
elif int(ch)==4:
	print("Enter username : ", end='')
	User_name=input()
	os.system("useradd {}".format(User_name))
	print("Want to check whether user is created or not (y/n)  ",end='');
	os.system("id {}".format(User_name))
elif ch=='5':
	print("Enter username : ",end='');
	User_namei=input();
	os.system("userdel {}".format(User_namei));
	print("Want to check whether user is deleted or not (y/n)  ",end='')
	check=input()
	if check=='y':
		os.system("id {}".format(User_namei));
	else:
		print("Exit")

elif int(ch)==6:
	print("""\t\t\t\tOPERATION RELATED TO FILES
	\tPress 1 : To create folder
	\tPress 2 : To create file
	\tPress 3 : To write on the file
	\tPress 4 : To display the content in file
	\tPress 5 : To delete the file""")
	
	Press=input()
	if int(Press)==1:
		print("Enter File name : ",end=' ')
		File_name=input()
		os.system("mkdir {}".format(File_name));
		print("\n\n");
		os.system("ls");
	elif int(Press)==2:
		print("Enter File name : ",end=' ')
		File_name=input()
		os.system("mkdir {}".format(File_name));
		print("\n\n");
		os.system("ls");
	elif int(Press)==3:
		print("Enter File name : ",end=' ')
		File_name=input()
		os.system("gedit {}".format(File_name));
	elif int(Press)==4:
		print("Enter File name : ",end=' ')
		File_name=input()
		os.system("cat {}".format(File_name));
	elif int(Press)==5:
		print("Enter File name : ",end=' ')
		File_name=input()
		print("Deleting file .........");
		os.system("rm {}".format(File_name));
		print("\n\n");
		os.system("ls");
	print("DONE")
elif int(ch)==7:
	print("still nothing written in this");
elif int(ch)==8:
	os.system("exit")
elif int(ch)==9:
	print("Rebooting the system........")
	os.system("reboot");
elif int(ch)==10:
	print("POWERING OFF........")
	os.system("poweroff");
else:
	print("OOOOPPS!!!!!!!! Incorrect Choice")

