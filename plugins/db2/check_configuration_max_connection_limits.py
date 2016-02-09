class check_configuration_max_connection_limits():
    """
    check_configuration_max_connection_limits:
    The max_connections parameter indicates the maximum number of client connections
    allowed per database partition. It is recommended that this parameter be set 
    equal to the max_coordagents parameter; the max_coordagents parameter should be
    set to 100. Ensure that dependent parameters, such as maxappls, be set less than
    the max_coordagents parameter as well.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120
    # https://www-01.ibm.com/support/knowledgecenter/SSEPGG_9.7.0/com.ibm.db2.luw.admin.config.doc/doc/r0000279.html

    TITLE    = 'Maximum Connection Limits'
    CATEGORY = 'Configuration'
    TYPE     = 'clp'
    SQL         = ''
    CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output          = ''
        match           = False
        max_coordagents = None
        
        for line in results[0].split('\n'):
            if '(MAX_COORDAGENTS)=' in line.replace(' ', '').replace('\t', ''):
                max_coordagents = line.split('=')[1].strip()
                output         += line + '\n'
                match           = True
                
                if 'AUTOMATIC(' in max_coordagents:
                    max_coordagents = max_coordagents.replace('AUTOMATIC(', '').replace(')', "")
                
                if 100 == int(max_coordagents):
                    self.result['level'] = 'GREEN'
                if 1 > int(max_coordagents):
                    self.result['level'] = 'RED'
                    output              += 'MAX_COORDAGENTS is unlimited.\n'
                else:
                    self.result['level'] = 'YELLOW'
        
        if not match:
            self.result['level'] = 'RED'
            output += 'MAX_COORDAGENTS is unlimited.\n'

        match = False
        
        for line in results[0].split('\n'):
            if '(MAX_CONNECTIONS)' in line:
                max_connections = line.split('=')[1].strip()
                output         += line + '\n'
                match           = True
                
                max_connections = max_connections.replace('AUTOMATIC(', '').replace(')', "")
                
                if 'MAX_COORDAGENTS' != str(max_connections):
                    if int(max_connections) != int(max_coordagents):
                        output += 'MAX_CONNECTIONS is not equal to MAX_COORDAGENTS.\n'

        if not match:
            output += 'MAX_COORDAGENTS is set to AUTOMATIC.\n'
        
        match = False
        
        for line in results[0].split('\n'):
            if '(MAXAPPLS)' in line:
                value   = line.split('=')[1].strip()
                output += line + '\n'
                match   = True

                #todo: this setting is regulated by max connections, but probably should do some kind of check here.

        if not match:
            output += 'MAXAPPLS is set to AUTOMATIC.\n'
        
        self.result['output'] = output
        
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
