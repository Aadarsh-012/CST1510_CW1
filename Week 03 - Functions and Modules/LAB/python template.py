"""
RECORD CHECK  -  my version
===========================

Name  :  Aadarsh kumar das
Lane  :  Cyber 
Date  :  05/10/2026

Run it:   python template.py
"""
def status_of(percent):
    if percent>=100:
        return "OVER LIMIT"
    elif percent>= 90:
        return "WARNING"
    else:
        return "ok"

def check(value,limit):
    difference= value - limit
    percent=(value/limit)*100
    return difference,percent

label=input("enter label:");
value=float(input("enter value:"))
limit=float(input("enter limit"))

difference,percent=check(value,limit)
status=status_of(percent)

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"value:{value}")
print(f"limit:{limit}")
print(f"Difference:{difference:.2f}")

print("=" * 34)