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
	
	def do_check(self, *results):

		for rows in results:
			for row in rows:
				if 'DISABLED' == row[1]:
					self.result['level']  = 'YELLOW'
					self.result['output'] = 'SSL (TLS) is (%s) not not enabled.' % (row[1])
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'SSL (TLS) is (%s) enabled.' % (row[1])

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
