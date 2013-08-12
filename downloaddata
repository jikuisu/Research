#
#  Copyright Jikui Su @2013
#  Contact sujikui@gmail.com
#


from datetime import datetime
import subprocess
import shlex
import time
import os

##
# datetime.fromtimestamp(1371150600).isoformat()
# '2013-06-13T15:10:00'
##

HouseId = 4214

HouseIdList = [4214, 5072,5073, 5559]

#FileName = int(time.time()) # timestamp in UTC

##
#  S specify the data in units of minutes
#  c output data in CSV format
#  C the returned data be delta-compressed
#  n=540, the number of rows outputed.
#  the first 9 minutes data will be in seconds, so 9*60 = 540 rows
##
for HouseId in HouseIdList:
  RootDir = r"/home/sujikui/research/egauge/%d"%HouseId
	SubDir = time.strftime("%Y_%m_%d") # 2013_06_13
	path = os.path.normpath(os.path.join(RootDir, SubDir))
	os.makedirs(path, exist_ok=True)
	os.chdir(path)

	dayInyear = time.strftime("%j")  # day of thle year
	MinHourInDay = time.strftime("%H_%M") # hour and minutes in a day

	FileName = MinHourInDay
	Command =  "wget \"http://egauge%d.egaug.es/cgi-bin/egauge-show?S&c&C&n=540\" -O %s.csv"%(HouseId, FileName)
	print(Command)
	args = shlex.split(Command)
	print(args)

	# execute the command
	subprocess.Popen(args, stdout=subprocess.PIPE)






