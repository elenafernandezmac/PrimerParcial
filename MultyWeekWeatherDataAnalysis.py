import numpy as np
#temperature lists for each week
first_weeks = [22,24,19,21,25,23,20]
second_weeks = [20,22,21,23,24,22,21]
third_weeks = [23,21,20,22,24,25,23]

#calculate the average temperature for each week
first_average = sum(first_weeks)/7
second_average = sum(second_weeks)/7
third_average = sum(third_weeks)/7

#sort from hottest to coldest day and assign a function to the first one in each week
first_sorted = sorted(first_weeks)
first_hot = first_sorted[0]

second_sorted = sorted(second_weeks)
second_hot = second_sorted[0]

third_sorted = sorted(third_weeks)
third_hot = third_sorted[0]

# Find mild weeksç
#Find coldest temperature by reversing the hottest to coldest
first_reversed = reversed(first_sorted)
first_cold = next(first_reversed)
second_reversed = reversed(second_sorted)
second_cold = next(second_reversed)
third_reversed = reversed(third_sorted)
third_cold = next(third_reversed)


#get temperature fluctuation (6 values)
first_fluctuation = []
for i in range(1, len(first_weeks)):
    fluctuation = first_weeks[i] - first_weeks[i-1]
    first_fluctuation.append(fluctuation)

second_fluctuation = []
for i in range(1, len(second_weeks)):
    fluctuation2 = second_weeks[i] - second_weeks[i-1]
    second_fluctuation.append(fluctuation2)

third_fluctuation = []
for i in range(1, len(third_weeks)):
    fluctuation3 = third_weeks[i] - third_weeks[i-1]
    third_fluctuation.append(fluctuation3)


#print average, high
print(f"The average temperature was of {first_average} in the first week, {second_average} in the second and {third_average} in the third")
print(f"The highest temperature of each week was of {first_hot}, {second_hot} and {third_hot} respectively")

#print if hottest <=25 and coldest >=20
if first_hot<=25 and first_cold>=20:
    print("The firstweek had mild temperatures")

if second_hot<=25 and second_cold>=20:
    print("The second week had mild temperatures")

if third_hot<=25 and third_cold>=20:
    print("The third week had mild temperatures")

#print fluctuation
print(f"The temperature fluctuation in the first week was {first_fluctuation}, in week two was {second_fluctuation} and in third week was {third_fluctuation}")