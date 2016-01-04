
class check_privilege_dba_():
	"""
	check_privilege_dba_:
	The Oracle database DBA_ views show all information which is relevant to
	administrative accounts.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Privileges On DBA_%'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege, table_name FROM dba_tab_privs WHERE table_name LIKE 'DBA_%' AND GRANTEE NOT IN ('APEX_030200','APPQOSSYS','AQ_ADMINISTRATOR_ROLE','CTXSYS','EXFSYS','MDSYS','OLAP_XS_ADMIN','OLAPSYS','ORDSYS','OWB$CLIENT','OWBSYS','SELECT_CATALOG_ROLE','WM_ADMIN_ROLE','WMSYS','XDBADMIN','LBACSYS','ADM_PARALLEL_EXECUTE_TASK','CISSCANROLE')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Privileges On DBA_%% (%s) granted to %s on %s\n' % (row[1], row[0], row[2])

		if 'GREEN' == self.result['level']:
			output = 'No users granted Privileges On DBA_%.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
