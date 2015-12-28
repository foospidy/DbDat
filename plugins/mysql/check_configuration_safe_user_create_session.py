class check_configuration_safe_user_create_session():
	"""
	check_configuration_safe_user_create_session:
    Prevent GRANT from creating a new user unless a non-empty also specified.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

	TITLE    = 'Safe User Create (Session)'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT @@session.sql_mode"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
        self.result['level']  = 'RED'
        self.result['output'] = 'Safe user create is not enabled.'
            
		for row in rows:
			for r in row:
				if 'NO_AUTO_CREATE_USER' == r[1]:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Safe user create is enabled.'
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
