class check_user_sys_system_lock():
	"""
	check_user_sys_system_lock
	Check that sys and system are locked.
	"""
	# References:
	# http://docs.oracle.com/cd/B19306_01/network.102/b14266/checklis.htm

	TITLE       = 'SYS and SYSTEM Locked'
	CATEGORY    = 'User'
	TYPE        = 'sql'
	SQL    		= "SELECT username, account_status FROM dba_users WHERE UPPER(username) IN ('SYS', 'SYSTEM')"
	result      = {}
	
	def do_check(self, *results):
		output               = ''
		self.result['level'] = 'GREEN'
		
		for rows in results:
			for row in rows:
				if 'OPEN' == row[1]:
					self.result['level'] = 'RED'
					output += 'SYS and SYSTEM accounts should be locked, ' + row[0] + ' is ' + row[1] + '\n'
		
		if 'GREEN' == self.result['level']:
			output = 'SYS and SYSTEM accounts appear to be locked.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
