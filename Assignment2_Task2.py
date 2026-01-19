#Sum of Integers from 1 to 50 Using a Loop

start = 1
stop = 50
total = 0
for i in range(start, stop+1):
    total = total+i

print(f"The sum of nunbers from {start} to {stop} is: {total}")