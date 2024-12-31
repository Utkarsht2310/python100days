# Make a function which print how many weeks do you have if you will live till 90 years.

def left_life(age):
    left_weeks  = (90-age) * 52
    print(f"You have {left_weeks} left...")

left_life(56)