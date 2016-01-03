class check_privilege_public_dangerous_packages():
	"""
	check_privilege_public_dangerous_packages
	Revoke execute privilege from PUBLIC on "dangerous" packages.
	"""
	# References:
	# http://www.red-database-security.com/wp/sentrigo_webinar.pdf
    # http://blog.opensecurityresearch.com/2012/03/top-10-oracle-steps-to-secure-oracle.html
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

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
	        'UTL_MAIL',
	        'UTL_ORAMTS',
		'DBMS_SQL',
		'DBMS_LOB',
		'DBMS_XMLGEN',
		'DBMS_AW_XML',
		'DBMS_RANDOM',
		'DBMS_OBFUSCATION_TOOLKIT',	
		'DBMS_ADVISOR',
		'DBMS_LDAP',
		'DBMS_LDAP_UTL',
		'DBMS_JOB',
		'DBMS_SCHEDULER',
		'DBMS_DDL',
		'DBMS_EPG',
	        'DBMS_CRYPTO',
	        'DBMS_JAVA',
	        'DBMS_JAVA_TEST',
	        'DBMS_BACKUP_RESTORE',
	        'DBMS_XMLQUERY',
	        'DBMS_SYS_SQL',
	        'DBMS_AQADM_SYSCALLS',
	        'DBMS_AQADM_SYS',
	        'DBMS_REPACT_SQL_UTL',
	        'DBMS_STREAMS_ADM_UTL',
	        'DBMS_STREAMS_RPC',
	        'DBMS_PRVTAQIM',
	        'DBMS_IJOB',
	        'DBMS_FILE_TRANSFER',
	        'INITJVMAUX',
		'CTXSYS.DRITHSX',
		'ORDSYS.ORD_DICOM',
		'KUPP$PROC',
		'HTTPURITYPE',
	        'LTADM',
	        'WWV_DBMS_SQL',
	        'WWV_EXECUTE_IMMEDIATE'
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

		self.SQL  = "SELECT UPPER(table_name) FROM sys.dba_tab_privs WHERE grantee='PUBLIC' AND privilege='EXECUTE' "
		self.SQL += "AND UPPER(table_name) IN ('" + "', '".join(self.dangerous_packages) + "')"
