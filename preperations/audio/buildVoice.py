from gtts import gTTS 

#this code is used to create the voice file

text = "the"
save_at = "voices/the.mp3"

lan = 'en'

speech = gTTS(text = text, lang = lan, slow = False)

speech.save(save_at)