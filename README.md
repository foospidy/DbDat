# DbDat
**Db Database Assessment Tool**

DbDat performs numerous checks on a database to evaluate security. The categories of checks performed are configuration, privileges, users, and information. Checks are performed by running queries or reading database configuration files. The goal of this tool is to highlight issues that need immediate attention and identify configuration settings that should be reviewed for appropriateness. This tool is not for identifying SQL Injection vulnerabilities in an application, there are good tools available for that already (e.g. https://github.com/sqlmapproject). Also, this tool does not attempt to determine what CVEs may impact the version of the target database (but may do so in the future - maybe). Rather, this tool can help you better understand the potential impact of a successful SQL Injection attack due to weak configuration or access controls. A majority of the checks are from the CIS (https://cisecurity.org) Security Benchmarks for databases, so thanks to the CIS! The benchmark documents can be found here: https://benchmarks.cisecurity.org/downloads/browse/index.cfm?category=benchmarks.servers.database

I highly recommend downloading the benchmark document for your target database as it contains additional information about the checks performed.

Finally, DbDat is intended to be a framework to enable easy creation of new plugins and checks. Contributions from the security, or even database administrator, community is what will make this a great tool. The current set of checks are in no way complete, certainly more needs to be done. Please contribute!

**Developing New Database Checks**

_Pull requests are very welcome!_ Checks are organized by database type (e.g. MySQL, Oracle, MS SQL, etc.) in the plugins folder. Each check is a single python file that must have `check_` at the begining of the file name. Each file contains a class with a `do_check` method. This method is the primary logic for checks. The quick way to get started is to copy an existing check file and modify it. However, see the Developing Plugins section below for more details.

## Running DbDat

1. Be sure you have the necessary dependencies installed for Python scripts to connect to your target database. See dependencies section below.
2. Add a connection profile entry in the `etc/dbdat.conf` file for each database you want to assess.
3. Run: `python dbdat.py -p <profile name>`
4. View the report. To view the report `cd` to reports directory and run `python -m SimpleHTTPServer 9000` (or choose a port number you prefer). Then open your browser and navigate to `http://localhost:9000`.

To see a list of additional command line arguments run `python dbdat.py -h`

#### Report Output

The report organizes results by levels, which are RED, YELLOW, ORANGE, GRAY, and GREEN.

- RED - items needing immediate attention.
- YELLOW - items needing review.
- ORANGE - checks that failed to execute properly.
- GRAY - items that may not be applicable to the version of the database being assessed.
- GREEN - items that passed

## Dependencies

So far DbDat has been tested on Debian Linux, CentOS Linux, and Windows 7 with Python 2.7

##### MySQL support

Run: `pip install MySQL-python`

Or on Debian, run: `apt-get install python-mysqldb`

##### PostgreSQL support

Run: `pip install psycopg2`

##### Oracle support

Run: `pip install cx_Oracle`
- https://cx-oracle.readthedocs.org/en/latest/index.html

_Note: you will need to install Oracle client libraries for this to work._

##### MS SQL support

Run: `pip install pymssql`
- https://pymssql.readthedocs.org/en/latest/index.html

##### Sybase support
- todo

##### DB2 support

Run: `pip install ibm_db` or `easy_install ibm_db`

_Note: you will need to ensure the user running DbDat has access to execute DB2 CLP commands (e.g. db2 and db2level)._

##### MongoDB support

Run: `pip install pymongo`

To support MongoDB YAML config files run: `pip install pyyaml`

##### CouchDB support

Run: `pip install couchdb`

## Developing Plugins

### Plugin Folders

Within the plugins folder there is a folder for each type of database, and each folder contains check files. This is a very simple structure, but you can also browse the plugins folder to get familiar https://github.com/foospidy/DbDat/tree/master/plugins

The database folders will contain:
- `__init.py` - The init file has an import statement for each check file.
- `check_` files - These are the actual files performing the database checks. The file and the class defined within the file should have the same name.
- `helper.py` - A file containing common functions. Check files can import `helper.py` to leverage common functions.

### Check Files

When adding a new check file an import statement needs to be added to the corresponding plugin directory's `__init__.py` file. The code pattern for the checks are fairly consistent. Review the existing files to get a sense of how they are structured. Note the difference between checks of type sql and configuration_file.

#### Check File

There are different "types" of checks that can be defined. The check type is determined by the `TYPE` variable and can be sql, configurtion_file, nosql, or clp. Below are example implementations for the different check type scnearios.

#### sql check type

For sql checks the do_check method signature must be: `do_check(self, *results)`

##### Typical sql check

https://github.com/foospidy/DbDat/blob/master/plugins/mysql/check_user_empty_password.py

##### sql check where SQL variable is set on init

In this example we need the `appuser` variable from the calling parent class. The appuser needs to be dynamically added to the sql statement, so the `self.SQL` varaible is being set in the `__init__` method. Also, since this do_check method needs to execute the sql we need the DB cursur (connection) as well, this is set in the `__init__` method with `self.dbcurs = parent.dbcurs`.

https://github.com/foospidy/DbDat/blob/master/plugins/mysql/check_privilege_user_grants.py

#### configuration_file check type

For configuration_file checks the do_check method signature must be: `do_check(self, configuration_file)`

##### Parsing configuration files that are compliant with Python's ConfigParser module

https://github.com/foospidy/DbDat/blob/master/plugins/mysql/check_configuration_general_log.py

##### Parsing configuration files that are not compliant with Python's ConfigParser module

In this example, the PostgreSQL configuration file does not have sections (e.g. `[section_name]`), so the helper module in the PostgreSQL folder contains a function that handles this. See the `get_config_value` function defined in `helper.py`.

https://github.com/foospidy/DbDat/blob/master/plugins/postgresql/check_configuration_host_wildcards.py

For other configuration file formats you will need to define your own parsing logic.

#### nosql check type

For nosql checks the do_check method signature must be: `do_check(self)`

NoSQL queries need to be executed within the do_check method, so the class `__init__` method must implement `self.db = parent.db`. The `self.db` variable can then used to execute NoSQL queries within the do_check method.

https://github.com/foospidy/DbDat/blob/master/plugins/mongodb/check_information_banner.py

#### clp check type

For clp checks the do_check method signature must be: `do_check(self, *results)`. clp checks are needed for IBM DB2 databases so the db2 command line processor can be executed to get information about the database. However, this type of check could be used to execute any arbitrary command line command. All command line output can be parsed from the `results` variable passed to the do_check method. In addition, you will need to define the `CMD` class method. This variable is list of the command and related arguments.

https://github.com/foospidy/DbDat/blob/master/plugins/db2/check_privilege_group_entitlements.py

#### The Category Variable

Every check must have a category specified using the `CATEGORY` variable. The category is a way to organize checks. Possible categories are: Information, Configuration, Privilege, and User. Specify the category that is most relevant to the context of the check. 

#### Outline of Check File
This is a rough example demontrate the pattern a check file should follow:

```python
# (OPTIONAL): Add import statements, include any necessary modules to support this check
import helper

# (REQUIRED): Define class, the class must have the same name as its file name.
class check_configuration_evaluate_something():

  # (REQUIRED): Add documentation, provide information on this check as this will be displayed in the report.
	"""
	check_configuration_evaluate_something:
	Some description goes here!
	"""

  # (OPTIONAL): Add references, this is only comments in code, adding references is helpful to others.
  # References:
  # https://www.percona.com/blog/2012/12/28/auditing-login-attempts-in-mysql/
  # https://dev.mysql.com/doc/refman/5.7/en/password-security-user.html

  # (REQUIRED): Add the standard set of variables 
	TITLE    = 'Client Password'
	CATEGORY = 'Configuration'
	TYPE     = 'configuration_file'
	SQL    	 = None
	
	verbose = False
	skip	= False
	result  = {}
	
	# (OPTIONAL): Add any custom variables specific to this check 
	custom_var = 'custom_val'
	
	
	# (REQUIRED): Define the do_check method, this is the actual check logic and is called by the main program.
	def do_check(self, *results):
	
		# (REQUIRED): check logic goes here, besure to set values for self.result['level'] and self.result['output']
		
		# Results from the SQL variable can be processed using:
		for rows in results:
			for row in rows:
		
			# (REQUIRED):
			# Always set the self.result['level'] and self.result['output'] variables before returning.
			if row[0] == 'bad':
				self.result['level']  = 'RED'
				self.result['output'] = 'Result is %s' % (row[0])
			elif row[0] == 'needs review':
				self.result['level']  = 'YELLOW'
				self.result['output'] = 'Result is %s' % (row[0])
			else:
				self.result['level']  = 'GREEN'
				self.result['output'] = 'Result is %s' % (row[0])
		
		# Always return self.result
		return self.result
	
	# (REQUIRED): at minimum the __init__ method should print the check being performed.
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		# get values from the parent calling class
		self.verbose = parent.verbose
```

## Other Database Security Tools

- [SQLMap](https://github.com/sqlmapproject)
- [NoSQLMap](https://github.com/tcstool/NoSQLMap)
- [Audit CouchDB](https://github.com/iriscouch/audit_couchdb)
- [MongoAudit](https://github.com/stampery/mongoaudit)
- [MSDAT](https://github.com/quentinhardy/msdat)
- [ODAT](https://github.com/quentinhardy/odat)
