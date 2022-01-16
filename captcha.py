# Import the captcha modules for image captcha
from captcha.image import ImageCaptcha
# Create an image instance of the gicen size
image = ImageCaptcha(width = 280, height = 90)
# Image captcha text
text = 'Iterathon'
# generate the image of the given text
data = image.generate(text)
# write the image on the given file and save it
image.write(text, 'CAPTCHA.png')

#code for same but audio captcha
# Import the following modules for audio
from captcha.audio import AudioCaptcha
 
# Create an audio instance
audio = AudioCaptcha() 
 
# Audio captcha text
captcha_text = "5454"
 
# generate the audio of the given text
audio_data = audio.generate(captcha_text)
 
# Give the name of the audio file
audio_file = "audio"+captcha_text+'.wav'
 
# Finally write the audio file and save it
audio.write(captcha_text, audio_file)
