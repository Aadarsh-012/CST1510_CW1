"""
RECORD CHECK  -  my version
===========================

Name  : Aadarsh Das
Lane  : Cyber
Date  : 29/09/2026

Run it:   python template.py
"""
label = input("Enter name of vehicle: ")      
value = float(input("Enter the value: "))    
limit = float(input("Enter the limit: "))  

diff = limit - value  
percent = (value/ limit)* 100 

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

print()
print("=" * 34)
print(f"  RECORD CHECK  - {label}")
print("="*34)
print(f"The name of your vehicle is {label}\nweight of vehicle is {value} \nlimit of bridge is {limit}")
print(f"status {status}")
print(f"difference is {diff:>20.2f}")
print(f"percent of difference is {percent:9.2f}")
print("="*34)