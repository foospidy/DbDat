class check_configuration_version():
	"""
	check_configuration_version
	Get the Oracle database version number and compare it to 
	the latest known published version.
	"""
	# References:

	TITLE    = 'Version Check'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT * FROM v$version"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		output       = ''
		ver_database = None
		ver_plsql    = None
		ver_core     = None
		ver_tns      = None
		ver_nlsrtl   = None
		LATEST_VERSION = '12.1.1'
		
		for rows in results:
			ver_database = rows[0][0]
			ver_plsql    = rows[1][0]
			ver_core     = rows[2][0]
			ver_tns      = rows[3][0]
			ver_nlsrtl   = rows[4][0]
		
		if ver_database:
			thisdb = ver_database.split()
		
			# check for non-production release
			if 'Production' != thisdb[-1].strip():
				self.result['level']  = 'RED'
				output                = 'Non-production release: %s\n' % (ver_database)
		
			# check for old version
			latest  = LATEST_VERSION.split('.')
			current = thisdb[-3].split('.')
			
			if int(current[0]) < int(latest[0]):
				self.result['level']  = 'RED'
				output               += '%s very old version.\n' % (thisdb[-3])
			
			elif int(current[1]) < int(latest[1]):
				self.result['level']  = 'YELLOW'
				output               += '%s old version.\b' % (thisdb[-3])
				
			elif int(current[2]) < int(latest[2]):
				self.result['level']  = 'YELLOW'
				output               += '%s slightly old version.\n' % (thisdb[-3])
			else:
				output += '%s recent version.\n' % (thisdb[-3])
			
			if ver_plsql:
				thisdb = ver_plsql.split()
				
				if 'Production' != thisdb[-1].strip():
					self.result['level']  = 'RED'
					output               += 'Non-production release: %s\n' % (ver_plsql)
			
			if ver_core:
				thisdb = ver_core.split()
				
				if 'Production' != thisdb[-1].strip():
					self.result['level']  = 'RED'
					output               += 'Non-production release: %s\n' % (ver_core)
			
			if ver_tns:
				thisdb = ver_tns.split()
				
				if 'Production' != thisdb[-1].strip():
					self.result['level']  = 'RED'
					output               += 'Non-production release: %s\n' % (ver_tns)
			
			if ver_nlsrtl:
				thisdb = ver_nlsrtl.split()
				
				if 'Production' != thisdb[-1].strip():
					self.result['level']  = 'RED'
					output               += 'Non-production release: %s\n' % (ver_nlsrtl)
					
			if '' == output:
				output = 'No results.'
			
			self.result['output'] = output
			
			return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
