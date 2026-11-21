# Logical operatores = evaluate multiple conditions (or,and, not)
#                      or = at least one condition must be TRUE
#                      and  = both conditions must be TRUE
#                      not = inverts the condition (not TRUE, not FALSE)


#or
temp = 12
is_raining = False

if temp > 12 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")

else:
    print("The outdoor event is still scheduled.")

#and
temp = 25
is_sunny = True

if temp >= 25 and is_sunny:
    print("It is hot outside 🥵")
    print("It is SUNNY ☀️")

elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")

elif 20 >= temp and is_sunny:
    print("It is WARM outside.")
    print("It is SUNNY ☀️")

#not
temp = 25
is_sunny = True

if temp >= 25 and not is_sunny:
    print("It is hot outside 🥵")
    print("It is NOT SUNNY 🌥️")

elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁️")

elif 20 >= temp and not is_sunny:
    print("It is WARM outside.")
    print("It is a little SUNNY ⛅")
    
