class check_information_banner():
	"""
	Get database banner
	"""
	# References:

	TITLE    = 'Database Banner'
	CATEGORY = 'Information'
	TYPE     = 'sql'
	SQL    	 = "SELECT VERSION()"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		output               = ''
		self.result['level'] = 'GREEN'
		
		for rows in results:
			for row in rows:
				output = output + row[0] + "\n"
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
