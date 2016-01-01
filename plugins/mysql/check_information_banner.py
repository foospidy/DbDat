class check_information_banner():
	"""
	check_information_banner:
    Get database banner information.
	"""
	# References:

	TITLE    = 'Database Banner'
	CATEGORY = 'Information'
	TYPE     = 'sql'
	SQL    	 = "SHOW VARIABLES LIKE '%version%'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		output               = ''
		self.result['level'] = 'GREEN'
		
		for rows in results:
			for row in rows:
				output += row[0] + ': ' + row[1] + "\n"
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
