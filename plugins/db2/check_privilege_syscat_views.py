class check_privilege_syscat_views():
	"""
	check_privilege_syscat_views:
	SYSCAT views have underlying SYSIBM tables that are also granted to PUBLIC group by
	default. Ensure that permission applied to these tables revoke access from unnecessary
	users. If the database was created using the RESTRICTIVE option, then grants to PUBLIC are
	voided.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

	TITLE    = 'Syscat Views'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT ttname FROM sysibm.systabauth WHERE tcreator='SYSCAT' AND grantee='PUBLIC'"
	
	verbose = False
	skip	= False
	result  = {}
	
	objects = {
		'AUDITPOLICIES':'The SYSCAT.AUDITPOLICIES view contains all audit policies for a database. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'AUDITUSE':'The SYSCAT.AUDITUSE view contains database audit policy for all non-database objects, such as authority, groups, roles, and users. It is recommended that the PUBLIC role be restricted from accessing this view',
		'DBAUTH':'The SYSCAT.DBAUTH view contains information on authorities granted to users or groups of users. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'COLAUTH':'The SYSCAT.COLAUTH view contains the column privileges granted to the user or a groups of users. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'EVENTS':'The SYSCAT.EVENTS view contains all events that the database is currently monitoring. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'EVENTTABLES':'The SYSCAT.EVENTTABLES view contains the name of the destination table that will receive the monitoring events. It is recommended that the PUBLIC role be restricted from accessing his view.',
		'ROUTINES':'The SYSCAT.ROUTINES view contains all user-defined routines, functions, and stored procedures in the database. It is recommended that the PUBLIC role be restricted from accessing this view',
		'INDEXAUTH':'The SYSCAT.INDEXAUTH view contains a list of users or groups that have CONTROL access on an index. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'PACKAGEAUTH':'The SYSCAT.PACKAGEAUTH view contains a list of users or groups that has EXECUTE privilege on a package. It is recommended that the PUBLIC role be restricted from accessing this view',
		'PACKAGES':'The SYSCAT.PACKAGES view contains all packages created in the database instance. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'PASSTHRUAUTH':'The SYSCAT.PASSTHRUAUTH view contains the names of user or group that havepassthrough authorization to query thedata source. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SECURITYLABELACCESS':'The SYSCAT.SECURITYLABELACCESS view contains all accounts in the database that have a security label privilege. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SECURITYLABELCOMPONENTELEMENTS':'The SYSCAT.SECURITYLABELCOMPONENTELEMENTS view contains the element value for a security label component. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SECURITYLABELCOMPONENTS':'The SYSCAT.SECURITYLABELCOMPONENTS view contains the components of a security label. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SECURITYLABELS':'The SYSCAT.SECURITYLABELS view contains all security labels within the database. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SECURITYPOLICIES':'The SYSCAT.SECURITYPOLICIES view contains all database security policies. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SECURITYPOLICYCOMPONENTRULES':'The SYSCAT.SECURITYPOLICYCOMPONENTRULES view contains the access rights for a security label component. It is recommended that the PUBLIC role be restricted from accessing this view',
		'SECURITYPOLICYEXEMPTIONS':'The SYSCAT.SECURITYPOLICYEXEMPTIONS contains the exemption on a security policy that was granted to a database account. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SURROGATEAUTHIDS':'The SYSCAT.SURROGATEAUTHIDS contains all accounts that have been granted SETSESSIONUSER privilege on a user or to PUBLIC. It is recommended that the PUBLIC role be restricted from accessing this view',
		'ROLEAUTH':'The SYSCAT.ROLEAUTH contains information on all roles and their respective grantees. It is recommended that the PUBLIC role be restricted from accessing this view',
		'ROLES':'The SYSCAT.ROLES contains all roles available in the database. It is recommended that the PUBLIC role be restricted from accessing this view',
		'ROUTINEAUTH':'The SYSCAT.ROUTINEAUTH contains a list of all users that have EXECUTE privilege on a routine (function, method, or procedure). It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SCHEMAAUTH':'The SYSCAT.SCHEMAAUTH contains a list of all users that have one or more privileges or access to a particular schema. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SCHEMATA':'The SYSCAT.SCHEMATA contains all schema names in the database. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'SEQUENCEAUTH':'The SYSCAT.SEQUENCEAUTH contains users and/or groups that have access to one or more privileges on a sequence. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'STATEMENTS':'The SYSCAT.STATEMENTS contains all SQL statements of a compiled package. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'PROCEDURES':'The SYSCAT.PROCEDURES contains all stored procedures in the database. It is recommended that the PUBLIC role be restricted from accessing this view',
		'TABAUTH':'The SYSCAT.TABAUTH contains users or groups that havebeen granted one or more privileges on a table or view. It is recommended that the PUBLIC role be restricted from accessing this view.',
		'TBSPACEAUTH':'The SYSCAT.TBSPACEAUTH contains users or groups that has been granted the USE privilege on a particular table space in the database. It is recommended that the PUBLIC role be restricted from accessing this view'
		}
	
	def do_check(self, *results):
		output = ''
		self.result['level']  = 'GREEN'
		
		for rows in results:
			for row in rows:
				if row[0] in self.objects:
					self.result['level']  = 'RED'
					output += 'SYSCAT.%s granted to PUBLIC - %s.\n\n' % (row[0], self.objects[row[0]])

					
		if 'GREEN' == self.result['level']:
			output = 'SYSCAT views not granted to PUBLIC.'
		
		self.result['output'] = output
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
