class check_configuration_version():
    """
    check_configuration_version:
    Determine current database version.
    """
    # References:
    # http://stackoverflow.com/questions/13331621/sql-query-to-get-sql-year-version
    # http://sqlserverupdates.com

    TITLE    = 'Version Check'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL         = "select SERVERPROPERTY('productversion') UNION SELECT @@version"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        output         = ''
        PRODUCTVERSIONS = [
             ('2014', '12.0.2000.8'),
             ('2012', '11.0.2100.60'),
             ('2008R2', '10.50.1600.1'),
             ('2008', '10.0.1600.22'),
        ]
        LATEST_SP_AND_CU = {
            '2014'   : ['12.0.4100.0', '12.0.4436'], # latest SP and latest CU (SP1 and CU4)
            '2012'   : ['11.0.6020.0', '11.0.6518.0'], # latest SP and latest CU (SP3 and CU1)
            '2008R2' : ['10.50.6000', '10.50.6220.0'], # latest SP and latest GDR (SP3 and MS15-058)
            '2008'   : ['10.00.6000', '10.0.6000.29']  # latest SP and latest GDR (SP4 and MS15-058)
        }
        version_number = None
        for rows in results:
            version_number = rows[0][0]
            version_string = rows[1][0]

        version = [int(a) for a in version_number.split('.')]
        for v in PRODUCTVERSIONS:
            comp = [int(a) for a in v[1].split('.')]
            if version >= comp:
                release = v[0]
                break

        # release identified
        # GREEN if AT least latest SP + CU or GDR
        # YELLOW if AT least latest SP
        # RED if NOT latest SP
        lower, upper = LATEST_SP_AND_CU[release]

        lower_comp = [int(a) for a in lower.split('.')]
        upper_comp = [int(a) for a in upper.split('.')]


        if version_number:
            if version >= upper_comp:
                self.result['level']  = 'GREEN'
                output               += '%s recent version (upper than %s).\n' % (version, upper)
            elif version >= lower_comp:
                self.result['level']  = 'YELLOW'
                output               += '%s slightly old version (between %s and %s).\n' % (version_number, lower, upper)
            else:
                self.result['level']  = 'RED'
                output               += '%s very old version (lower than %s).\n' % (lower, version_number)

        output               += '%s\n' % (version_string)
        self.result['output'] = output + 'grrrr' + release

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
