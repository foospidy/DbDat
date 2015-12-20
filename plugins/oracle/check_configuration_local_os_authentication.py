class check_configuration_local_os_authentication():
	"""
	check_configuration_local_os_authentication
	"""
	# References:
	# http://www.dba-oracle.com/security/local_os_authentication.htm

	TITLE    = 'Local OS Authentication'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT value FROM v$parameter WHERE name='os_authent_prefix'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output       = ''
		for row in rows:
			if '' != str(row[0][0]):
				self.result['level'] = 'RED'
				output += 'OS authentication prefix is not null. Set os_authent_prefix to null.'
			else:
				self.result['level'] = 'GREEN'
				output += 'OS authentication prefix is null.'

		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
