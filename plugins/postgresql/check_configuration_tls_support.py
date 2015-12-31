class check_configuration_tls_support():
	"""
	Does the database support  SSL (TLS) connections?
	"""
	# References:

	TITLE    = 'SSL (TLS) Support'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SHOW ssl"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):		
		for rows in results:
			for row in rows:
				if 'on' != row[0]:
					self.result['level']  = 'YELLOW'
					self.result['output'] = 'SSL (TLS) is not supported by this database server.'
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'SSL (TLS) is supported by this database server.'

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
