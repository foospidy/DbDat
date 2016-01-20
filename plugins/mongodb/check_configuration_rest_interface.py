import helper

class check_configuration_rest_interface():
	"""
	check_configuration_rest_interface:
	The monogdb REST interface is not recommended for production. It does not support
	any authentication. It is turned off by default. If you have turned it on using
	the "rest" configuration option you should turn it off for production systems.
    
    MongoDB versions under 2.6: check the "rest" configuration option
    MongoDB versions 2.6 and above, check the net.http.RESTInterfaceEnabled option
	"""
	# References:
	# http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/
	# https://docs.mongodb.org/v2.4/reference/configuration-options/#rest
	# https://docs.mongodb.org/manual/reference/configuration-options/#net.http.RESTInterfaceEnabled

	TITLE    = 'REST Interface'
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
			option = 'rest'
			value  = helper.get_config_value(configuration_file, option)

			if None == value:
				self.result['level']  = 'YELLOW'
				self.result['output'] = '%s setting not found.' % (option)
			elif 'false' == value.lower():
				self.result['level']  = 'GREEN'
				self.result['output'] = '%s interface is (%s) enabled.' % (option, value)
			else: 
				self.result['level']  = 'RED'
				self.result['output'] = '%s interface is (%s) not enabled.' % (option, value)
		else:
			option = 'net.http.RESTInterfaceEnabled'
			value  = helper.get_yaml_config_value(configuration_file, option)
			
			if None == value:
				self.result['level']  = 'GREEN'
				self.result['output'] = '%s is (not found, default is False) not enabled.' % (option)
			elif False == value:
				self.result['level']  = 'GREEN'
				self.result['output'] = '%s is (%s) not enabled.' % (option, value)
			else: 
				self.result['level']  = 'RED'
				self.result['output'] = '%s is (%s) enabled.' % (option, value)
		
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)

		self.verbose = parent.verbose
		self.db      = parent.db
