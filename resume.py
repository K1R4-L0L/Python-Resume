college = input("Type  your college: ")
location = input("Type the city you currently live in: ")
education = input("Type your highest degree level: ")
profession1 = input("Type your first job: ")
profession2 = input("Type your second job (optional): ")
Interests = input("Type your favorite hobby or hobbies: ")
award1 = input("Type any awards you have recieved: ")
experience = input("Type your number of years of experience in this field: ")
level = input("Type your level of experience (i.e: intern, research, secretary): ")
qualities = input("In a brief explanation (100 words or less), explain why you decided to pursue this career field: ")
SAT = input("Enter your SAT (or ACT) highest score: ")

print (f"""College:{college}\n Current city:{location}.\n We will use this to determine which of our locations is best for you!\n   
Highest Degree:{education}\n  First Job:{profession1}\n   Second Job:{profession2}\n 
Interests: {Interests}\n   Awards:{award1}\n
Years of exp: {experience}\n  level of experience: {level}\n  why I chose this field: {qualities}""")



education = ["college-graduate", "masters degree", "bachelors degree", "four years college education", "ivy league", "liberal arts", "mid-major student"]
Interests = ["research", "accounting", "secretary", "technician", "engineer", "computer scientist", "calculus"]


score = 0
experience = int(experience);
SAT = int(SAT);
qualities = int(qualities);


if experience > 2:
    score += 1
    print("Check")

if SAT > 1450:
    score += 1
    print("Check")


qualities = ["passionate", "dedicated", "hardworking", "persistent", "dilligent"]
for qualities in input:
    if qualities >= 3:
       score += 1
       print("Check")
    else:
       pass 
       print("Check")


if Interests > 3:
    score += 1
    print("Check")

if education > 3:
    score += 1
    print("Check")


if score > 3:
    print("Congradulations, you are a possible canidate for the position!")
else:
    print("Sorry, our guidelines do not meet your contentions. Thank you for your visit!")

print("Total Score:", score)

