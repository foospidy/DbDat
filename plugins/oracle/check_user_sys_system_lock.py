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
	SQL    		= "SELECT username, account_status FROM dba_users WHERE username IN ('SYS', 'SYSTEM')"
	result      = {}
	
	def do_check(self, *rows):
		output       = ''
		
		for row in rows:
			for r in row:
				if 'OPEN' == r[1]:
					self.result['level'] = 'RED'
					output += 'SYS and SYSTEM accounts should be locked, ' + r[0] + ' is ' + r[1] + '\n'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
