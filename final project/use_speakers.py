from playsound import playsound

def play(person):
	"""
	This function is used to play a sound by given meta data
	"""
	if person.gender or person.beard:
		playsound("voices/man.mp3")
	else:
		playsound("voices/woman.mp3")
	if person.glass or person.sunglass or person.beard:
		playsound("voices/with.mp3")
		playsound("voices/the.mp3")
	if person.glass:
		playsound("voices/glasses.mp3")
	elif person.sunglass:
		playsound("voices/sunglass.mp3")
	if person.beard:
		playsound("voices/beard.mp3")
	playsound("voices/pwam.mp3")