
class check_privilege_execute_any_procedure_outln():
	"""
	check_privilege_execute_any_procedure_outln:
	Remove unneeded privileges from OUTLN.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Execute Any Procedure OUTLN'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='EXECUTE ANY PROCEDURE' AND grantee='OUTLN'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Execute Any Procedure granted to %s\n' % (row[0])

		if 'GREEN' == self.result['level']:
			output = 'Execute Any Procedure not granted to user OUTLN'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
