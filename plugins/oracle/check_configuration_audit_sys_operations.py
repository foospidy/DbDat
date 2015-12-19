class check_configuration_audit_sys_operations():
	"""
	check_configuration_audit_sys_operations
	"""
	# References:

	TITLE    = 'Audit SYS Operations'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT value FROM v$parameter WHERE name='audit_sys_operations'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output       = ''
		for row in rows:
			if 'FALSE' == row[0][0]:
				self.result['level'] = 'RED'
				output += 'Audit of sys operations is not enabled.'
			else:
				self.result['level'] = 'GREEN'
				output += 'Audit of sys operations is enabled.'

		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
