from sys import exit

print "What's your name?"
user_name = raw_input("> ")

def capsized():
	print "This is a tragic end to your life."
	print "But better to have tragedy than boredom."
	print "As any captain, you go down with your ship."
	start()

def toblar():
	print "Ahh, a small island."
	print "A parrot swoops down on your deck."
	print "Maybe this is the right path after all."
	print "Too be continued..."
	exit()

def borneo():
	print "You're getting close to a large island."
	print "A small canoe is rowing toward you."
	print "1. Talk with the canoe.\n2. Head the other way, FAST!"
	
	next = raw_input("> ")
	
	if next == 1:
		print "You approach the canoe."
		print "It is a gang of angry savages."
		print "They mercilessly slaughter you!"
		exit()
	elif next == 2:
		print "Too slow.  The winds weren't in your favor."
		print "The canoe catches you and slaughters you."
		exit()
	else:
		print "I'm sorry, don't you know how to type?"
		next = raw_input("> ")
		print next + "My ass."
		print "You're dead!"
		start()

def west():
	print "Something out here is strange."
	print "You can't quite tell what it is."
	print "1. Go out toward open water.\n2. Head toward a reef."
	
	next = raw_input("> ")
	
	if next == 1:
		open_water()
	elif next == 2:
		print "You head toward the reef and hit a rock."
		capsized()
	

def south():
	print "Heading south, huh?  Must have a 6th sense..."
	print "You come upon a group of mermaids who block your path..."
	print "A black haired mermaid offers you a comb."
	print "A red haired mermaid tells you to follow her and you",
	print " will find Lord Blackburn's friend."
	print "1. Follow the red head\n2. Take the comb and turn around."
	
	next = raw_input("> ")
	
	if next == "1":
		print "You have been seduced."
		print "Not by a mermaid, but a darker spirit of the sea."
		print "You follow her until you do not know where you are."
		capsized()
	elif next == "2":
		print "A comb is a comb.  At least it's not the fork Ariel used."
		print "You take it and turn around."
		direction()
	else:
		print "Come on man, just use 1 or 2."
		south()
		

def east():
	print "You sail and sail.  Something is wrong."
	print "You need to decide, head North or continue."
	print "1. Continue East\n2. Head North"
	
	next = raw_input("> ")
	
	if next == "1":
		open_water()
	elif next == "2":
		toblar()
	else:
		print "1 or 2, buddy."
		east()

def north():
	print "Two islands in your view."
	print "1. Borneo\n2.Toblar\n"
	print "Which one will you sail towards?"
	
	next = raw_input("> ")
	
	if next == "1":
		borneo()
	elif next == "2":
		toblar()
	else:
		print "Man, 1 or 2.."
		north()

def direction():
	print "You are just off the main island and your crew is waiting " + user_name
	print "Which way will you go?"
	print "1. North"
	print "2. East"
	print "3. South"
	print "4. West"
	
	next = raw_input("> ")
	
	if next == "1":
		north()
	elif next == "2":
		east()
	elif next == "3":
		south()
	elif next == "4":
		west()
	else:
		print "Use the numbers 1, 2, 3, or 4."
		direction()

def open_water():
	print "Nothing but open ocean stares you in the face."
	print "The sun glistens off the water."
	print "But what is that?"
	print "A scary, deadly monster!!"
	print "What will you do???"
	
	user_choice = raw_input("> ")
	
	print "You " + user_choice
	print "That doesn't seem to help, " + user_name
	print "The monster swallows your ship and you die!!!"
	start()

def help_now():
	print "Glad you decided to help, " + user_name
	print "For you, we have a catamaran with a large crew at your disposal."
	print "Her name is the Davies.  Treat her well and you won't fail!"
	direction()
	

def stay_or_go():
	print "Are you going to stay and help, or go your merry boring way?"
	print "1. Stay and help\n2. Go merry way."
	
	next = raw_input("> ")
	
	if next == "1":
		print "You wander around a while and find the same pirate."
		print "1. Help him now?\n2. Sail away from island"
		help_now()
	elif next == "2":
		open_water()
	else:
		print "Dude, seriously.  1 or 2."
		stay_or_go()

def start():
	print 'Welcome to the Caribean, ' + user_name + '. I am Lord Blackburn.'
	print 'We have lost a dear friend.  Will you help us find him?'
	print "1. Yes\n2. No"
	
	next = raw_input("> ")
	
	if next == "1":
		print "Good man!"
		print "For you, we have a catamaran with a large crew at your disposal."
		print "Her name is the Davies.  Treat her well and you won't fail!"
		direction()
	elif next == "2":
		print '"No?!  Aye, one of those selfish pirates, ay?"'
		print "He wanders off, resentfully."
		stay_or_go()
	else:
		print "Type 1 or 2 to make selections in this game."
		start()

start()
