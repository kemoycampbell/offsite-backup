from configparser import ConfigParser
import os
class Config(object):



	def __init__(self):

		self.production_server_enable = None
		self.production_server_hostname = None
		self.production_server_port = None
		self.production_server_username = None
		self.production_server_password  = None
		self.production_server_timeout = None

		self.production_database_enable = None
		self.productin_database_hostname = None
		self.production_database_port = None
		self.production_database_username = None
		self.production_database_password  = None
		self.production_database_timeout = None

		self.sandbox_server_enable = None
		self.sandbox_server_hostname = None
		self.sandbox_server_port = None
		self.sandbox_server_username = None
		self.sandbox_server_password  = None
		self.sandbox_server_timeout = None

		self.log_enable = None
		self.log_name = None
		self.log_size_limit = None
		self.log_file_limit = None

		self.allowNoPasswordDatabase = True


	# convert human sizes to bytes
	def convert_bytes(self,byts):
	    try:
	        byts = byts.lower()
	        if byts.endswith('kb'):
	            return int(byts[0:-2]) * 1024
	        elif byts.endswith('mb'):
	            return int(byts[0:-2]) * 1024 * 1024
	        elif byts.endswith('gb'):
	            return int(byts[0:-2]) * 1024 * 1024 * 1024
	        
	        # for anything else... just throw an exception, we care zero
	        raise IOError('Invalid input. Correct format: #kb/#mb/#gb like 10gb or 5mb')
	        
	    except Exception as error:
	        raise Exception('Invalid input. Correct format: #kb/#mb/#gb like 10gb or 5mb. An error ' +
	                        repr(error) + ' occurred.')



	def configure(self):
		#ensure that the config file exist
		curr_dir = os.path.dirname(os.path.abspath(__file__))
		config_file = curr_dir+"/config.ini"

		#ensure config file not missing
		if not os.path.isfile(config_file):
			raise Exception("Config.ini file missing!")

		
		#all is cood so we will continue parsing
		config = ConfigParser()
		if not config.read(config_file):
			raise IOError("Could not read the config file ",config_file)

		#ections = config.sections()

		#configure the production
		self.configure_production_server(config)

		self.configure_production_database(config)

		self.configure_sandbox_server(config)

	def allowNoPasswordDatabase(boolean):
		elf.allowNoPasswordDatabase = boolean


	def configure_production_server(self,config):

		try:
			server = config['Production_server']
		except:
			raise KeyError("[Production_server] and its related data might be missing from config.ini")
		
		self.production_server_enable = self.__toBoolean(self.config_get(server,'enable'))
		self.production_server_hostname = self.config_get(server,'hostname');
		self.production_server_port = self.config_get(server,'port')
		self.production_server_username = self.config_get(server,'username')
		self.production_server_password = self.config_get(server,'password')
		self.production_server_timeout = self.config_get(server,'timeout')

		self.__checkProductionSetup()



	def configure_production_database(self,config):

		try:
			server = config['Production_database_server']
		except:
			raise KeyError("[Production_database_server] and its related data might be missing from config.ini")

		self.production_database_enable = self.__toBoolean(self.config_get(server,'enable'))
		self.production_database_hostname = self.config_get(server,'hostname')
		self.production_database_port = self.config_get(server,'port')
		self.production_database_username = self.config_get(server,'username')
		self.production_database_password = self.config_get(server,'password')
		self.production_database_timeout = self.config_get(server,'timeout')

		self.__checkProductionDatabaseSetup()

	def config_get(self,array,value):
		return self.strip_quotes(array.get(value))


	def configure_sandbox_server(self,config):

		try:
			server = config['Sandbox_server']
		except:
			raise KeyError("[Sandbox_server] and its related data might be missing from config.ini")
		
		self.sandbox_server_enable = self.__toBoolean(self.config_get(server,'enable'))
		self.sandbox_server_hostname = self.config_get(server,'hostname')
		self.sandbox_server_port = self.config_get(server,'port')
		self.sandbox_server_username = self.config_get(server,'username')
		self.sandbox_server_password = self.config_get(server,'password')
		self.sandbox_server_timeout = self.config_get(server,'timeout')

		self.__checkSandboxDatabaseSetup()


	def strip_quotes(self,s):
		single_quote = "'"
		double_quote = '"'

		if s.startswith(single_quote) and s.endswith(single_quote):
			s = s.strip(single_quote)
		elif s.startswith(double_quote) and s.endswith(double_quote):
			s = s.strip(double_quote)

		return s

	def __toBoolean(self,string):
		
		string = string.lower()
		if string == "true":
			return True
		elif string=="false":
			return False

		raise ValueError("string passed to __toBoolean can only be one of those {True,true,False,false}")


	def __checkProductionSetup(self):
		if self.production_server_enable == True:
			print("Checking production server configuration....")
			print("------------------------------------------")
			print("Production server backup enabled")
			if self.production_server_hostname:
				print("production server hostname OK")
			else:
				print("production server hostname invalid")
			if self.production_server_port:
				try:
					self.production_server_port = int(self.production_server_port)
					print("production server port ok")
				except:
					print("Production server port invalid")
			else:
				print("Production server port invalid")

			if self.production_server_username:
				print("Production server username ok")
			else:
				print("Production server username invalid")

			if self.production_server_password:
				print("Production server password ok")
			else:
				print("Production server password invalid")

			if self.production_server_timeout:
				print("Production server timeout ok")
			else:
				print("Production server timeout invalid")

	def __checkProductionDatabaseSetup(self):
		if self.production_database_enable == True:
			print("\nChecking production database server configuration....")
			print("------------------------------------------")
			print("Production database server backup enabled")
			if self.production_database_hostname:
				print("production database server hostname OK")
			else:
				print("production database server hostname invalid")
			if self.production_database_port:
				try:
					self.production_database_port = int(self.production_database_port)
					print("production database server port ok")
				except:
					print("Production database server port invalid")
			else:
				print("Production database server port invalid")

			if self.production_database_username:
				print("Production database server username ok")
			else:
				print("Production database server username invalid")

			if self.production_database_password:
				print("Production database server password ok")
			else:
				if self.allowNoPasswordDatabase==False:
					print("Production server password invalid")

			if self.production_database_timeout:
				print("Production database server timeout ok")
			else:
				print("Production database server timeout invalid")

	def __checkSandboxDatabaseSetup(self):
		if self.sandbox_server_enable == True:
			print("\nChecking sandbox server configuration....")
			print("------------------------------------------")
			print("Sandbox server backup enabled")
			if self.sandbox_server_hostname:
				print("Sandbox server hostname OK")
			else:
				print("Sandbox server hostname invalid")
			if self.sandbox_server_port:
				try:
					self.sandbox_server_port = int(self.sandbox_server_port)
					print("Sandbox server port ok")
				except:
					print("Sandbox server port invalid")
			else:
				print("Sandbox server port invalid")

			if self.sandbox_server_username:
				print("Sandbox server username ok")
			else:
				print("Sandbox server username invalid")

			if self.sandbox_server_password:
				print("Sandbox server password ok")
			else:
				print("Sandbox password invalid")

			if self.sandbox_server_timeout:
				print("Sandbox server timeout ok")
			else:
				print("Sandbox server timeout invalid")












