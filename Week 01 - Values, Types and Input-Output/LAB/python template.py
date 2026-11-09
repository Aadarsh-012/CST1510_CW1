"""
RECORD CHECK  -  my version
===========================

Name  :  Aadarsh kumar das
Lane  :  Cybersecurity
Date  :  22-09-26

Run it:   python template.py
"""
label = input("Enter a source IP:")
first = float(input("Enter Failed login:"))
second =float(input("Enter Total login:"))

diff = second - first
percent = (first / second) *100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {first:10.2f}")
print("=" * 34)
print()
print(f"your failed login is {first:>16.2f}")
print(f"your total login is {second:>17.2f}")
print(f"your difference is {diff:>+18.2f}")
print(f"your percentage is {percent:>19.2f}%")
print(f"your server percent is {percent:>15.2f}%")
print()
print("=" * 34)