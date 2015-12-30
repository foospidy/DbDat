import os
import csv
import hashlib
import binascii
import helper

class check_user_weak_password():
	"""
	check_user_weak_password
	"""
	# Referecnes:
	# https://wiki.skullsecurity.org/Passwords
	# http://www.red-database-security.com/whitepaper/oracle_passwords.html
	# http://blog.red-database-security.com/2007/09/21/oracle-password-algorithm-11g-poc-code/
	# http://www.petefinnigan.com/weblog/archives/00001097.htm

	TITLE    = 'Weak Password'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL      = '' # set on init
	
	result    = {}
	appuser   = None
	dbcurs    = None
	dbversion = None
	
	def do_check(self, *results):
		output        = ''
		password_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'etc', 'check_user_weak_password.txt')
		
		for rows in results:
			for row in rows:
				if os.path.isfile(str(password_file)):
					with open(str(password_file), 'r') as passwords:
						for password in passwords:
							if int(self.dbversion) >= 11:
								# sha-1 hash
								ora_password = str(row[1])[2:]
								ora_sha1     = ora_password[:40].upper()
								ora_salt     = ora_password[40:60]
								sha_hash     = hashlib.sha1()
								
								sha_hash.update(password.strip())
								sha_hash.update(binascii.a2b_hex(ora_salt))
								
								if sha_hash.hexdigest().upper() == ora_sha1:
									self.result['level'] = 'RED'
									output += 'Weak password found for %s\n' % (row[0])
							
							else:
								# DES
								if line['hash_value'] == row[1]:
									self.result['level'] = 'RED'
									output += 'Weak password found for %s, description: %s\n' % (row[0])
		
		if 0 == len(output):
			self.result['level'] = 'GREEN'
			output += 'No weak password found.'
		
		self.result['output'] = output
		
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.appuser   = parent.appuser.upper() # upper it cuz oracle
		self.dbversion = helper.get_version(parent.dbcurs)
				
		if int(self.dbversion) >= 11:
			# sha-1 hash
			self.SQL = "SELECT name, spare4 FROM sys.user$ WHERE password IS NOT NULL AND name='" + self.appuser + "'"
		else:
			# DES
			self.SQL = "SELECT username, password FROM dba_users AND username='" + self.appuser + "'"
