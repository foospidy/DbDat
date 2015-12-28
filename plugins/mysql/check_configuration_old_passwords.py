class check_configuration_old_passwords():
	"""
	check_configuration_old_passwords
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

	TITLE    = 'Old Passwords'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SHOW GLOBAL VARIABLES LIKE 'old_passwords'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):		
		for row in rows:
			for r in row:
				if 'ON' == r[1]:
					self.result['level']  = 'RED'
					self.result['output'] = 'Old passwords is enabled.'
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Old passwords is disabled.'
			
			return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
