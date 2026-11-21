# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9032-9592"

#prints character of specified number [n]
print(credit_number[0])

#prints characters from specified number to specified number
print(credit_number[0:12])   #0 isn't necessary, python will always start at 0 unless specified otherwise

#prints characters from specified num to the end of string
print(credit_number[5: ])

#prints characters from the end to start
print(credit_number[-2])    #second last number will be printed

# : -beginning ::-beginning to end ::n -count by n
print(credit_number[::2])

#prints last 4 digits
last_digits = credit_number[-4:]
print(f"Credit card: XXXX-XXXX-{last_digits}")

#print in reverse order
reverse = credit_number[::-1]
print(reverse)
