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
	
	def do_check(self, *rows):		
		for row in rows:
			for r in row:
				if 'ON' != r[1]:
					self.result['level']  = 'RED'
					self.result['output'] = 'Secure Auth is disabled.'
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Secure Auth is enabled.'
			
			return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
