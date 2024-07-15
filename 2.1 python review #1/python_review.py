import random

temperature = []

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

even_temperature = []
odd_temperature = []

avg_temp = []

for i in range(7):
    temperature.append(random.randint(26,41))
    print(temperature)

good_days_count = 0

for i in range(7):
	if temperature[i] % 2 == 0:
		good_days_count = good_days_count+1

print("the number of good days are: ", good_days_count)


highest_temp = temperature[0]
for i in range(7):
	if highest_temp < temperature[i]:
		highest_temp = temperature[i]
		highest_day = days_of_the_week[i]
	else:
	    print(temperature[i])

print("highest temperature is: ", highest_temp)
print("highest temperature day is: ", days_of_the_week[i])

lowest_temp = temperature[0]
for i in range(7):
	if lowest_temp > temperature[i]:
		lowest_temp = temperature[i]
		lowest_day = days_of_the_week[i]
print("lowest temperature is: ", lowest_temp)
print("lowest temperature day is: ", lowest_day)

for i in range(7):
	avg_temp = sum(temperature) / 7

print("The average temperature is: ", avg_temp)
