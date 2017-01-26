class check_privilege_os_user_java_runtime_sys():
    """
    check_privilege_os_user_java_runtime_sys:
    By default, if an OS command is executed from the Java Runtime it executes with the privileges 
    of the process owner, typically oracle on Linux or LocalSystem on Windows. It is possible to 
    set a low privileged OS user instead.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    # https://docs.oracle.com/database/121/JJDEV/chten.htm#JJDEV10300

    TITLE    = 'Ensure an OS user has been set for Java runtime for SYS'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT OS_USERNAME FROM SYS.JAVA$RUNTIME$EXEC$USER$ WHERE OWNER#=0"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'RED'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'GREEN'
                output += 'OS user for Java runtime set to ' + row[0] + '\n'

        if 'RED' == self.result['level']:
            output = 'No OS user has been set for Java runtime for SYS.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
