class check_privilege_secadm():
    """
    check_privilege_secadm:
    The SECADM (security administrator) role grants the authority to create, alter
    (where applicable), and drop roles, trusted contexts, audit policies, security
    label components, security policies and security labels. It is also the authority
    required to grant and revoke oles, security labels and exemptions, and the
    SETSESSIONUSER privilege. SECADM authority has no inherent privilege to access data
    stored in tables. It is recommended thatthe secadm role be granted to authorized users
    only.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

    TITLE    = 'SECADM Role'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL         = "SELECT DISTINCT grantee, granteetype FROM syscat.dbauth WHERE securityadmauth='Y'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output = ''
        self.result['level']  = 'GREEN'

        for rows in results:
            for row in rows:
                self.result['level']  = 'YELLOW'
                output += 'SECADM granted to %s\n' % (row[0])

        if 'GREEN' == self.result['level']:
            output = 'No users granted SECADM.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
