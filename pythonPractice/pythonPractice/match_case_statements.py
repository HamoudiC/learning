# Match-case statement (switch statement) = An alternative to using many 'elif' statements
#                                           Execute some code if a value matches a 'case'
#                                           Benefits: cleaner and syntax is more readable

def day_of_the_week(day):
    match day:
        case 1:
            return "It is sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not valid day"
        
print(day_of_the_week(1))

#better format
def is_weekend(day):
    match day:
        case "sunday" | "saturday":
            return True
        
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        
        case _:
            return False
             
print(is_weekend("Friday"))
       
        