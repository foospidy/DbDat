
class check_configuration_audit_option_aud():
	"""
	check_configuration_audit_option_aud:
	The logging of attempts to alter the audit trail in the SYS.AUD$ table (open
	for read/update/delete/view) will provide a record of any activities that may
	indicate unauthorized attempts to access the audit trail.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Audit Options on SYS.AUD$'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT * FROM dba_obj_audit_opts WHERE object_name='AUD$' AND alt='A/A' AND aud='A/A' AND com='A/A' AND del='A/A' AND gra='A/A' AND ind='A/A' AND ins='A/A' AND loc='A/A' AND ren='A/A' AND sel='A/A' AND upd='A/A' AND fbk='A/A'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'RED'
		output                = ''

		for rows in results:
			if len(rows) > 0:
				self.result['level'] = 'GREEN'
				output = 'Auditing for AUD$ is enabled.'

		if 'RED' == self.result['level']:
			output = 'Auditing for AUD$ is not enabled.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
