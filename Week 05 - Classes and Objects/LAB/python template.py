"""
RECORD CHECK  -  my version
===========================

Name  :  Aadarsh kumar das
Lane  :  Cyber
Date  :

Run it:   python template.py
"""

class Record:
    def __init__(self,label,value,limit):
        self.label=label
        self.value=value
        self.limit=limit

    def status(self):
        if self.value>= self.limit:
            return "OVER LIMIT"
        elif self.value >= (self.limit* 0.9):
            return "WARNING"
        else:
            return "OK"
        

records = [
                Record("Server load",85,100),
                Record("Memory usage",95,90),
                Record("Disk Space",40,100)
          ]  

print("---Quick Status Check---")
for record in records:
    print(f"Record: {record.label} -> {record.status()}")

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    # your report lines go here
    print("=" * 34)
