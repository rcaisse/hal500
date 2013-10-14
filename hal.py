print "Hello, my name is Hal. Welcome!"
name = raw_input("Please, tell me your name. ")
title = raw_input("What do you like to be called? ")
print "Hi %s. I will not call you %s because I am an asshole." % (name, title)
print "Just kidding, %s." % title

mood = raw_input("How are you? ")
mood = mood.lower()

is_happy = False
happy_options = ["good", "not bad", "ok", "okay", "not too bad"]
for option in happy_options:
	if option in mood: 
		is_happy = True

if is_happy: 
	print "I am glad to hear that! I am in a very good mood today."
else:
	print "Oh... Well, go outside and do something fun!"

fav_turtle = raw_input("So, who is your favorite ninja turtle? ")

turtles = ["Leonardo", "Raphael", "Donatello", "Michelangelo"]

for turtle in turtles:
	first_letter = turtle[:1]
	if fav_turtle == turtle:
		print "Yeah, %s was my favorite too! " % turtle
	elif fav_turtle.startswith(first_letter): 
		print "Did you mean \"%s\"? I always liked him." % turtle

print "Goodbye!"