#rainfall_mi is a string containing the average number of inches of rainfall in Michigan.
#Code to compute the number of months that have more than 3 inches of rainfall.
#Store the result in the variable "num_rainy_months".
#No hard-code allowed.



rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
x= rainfall_mi.split(",")

num_rainy_months = 0
for n in x:
    n=float(n)  #Convert the String to float to compute the condition
    if n > 3.0:
        num_rainy_months+=1  #Increment if n>3.0

print(num_rainy_months)
