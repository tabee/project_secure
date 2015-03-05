import subprocess

def scanNetwork():
	subprocess.call('./writeDevicesFile.sh', shell=True) # warum geht ned?

def isAtHome():
	f = open("devices.txt")

	for line in iter(f):
		if "2c:29:97:8e:8d:bc" in line: return 1
	f.close()




scanNetwork()
print "Is MAC address available: " , isAtHome() 




