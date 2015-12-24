class check_privileges_public_role():
	"""
	check_privileges_public_role
	"""
	# References:
	# https://www.mssqltips.com/sqlservertip/1694/how-to-find-out-what-sql-server-rights-have-been-granted-to-the-public-role/

	TITLE    = 'Public Role Privileges'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT SDP.state_desc, SDP.permission_name, SSU.[name] AS \"Schema\", SSO.[name], SSO.[type] FROM sys.sysobjects SSO INNER JOIN sys.database_permissions SDP ON SSO.id = SDP.major_id INNER JOIN sys.sysusers SSU ON SSO.uid = SSU.uid ORDER BY SSU.[name], SSO.[name]"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		self.result['level'] = 'GREEN'
		output = 'No privileges granted to public'
		
		for row in rows:
			self.result['level'] = 'Yellow'
			output = 'Privileges granted to public'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
