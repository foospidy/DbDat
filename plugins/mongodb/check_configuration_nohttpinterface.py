import helper

class check_configuration_nohttpinterface():
	"""
	check_configuration_nohttpinterface:
	Mongodb by default provides a http interface running by default on port 28017 which
	provides the "home" status page. This interface is not recommended for production
	use and is best disabled. Use the "nohttpinterface" configuration setting to disable
	the http interface.
	"""
	# References:
	# http://blog.mongodirector.com/10-tips-to-improve-your-mongodb-security/
	# https://docs.mongodb.org/v2.4/reference/configuration-options/#nohttpinterface
	# https://docs.mongodb.org/manual/reference/configuration-options/#net.http.enabled
	

	TITLE    = 'No HTTP Interface'
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
			option = 'nohttpinterface'
			value  = helper.get_config_value(configuration_file, option)

			if None == value:
				self.result['level']  = 'YELLOW'
				self.result['output'] = 'No HTTP Interface setting not found.'
			elif 'true' == value.lower():
				self.result['level']  = 'GREEN'
				self.result['output'] = 'No HTTP Interface is (%s) enabled.' % (value)
			else: 
				self.result['level']  = 'RED'
				self.result['output'] = 'No HTTP Interface is (%s) not enabled.' % (value)

		else:
			option = 'net.http.enabled'
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
