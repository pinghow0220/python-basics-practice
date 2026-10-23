score = int(input("Enter your score: "))
if score >= 80 and score <= 100:
    print ("Excellent")
elif score >=60 and score < 80:
    print ("Pass")
elif score >= 40 and score < 60:
    print ("Conditional Pass")
elif score < 40:
    print("Fail")

