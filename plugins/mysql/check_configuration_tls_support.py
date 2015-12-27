class check_configuration_tls_support():
	"""
    check_configuration_tls_support:
	Does the database support  SSL (TLS) connections?
	"""
	# References:

	TITLE    = 'SSL (TLS) Support'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SHOW VARIABLES LIKE 'have_ssl'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):		
		for row in rows:
			for r in row:
				if 'DISABLED' == r[1]:
					self.result['level']  = 'YELLOW'
					self.result['output'] = 'SSL (TLS) is not supported by this database server.'
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'SSL (TLS) is not supported by this database server.'

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
