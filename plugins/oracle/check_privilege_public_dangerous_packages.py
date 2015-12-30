class check_privilege_public_dangerous_packages():
	"""
	check_privilege_public_dangerous_packages
	Revoke execute privilege from PUBLIC on these ojbects.
	"""
	# References:
	# http://www.red-database-security.com/wp/sentrigo_webinar.pdf
    # http://blog.opensecurityresearch.com/2012/03/top-10-oracle-steps-to-secure-oracle.html

	TITLE    = 'PUBLIC Dangerous Packages'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = '' # set in init
	
	verbose = False
	skip	= False
	result  = {}
	
	dangerous_packages = {
		'UTL_FILE',
		'UTL_HTTP',
		'UTL_INADDR',
		'UTL_SMTP',
		'UTL_TCP',
		'UTL_DBWS',
		'DBMS_SQL',
		'DBMS_LOB',
		'DBMS_XMLGEN',
		'DBMS_AW_XML',
		'DBMS_RANDOM',
		'DBMS_OBFUSCATION_TOOLKIT',	
		'dbms_advisor',
		'dbms_ldap',
		'dbms_ldap_utl',
		'dbms_job',
		'dbms_scheduler',
		'dbms_ddl',
		'dbms_epg',
		'dbms_xmlgen',
		'dbms_aw_xml',
		'CTXSYS.DRITHSX',
		'ORDSYS.ORD_DICOM',
		'KUPP$PROC',
		'HTTPURITYPE'
		}
	
	def do_check(self, *results):
		output               = ''
		self.result['level'] = 'GREEN'
		
		for rows in results:
			for row in rows:
				self.result['level'] = 'RED'
				output += row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'no PUBLIC dangerous packages found.'
		
		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)

		self.SQL  = "SELECT table_name FROM sys.dba_tab_privs WHERE grantee='PUBLIC' AND privilege='EXECUTE' "
		self.SQL += "AND table_name IN ('" + "', '".join(self.dangerous_packages) + "')"
