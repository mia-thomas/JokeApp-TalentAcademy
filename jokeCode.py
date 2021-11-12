 ##### RANDOM JOKE GENERATOR #####

 #ask user if they would like a joke
#if yes how many?
#requests.get

#Asking user if they would like Joke.
print("Hello, Would you like to hear a Joke?")

#User Input - Whether they would like to hear a Joke.
jokeRequest = input("Please type Yes or No?: ")

#depending on user input they will be asked how many jokes they want to hear,
#if they do not want to hear a joke they will get a goodbye message. else statement
#for if answer is neither yes or no. asks user to begin again.
if jokeRequest == "Yes" or jokeRequest == "yes":
    jokeNumber = int(input("How Many Jokes would you like to hear today? Please type a Number:  "))
elif jokeRequest == "No" or jokeRequest == "no":
    print("I am sorry to hear that! goodbye, see you again!")
else:
    print("Invalid Input. Please restart")


