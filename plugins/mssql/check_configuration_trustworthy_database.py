class check_configuration_trustworthy_database():
	"""
	check_configuration_trustworthy_database
	"""
	# References:
	# http://sqltidbits.com/scripts/check-if-xpcmdshell-enabled-across-multiple-servers

	TITLE    = 'Trustworthy Database'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name FROM sys.databases WHERE is_trustworthy_on=1 AND name != 'msdb' AND state=0"
	
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		
		self.result['level'] = 'GREEN'
		output = 'No databases with trustworthy enabled.'
		
		for row in rows:
			for r in row:
				self.result['level'] = 'RED'
				output = 'Databases with trustworthy enabled.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
