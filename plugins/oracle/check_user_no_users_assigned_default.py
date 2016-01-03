class check_user_no_users_assigned_default():
	"""
	check_user_no_users_assigned_default:
	Upon creation database users are assigned to the DEFAULT profile unless otherwise specified.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Users Assigned the DEFAULT Profile'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = "SELECT username FROM sys.dba_users WHERE profile='DEFAULT' AND account_status='OPEN' AND username NOT IN ('ANONYMOUS', 'CTXSYS', 'DBSNMP', 'EXFSYS', 'LBACSYS', 'MDSYS', 'MGMT_VIEW','OLAPSYS','OWBSYS', 'ORDPLUGINS', 'ORDSYS', 'OUTLN', 'SI_INFORMTN_SCHEMA','SYS', 'SYSMAN', 'SYSTEM', 'TSMSYS', 'WK_TEST', 'WKPROXY', 'WMSYS', 'XDB', 'CISSCAN')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				if 'UNLIMITED' == row[2]:
					self.result['level'] = 'RED'
					output += 'User Assigned the DEFAULT Profile: ' + row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'No Users Assigned the DEFAULT Profile.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
