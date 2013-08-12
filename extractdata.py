#
#  Copyright Jikui Su @2013
#  Contact sujikui@gmail.com
#
from datetime import datetime
import os

# define the home and which field we need to extract
HomeFieldDict = {
"4214":['"Date & Time"', # the time of the data
        '"use [kW]"',    # the total usage of the data
   '"Total V [V]"', # the total voltage
	'"Grid [kW]"',   # phase 1 usage
	'"4214 Total Voltage [V]"', # phase 1 voltage
	'"eGauge 4211 Grid [kW]"', # phase 2 usage
	'"4211 Total Voltage [V]"', # phase 2 voltage
	]
}

# extract the data for one home from one file specified by FilePath, and field in FieldList
def ExtractOneFile(FilePath, FieldList, ResultDict):
    IsFirst = True
    IndexList = []
    #print FilePath
    for Line in open(FilePath):
        Contents = Line.split(",")
        #print(Contents)
        if (IsFirst):
	    for Field in FieldList:
		IndexList.append(Contents.index(Field))
            IsFirst = False
	    #print(IndexList)
	else:
	    ValueList = []
	    for Index in IndexList:
                Value = Contents[Index]
                if Value[0] == '-':
                    Value = Value[1:]
	        ValueList.append(Value)
	    ResultDict[ValueList[0]] = ValueList[1:]
    #print(len(ResultDict))

# extract the data for one home, specified in Dir, and field in FieldList
def ExtractData(Dir, FieldList, ResultDict):
    for Root, Dirs, Files in os.walk(Dir):
        for File in Files:
            FilePath = os.path.join(Root, File)
            ExtractOneFile(FilePath, FieldList, ResultDict)
            #return
    #print(Dir)
    #print(FieldList)

# serialize the data in dictionary into a csv file
def Serialize(ResultDict):
    Keys = ResultDict.keys()
    Keys.sort()
    OutFile = open("result.csv", "w")
    content = ','.join(HomeFieldDict['4214'])
    OutFile.write("%s\n" % content)
    for key in Keys:
        isotime = datetime.fromtimestamp(float(key)).isoformat()
        content = ','.join([isotime] + ResultDict[key])
        OutFile.write("%s\n" % content)
        #return

AbsRoot = r'/home/sujikui/research/egauge'
ResultDicts = {} # the key is homedir (aka homeid), value is one home information
for HomeDir in HomeFieldDict:
    ResultDict = {} # key is the (data & time), value is other field
    FullHomeDir = os.path.normpath(os.path.join(AbsRoot, HomeDir))
    Fiedlist = HomeFieldDict[HomeDir]
    ResultDicts["HomeDir"] = ResultDict
    ExtractData(FullHomeDir, Fiedlist, ResultDict)
    #print(len(ResultDict))
    Serialize(ResultDict)


