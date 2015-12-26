class check_configuration_version():
	"""
	check_configuration_version:
    Determine current database version.
	"""
	# References:
	# http://stackoverflow.com/questions/13331621/sql-query-to-get-sql-year-version

	TITLE    = 'Version Check'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "select SERVERPROPERTY('productversion') UNION SELECT @@version"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output         = ''
		LATEST_VERSION = '12.0.2000.8'
		version_number = None
		
		for row in rows:
			version_number = row[0][0]
			version_string = row[1][0]
		
		if version_number:
			latest = LATEST_VERSION.split('.')
			thisdb = version_number.split('.')
			
			if int(thisdb[0]) < int(latest[0]):
				self.result['level']  = 'RED'
				output               += '%s very old version.\n' % (version_number)
				
			elif int(thisdb[1]) < int(latest[1]):
				self.result['level']  = 'YELLOW'
				output               += '%s old version.\n' % (version_number)
				
			elif int(thisdb[2]) < int(latest[2]):
				self.result['level']  = 'YELLOW'
				output               += '%s slightly old version.\n' % (version_number)
			else:
				self.result['level']  = 'GREEN'
				output               += '%s recent version.\n' % (version_number)
		
		output               += '%s\n' % (version_string)
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
