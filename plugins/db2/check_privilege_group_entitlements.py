import subprocess

class check_privilege_group_entitlements():
	"""
	check_privilege_group_entitlements:
	Only authorized users should be added to SYSADM_GROUP, SYSCTRL_GROUP, SYSMAINT_GROUP, or SYSMON_GROUP.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

	TITLE    = 'Group Entitlements'
	CATEGORY = 'Privilege'
	TYPE     = 'clp'
	SQL    	 = ''
	CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']
	
	verbose = False
	skip	= False
	result  = {}
	
	groups  = {
		'SYSADM_GROUP': 'The sysadm_group parameter defines the system administrator group with SYSADM authority for the DB2 instance. Accounts with this authority possess the highest level of authority within the database manager (ie, stopping/starting services, backup/recovery, and maintenance) and controls all database objects (ie, data, system objects and privileges). It is recommended that the sysadm_group group contains authorized users only.',
		'SYSCTRL_GROUP': 'The sysctrl_group parameter defines the system administrator group with system control (SYSCTRL) authority. It is recommended thatthe sysctrl_group group contains authorized users only.',
		'SYSMAINT_GROUP': 'The sysmaint_group parameter defines the system administrator group that possess the system maintenance (SYSMAINT) authority. It is recommended that sysmaint_group group contains authorized users only.',
		'SYSMON_GROUP': 'The sysmon_group parameter defines the operating system groups with system monitor (SYSMON) authority. It is recommended that sysmon_group group contains authorized users only.'
		}
	
	
	def do_check(self, *results):
		self.result['level'] = 'YELLOW'
		output = ''
		
		for group in self.groups:
			for line in results[0].split('\n'):
				if group in line:
					output += '%s\n\n%s is set to %s\n\n' % (self.groups[group], group, line.split('=')[1].strip())
		
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
