class check_configuration_secure_auth():
	"""
	check_configuration_secure_auth:
    Disallow authentication for accounts that have old (pre-4.1) passwords.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

	TITLE    = 'Secure Auth'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SHOW GLOBAL VARIABLES LIKE 'secure_auth'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):

		for rows in results:
			for row in rows:
				if 'ON' != row[1]:
					self.result['level']  = 'RED'
					self.result['output'] = 'Secure Auth is (%s) not enabled.' % (row[1])
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Secure Auth is (%s) enabled.' % (row[1])
			
			return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
