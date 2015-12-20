class check_configuration_remote_os_authentication():
	"""
	check_configuration_remote_os_authentication
	"""
	# References:
	# http://docs.oracle.com/cd/B19306_01/network.102/b14266/checklis.htm
	# http://www.dba-oracle.com/t_remote_os_authent.htm

	TITLE    = 'Remote OS Authentication'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT value FROM v$parameter WHERE name='remote_os_authent'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output       = ''
		for row in rows:
			if 'TRUE' == row[0][0]:
				self.result['level'] = 'RED'
				output += 'Remote OS authentication is enabled. Set remtoe_os_authent to FALSE.'
			else:
				self.result['level'] = 'GREEN'
				output += 'Remote OS authentication is disabled.'

		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
