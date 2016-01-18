import helper

class check_configuration_noscripting():
	"""
	check_configuration_noscripting:

	MongoDB supports the execution of JavaScript code for certain server-side operations: 
	mapReduce, group, eval, and $where. If you do not use these operations, disable server-side
	scripting by using:

	The --noscripting option on the command line in versions <=2.6.
	The security.javascriptEnabled configuration option in versions >2.6
	"""
	# References:
	# https://docs.mongodb.org/v2.6/MongoDB-security-guide-v2.6.pdf
	# https://docs.mongodb.org/manual/reference/configuration-options/#core-options

	TITLE    = 'No Scripting'
	CATEGORY = 'Configuration'
	TYPE     = 'configuration_file'
	SQL    	 = None # SQL not needed... because this is NoSQL.

	verbose = False
	skip	= False
	result  = {}

	db      = None

	def do_check(self, configuration_file):
		option         = None
		version_number = self.db.server_info()['versionArray']
		
		if version_number[0] <= 2 and version_number[1] < 6:
			option = 'noscripting'
			value = helper.get_config_value(configuration_file, option)
			
			if None == value:
				self.result['level']  = 'RED'
				self.result['output'] = '%s is (not found) not enabled.' % (option)
			elif 'true' != value.lower():
				self.result['level']  = 'GREEN'
				self.result['output'] = '%s is (%s) enabled.' % (option, value)
			else: 
				self.result['level']  = 'RED'
				self.result['output'] = '%s is (%s) not enabled.' % (option, value)
			
		else:
			option = 'security.javascriptEnabled'
			value = helper.get_yaml_config_value(configuration_file, option)
			
			if None == value:
				self.result['level']  = 'RED'
				self.result['output'] = '%s is (not found) enabled.' % (option)
			elif False == value:
				self.result['level']  = 'GREEN'
				self.result['output'] = '%s is (%s) not enabled.' % (option, value)
			else: 
				self.result['level']  = 'RED'
				self.result['output'] = '%s is (%s) enabled.' % (option, value)

		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)

        # db is needed to get version info
		self.db      = parent.db
		self.verbose = parent.verbose
