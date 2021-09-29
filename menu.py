import os
import getpass
password = getpass.getpass("password :")
if password != "arth" :
        print("incorrect password")
        exit()
while True:
      print() 
      print("""
       press  1: To install httpd service
       press  2: To configure httpd service
       press  3: To start httpd service
       press  4: To use SCP protocol
       press  5: ifconfig
       press  6: To create file-vi
       press  7: which- to get location of the given command)
       press  8: ping - checks the connectivity
       press  9: To use man command
       press 10: To see all command prompt signals
       press 11: To remote login
       press 12: create folder/directory
       press 13: Delete folder/directory
       press 14: To add any New user
       press 15: Exit()
      """)
      print()
      print("enter your choice:" ,end='')
      p=input()
      if int(p)==1:
         os.system("yum install httpd")
      elif int(p)==2:
         os.system("clear")
         os.chdir("/var/www/html")
         name=input("enter filename:")
         os.system("gedit {}.html".format(name))
      elif int(p)==3:
         os.system("clear")
         os.system("systemctl start httpd")
         os.system("systemctl stop firewalld")
         ip=input("Please enter your IP Address:")
         os.system("firefox http://{}/{}.html".format(ip,name))
      elif int(p)==4:
         os.system("clear")
         filename=input("Enter File Name You Want Sent:")
         ipadd=input("Enter Destination IP")
         da=input("enter destination location")
         os.system("scp {} {}:/{}".format(filename,ipadd,da))
      elif int(p)==5:
         os.system("clear")
         os.system("ifconfig")
      elif int(p)==6:
         os.system("clear")
         f=input("enter filename:")
         os.system( "vi {}".format(f))
      elif int(p)==7:
         os.system("clear")
         c=input("enter the command name:")
         os.system("which {}".format(c))
      elif int(p)==8:
         ip=input("Enter ip address")
         os.system("ping {}".format(ip))
      elif int(p)==9:
         c=input("enter the command name:")
         os.system("man {}".format(c))
      elif int(p)==10:
         os.system("stty -a")
      elif  int(p)==11:
         ip=input("Enter ip address:")
         os.system("ssh {}".format(ip))
      elif int(p)==12:
         d=input("Enter folder name")
         os.system("mkdir {}".format(d))
      elif int(p)==13:
         d=input("enter file/foldername:")
         os.system("rm {}".format(d))
      elif int(p)==14:
         u=input("Enter username:")
         os.system("useradd {}".format(u))
         os.system("passwd")
      elif int(p)==15:
         exit()
      else:
           print("invalid choice")

