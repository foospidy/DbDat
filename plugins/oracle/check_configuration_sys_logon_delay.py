class check_configuration_sys_logon_delay():
    """
    check_configuration_sys_logon_delay
    Ensure _sys_logon_delay is set to 1 or higher.
    The _sys_logon_delay hidden parameter determines the length in seconds of the delay 
    between failed logon attempts for the SYS user (and other users controlled by the password 
    file such as SYSBACKUP, SYSDG and SYSKM).
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf

    TITLE    = 'SYS Logon Delay'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL      = "SELECT c.ksppstvl FROM x$ksppi a, x$ksppsv c WHERE a.indx = c.indx AND a.ksppinm = '_sys_logon_delay'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):

        for rows in results:
            for row in rows:
                if int(row[0]) < 1:
                    self.result['level']  = 'RED'
                    self.result['output'] = 'SYS Logon Delay is (%s).' % (row[0])
                else:
                    self.result['level']  = 'GREEN'
                    self.result['output'] = 'SYS Logon Delay is (%s).' % (row[0])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
