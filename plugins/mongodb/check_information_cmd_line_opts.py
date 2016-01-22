class check_information_cmd_line_opts():
	"""
	check_information_cmd_line_opts:
	Command line options used when starting MongoDB.
	"""
	# References:
	# https://docs.mongodb.org/manual/reference/command/getCmdLineOpts/#dbcmd.getCmdLineOpts

	TITLE    = 'Command Line Options'
	CATEGORY = 'Information'
	TYPE     = 'nosql'
	SQL    	 = None # SQL not needed... because this is NoSQL.

	verbose = False
	skip	= False
	result  = {}

	db      = None

	def do_check(self):
		self.result['level'] = 'GREEN'
		output          = ''
		
		try:
			dcurs   = self.db['admin']
			options = dcurs.command('getCmdLineOpts')
			
			for option in options['argv']:
				output += '%s\n' % (option)
					
			self.result['output'] = output
		except Exception as e:
			self.result['level']  = 'ORANGE'
			self.result['output'] = 'Error: %s' % (e)
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)

		self.verbose = parent.verbose
		self.db      = parent.db
