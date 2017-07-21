V1
===

Added
=====
	-organized the project into 2 main folders : core and storage

	-core folder will contain all python scripts that perform connections and backup

	-storage folder will contain all php and local database server to store file changes info including hashes, timestamps and filenames

	- allowed user to set option whether the database required password in core/config.py

	-setup core/config.ini with all necessary fields for the servers (production server, production database and sandbox).

	-user have the option to choose which servers they want to enable by set boolean string in the core/config.ini

	-display the servers configuration checking on the terminal. This is not a successful connection to the database but rather to ensure that the necessary fields are configured properly if the server is enabled.

	-add a new attribute [connection] in the config.ini which allows user to determine the connection method such as ssh or ftp, password based authenication or private key

ToDO
======
implement ftp

