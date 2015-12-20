class check_configuration_dictionary_accessibility():
	"""
	check_configuration_dictionary_accessibility
	"""
	# References:
	# http://docs.oracle.com/cd/B19306_01/network.102/b14266/checklis.htm

	TITLE    = 'Dictionary Protection'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT value FROM v$parameter WHERE name='O7_DICTIONARY_ACCESSIBILITY'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output       = ''
		for row in rows:
			if 'TRUE' == row[0][0]:
				self.result['level'] = 'RED'
				output += 'Enable data dictionary protection. Set O7_DICTIONARY_ACCESSIBILITY to FALSE.'
			else:
				self.result['level'] = 'GREEN'
				output += 'Data dictionary protection is enabled'

		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
