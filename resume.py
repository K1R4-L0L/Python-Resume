college = input("Type  your college: ")
location = input("Type the city you currently live in: ")
degree = input("Type your highest degree level: ")
profession1 = input("Type your first job: ")
profession2 = input("Type your second job (optional): ")
interest1 = input("Type your favorite hobby: ")
interest2 = input("Type your other hobby(ies) (optional): ")
award1 = input("Type any awards you have recieved: ")
experience = input("Type your number of years of experience in this field: ")
level = input("Type your level of experience (i.e: intern, research, secretary): ")
reason = input("In a brief explanation (100 words or less), explain why you decided to pursue this career field: ")

print (f"""College:{college}\n Current city:{location}.\n We will use this to determine which of our locations is best for you!\n   
Highest Degree:{degree}\n  First Job:{profession1}\n   Second Job:{profession2}\n 
Interests: {interest1} and {interest2}\n   Awards:{award1}\n
Years of exp: {experience}\n  level of experience: {level}\n  why I chose this field: {reason}""")