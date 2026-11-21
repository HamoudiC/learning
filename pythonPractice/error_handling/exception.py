# Exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. except, 3. finally

try:
    number = int(input("PLease input a number: "))
    print( 1 / number)

except ZeroDivisionError:
    print("You can't divide by 0 IDIOT!")

except ValueError:
    print("Enter only numbers please.")

except Exception:
    print("Something went wrong!")

finally:
    print("Do some cleanup here.")


# except Exception:
#   print("Something went wrong!")

# Catches all errors with one message but since its too broad
# it does not provide any detail on what went wrong.
# specify the exceptions and use 'Exception' as last resort
# similar to if = specific, elif = specific, elif = specific, else = Exception