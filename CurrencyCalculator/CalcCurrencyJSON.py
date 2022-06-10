# Options: -n = New Records for data.json
# Documentname: CalcCurrencyJSON.py
# Description: Calculate Currency with values from JSON file/string
# Author: Loai Afify
# Created on: 29.03.2022
#########################################
# Changes:
# Created Document
# Inserted Header
# Created data.json
#########################################
# Start of Script below
#########################################
import json, sys
stop=""
f = open('data.json')
data = json.loads(f.read())
outstr="Enter corresponding number for conversion: "
for i in range(data[-1]["ID"]):
    outstr = outstr + str(data[i]["startCurr"]) + "->" + str(data[i]["goalCurr"])+ "=" + str(data[i]["ID"]) + " "
def CurrCalc():
    goalCurr=int(input(outstr))
    amount=float(input("Please enter the Amount of money to be converted: "))
    goalCurr-=1
    endAmount=(data[goalCurr]["course"])*amount
    print("Your new Amount is:", endAmount, (data[goalCurr]["goalCurr"]) )
def newRec():
    global stop
    global data
    while stop != "SAVE":
        dStartCurr=input("Enter Starting Currency for the new Record: ")
        dGoalCurr=input("Enter Goal Currency for the new Record: ")
        dCourse=float(input("Enter the conversion-course for the new Record: "))
        newRecord={
            "ID":(data[-1]["ID"]+1),
            "startCurr":dStartCurr,
            "goalCurr":dGoalCurr,
            "course":dCourse
        }
        data.append(newRecord)
        with open('data.json', 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True))
        stop=input("Do you want to save your Work and Terminate the Loop, enter 'SAVE' otherwise ENTER: ")

if len(sys.argv) > 1:
    if sys.argv[1] == "-n":
        newRec()
    else:
        print("Your Input was Invalid")
else:
    CurrCalc()
#########################################
# End of Script
