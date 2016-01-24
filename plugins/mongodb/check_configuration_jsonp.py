import helper

class check_configuration_jsonp():
	"""
	check_configuration_jsonp:

	Set to true to permit JSONP access via an HTTP interface. Consider the security 
    implications of allowing this activity before setting this option.

	The jsonp configuration option in versions <=2.6.
	The net.http.JSONPEnabled configuration option in versions >2.6
	"""
	# References:
	# https://docs.mongodb.org/v2.4/reference/configuration-options/#jsonp
	# https://docs.mongodb.org/v2.6/reference/configuration-options/#net.http.JSONPEnabled

	TITLE    = 'JSONP Enabled'
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
			option = 'jsonp'
			value  = helper.get_config_value(configuration_file, option)
			
			if None == value:
				self.result['level']  = 'GREEN'
				self.result['output'] = '%s is (not found) not enabled.' % (option)
			elif 'false' == value.lower():
				self.result['level']  = 'GREEN'
				self.result['output'] = '%s is (%s) not enabled.' % (option, value)
			else: 
				self.result['level']  = 'RED'
				self.result['output'] = '%s is (%s) enabled.' % (option, value)
			
		else:
			option = 'net.http.JSONPEnabled'
			value = helper.get_yaml_config_value(configuration_file, option)
			
			if None == value:
				self.result['level']  = 'GREEN'
				self.result['output'] = '%s is (not found) not enabled.' % (option)
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
