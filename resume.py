college = input("Type  your college: N/a or college name ")
location = input("Type the state you currently live in (respond with state acronyms): ")
languages = input("Type the languages you speak (put eng for only english): ")
degree = input("Type your highest degree level: ")
profession1 = input("Type your first job: ")
profession2 = input("Type your second job (optional): ")
interest1 = input("Type your favorite hobby: ")
interest2 = input("Type your other hobby(ies) (optional): ")
award1 = input("Type any awards you have recieved: ")
experience = input("Type your number of years of experience in this field: ")
level = input("Type your level of experience (i.e: intern, research, secretary): ")
reason = input("In a brief explanation (100 words or less), explain why you decided to pursue this career field: ")
SAT = input("Enter your SAT (or ACT converted) highest score: ")
points = 0; 

print (f"""College:{college}\n Current city:{location}.\n We will use this to determine which of our locations is best for you!\n   
Highest Degree:{degree}\n  First Job:{profession1}\n   Second Job:{profession2}\n  Language:{languages}\n 
Interests: {interest1} and {interest2}\n   Awards:{award1}\n
Years of exp: {experience}\n  level of experience: {level}\n  why I chose this field: {reason}""")


SAT = int(SAT);        #SAT score check: greater than 1400 earns a point
if SAT > 1400:
    score += 1
else: 
    score =+ 0

experience = int(experience);            #experience score: 2y or more earns a point
if experience >= 2:
    score += 1
else: 
    score =+ 0


if input(college) == ["N/a"]: ## if the college, then resume should not be pushed up for recomendations 
    points -= 1; 

if input(location) == ["NM", "OK", "LA", "WV", "AK"]: #States ranked worst education worst 5
    points -= 1
elif input(location) == ["FL", "UT", "MA", "NJ","CO"]: # top 5 best rated
    points += 2
else:
    points += 1 #any other state or country

if input(languages) == ["eng"]:
    points =+ 0
else:
    points += 1
print(points)




