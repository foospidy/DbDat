class check_configuration_audit_sys_operations():
	"""
	check_configuration_audit_sys_operations
	"""
	# References:

	TITLE    = 'Version Check'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT value FROM v$parameter WHERE name='audit_sys_operations'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output       = ''
		
		for row in rows:
            #todo
				
		
		
			
			self.result['output'] = output
			
			return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
