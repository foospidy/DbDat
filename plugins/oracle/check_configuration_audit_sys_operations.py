class check_configuration_audit_sys_operations():
	"""
	check_configuration_audit_sys_operations
	"""
	# References:

	TITLE    = 'Audit SYS Operations'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='AUDIT_SYS_OPERATIONS'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):

		for rows in results:
			for row in rows:
				if 'FALSE' == row[0]:
					self.result['level']  = 'RED'
					self.result['output'] = 'Audit of sys operations is (%s) not enabled.' % (row[0])
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Audit of sys operations is (%s) enabled. %s' % (row[0])

		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
