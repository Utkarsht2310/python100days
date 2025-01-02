# Write your code here.
# Calculate the bmi using weight and height.
# def bmi(h,w):
#     return w / h*2
# bmi = bmi(1.70, 70)
#
# print(bmi)

def bmi():
    w = float(input("Enter your weight in Kg: "))
    h = float(input("Enter your height in meters: "))
    my_bmi = w/(h**2)
    print("Your BMI is :", my_bmi)

bmi()
