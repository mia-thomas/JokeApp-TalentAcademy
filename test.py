print("Hello User, Would you like to receive any Affirmations today?")

answer = input("Yes or No?")

if answer == 'yes' or answer == 'Yes':
    print("Great. lets get started! How many Affirmations would you like to receive today?")
    f = open("affirmations.txt","w")
    f.close()
elif answer == 'no' or answer == 'No':
    print("No Problem. See you soon")
else:
    print("I didnt catch that. I will assume you want some affirmations! How many Affirmations would you like today?")

number = int(input("Enter a Number please:"))

print(number)

file_name = "affirmations.txt"
i = 1
f = open("affirmations.txt", "a")
while i <= number :
    import requests
    websiteOutput = requests.get('https://www.affirmations.dev/')
    f.write(websiteOutput.text)
    f.write("\n")
    i += 1 
f.close()
f = open("affirmations.txt", "r")

count = len(open("affirmations.txt", "r").readlines())
print("Thank you! all your Affirmations can now be found in the file named:", file_name, "\n" "You will find", count, "affirmations waiting for you in the file", file_name,)