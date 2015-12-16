class check_information_banner():
	"""
	Get database banner
	"""
	# References:

	TITLE    = 'Database Banner'
	CATEGORY = 'Information'
	TYPE     = 'sql'
	SQL    	 = "SHOW VARIABLES LIKE '%version%'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output          = ''
		self.result['level'] = 'GREEN'
		
		for row in rows:
			for r in row:
				output = output + r[0] + ': ' + r[1] + "\n"
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
