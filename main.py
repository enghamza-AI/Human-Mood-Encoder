#Human Mood Encoder

#Take input from Users

sleep_hours = float(input("Enter sleep hours (0-12): "))
coffee_cups = float(input("Enter coffee cups (0-10): "))
work_done = float(input("work done percent (0-100): "))
social = float(input("Social interaction level (0-10): "))

#Normalize values to 0-1 scale

sleep_norm = sleep_hours / 12
coffee_norm = coffee_cups / 10
work_norm = work_done / 100
social_norm = social / 10

#Applying weights

mood_score = (
    sleep_norm * 0.35 +
    work_norm * 0.35 +
    social_norm * 0.2 -
    coffee_norm * 0.1
)

#convert to percentage
mood_score = mood_score * 100

#printing the finals

print("Your Mood Score:", round(mood_score, 2))


