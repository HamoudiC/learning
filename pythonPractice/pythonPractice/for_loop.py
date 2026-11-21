# for loop = execute a block of code a fixed amount of times.
#            You can iterate over a range, string,sequence, etc..

#counter for loop
for x in range(1,11):
    print(x)

#reverse counter for loop
#                 start,finish,count by 2 in this example
for x in reversed(range(1,11,2)):
    print(x)
    print("HAPPY NEW YEAR")

for x in range(1,21):   #print from 1 - 21
    if x == 13:             
        continue    #continue skipped over 13
    else:
        print(x)    #keeps printing