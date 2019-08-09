#Create the password field for the configuration file with the proper format

from IPython.lib import passwd

pw = passwd(algorithm="sha256")
print("Copy and paste the following line in the configMap under the [settings] section:")
print("phoenix-password = " + pw)
