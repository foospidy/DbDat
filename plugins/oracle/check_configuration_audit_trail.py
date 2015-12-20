class check_configuration_audit_trail():
	"""
	check_configuration_audit_trail
	"""
	# References:

	TITLE    = 'Audit Trail'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT value FROM v$parameter WHERE name='audit_trail'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output       = ''
		for row in rows:
			if 'NONE' == row[0][0]:
				self.result['level'] = 'RED'
				output += 'No audit trail enabled.'
			else:
				output += 'Audit trial set to: ' + row[0][0]
				self.result['level'] = 'GREEN'

		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
