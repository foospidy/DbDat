import os

class check_user_weak_password():
	"""
	Accounts with weak passwords.
	"""
	# References:
	# https://wiki.skullsecurity.org/Passwords
	# http://www.ibm.com/developerworks/opensource/library/os-postgresecurity/index.html

	TITLE    = 'Weak Password'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL      = "SELECT VERSION()"
	
	verbose = False
	skip	= False
	result  = {}
	appuser = None
	dbcurs  = None
	
	def do_check(self, *rows):
		rows          = None # not using results from SQL specified above, check is based on SQL used below.
		output        = ''
		match         = False
		password_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'etc', 'check_user_weak_password.txt')

		if os.path.isfile(str(password_file)):
			with open(str(password_file), 'r') as passwords:
				for password in passwords:
					self.SQL = "SELECT 'md5' || md5('" + password.strip() + self.appuser + "') AS generated_hash, passwd AS stored_hash FROM pg_shadow WHERE usename='" + self.appuser + "'"
					self.dbcurs.execute(self.SQL)
					
					rows = self.dbcurs.fetchall()
					
					for row in rows:
						if row[0] == row[1]:
							match = True
			
			if match:
				self.result['level']  = 'RED'
				self.result['output'] = 'Weak password found!'
			else:
				self.result['level']  = 'GREEN'
				self.result['output'] = 'No weak password found.'
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.appuser = parent.appuser
		self.dbcurs  = parent.dbcurs
