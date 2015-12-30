class check_configuration_sec_protocol_error_further_action():
	"""
	check_configuration_sec_protocol_error_further_action:
	The	SEC_PROTOCOL_ERROR_FURTHER_ACTION setting determines the Oracle server's 
	response to bad/malformed packets received from the client.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Protocol Error Further Action'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='SEC_PROTOCOL_ERROR_FURTHER_ACTION'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		
		for rows in results:
			for row in rows:
				if row[0] != 'DELAY, 3' and row[0] != 'DROP, 3':
					self.result['level']  = 'RED'
					self.result['output'] = 'SEC_PROTOCOL_ERROR_FURTHER_ACTION is %s.' % (row[0])
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'SEC_PROTOCOL_ERROR_FURTHER_ACTION is %s.' % (row[0])
		
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
