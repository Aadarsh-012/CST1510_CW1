"""
RECORD CHECK  -  my version
===========================

Name  : Aadarsh kumar das
Lane  : Cyber
Date  :

Run it:   python template.py
"""
def check_record(value,limit):
    difference=value-limit
    percent=(difference/limit)*100
    if value>limit:
       status="OVER"
    elif value< limit:
        status ="Under"
    else:
        status="Equal"
    return difference, percent , status

def print_report(label,limit,value):
    difference, percent, status =check_record(value,limit)

    print("label:",label)
    print("value:",value)
    print("limit:",limit)
    print("Differnece:",difference)
    print("percent:",round(percent,2),"%")
    print("status:",status)

def load_records(path):
    records=[]
    with open(path,"r")as file:
        for line in file:
            parts=line.strip().split(",")
            label =parts[0]
            value = float(parts[1])
            limit=float(parts[2])
            records.append({ "label":label,
                             "value":value,
                              "limit":limit
                            })
    return records

records=load_records("data.txt")

for record in records:
    print_report(record["label"],
                 record["value"],
                 record["limit"])