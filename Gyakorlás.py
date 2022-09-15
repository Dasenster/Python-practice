def convert_cel_to_far(C):
    #this function will convert celsius to fahrenheit
    F = C * 9/5 + 32
    return print(f"{C:.0f} degrees C = {F:.2f} degrees F")

def convert_far_to_cel(F):
    #this function will convert fahrenheit to celsius
    C = (F - 32) * 5/9
    return print(f"{F:.0f} degrees F = {C:.2f} degrees C")

F = float(input("Please give me temperature in degrees F: "))
convert_far_to_cel(F)

C = float(input("Please give me temperature in degrees C: "))
convert_cel_to_far(C)





