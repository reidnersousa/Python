from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)


delta1 = timedelta(weeks=3, days=2, hours=24)
print(delta1)

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

