entry = int(input("Enter the number you want here : "))

start = 0
finish = entry


for entry in range(start, finish + 1):
   # all prime numbers are greater than 1
   if entry > 1:
       for numbers in range(2, entry):
           if (entry % numbers) == 0:
               break
       else:
           print(entry)