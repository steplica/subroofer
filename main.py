import pygame
import sys
from pygame.locals import *
import StringIO
import math
import numpy

sounds = []
bits = 16
size = (100, 30)
loop = False
def set_up_pygame():

	bits = 16

	pygame.mixer.pre_init(44100, -bits, 2)
	
	pygame.init()
	_display_surf = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)


def get_sound(frequency, duration):
	global bits
	global size

	#this sounds totally different coming out of a laptop versus coming out of headphones
	sample_rate = 44100
	n_samples = int(round(duration*sample_rate))

	#setup our numpy array to handle 16 bit ints, which is what we set our mixer to expect with "bits" up above
	buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)
	max_sample = 2**(bits - 1) - 1

	for s in range(n_samples):
		t = float(s)/sample_rate    # time in seconds
		buf[s][0] = int(round(max_sample*math.sin(2*math.pi*frequency*t+math.pi)))        # left
		buf[s][1] = int(round(max_sample*.5*math.sin(2*math.pi*frequency*t+math.pi)))    # right
	
	sound = pygame.sndarray.make_sound(buf)
	return sound

def play_frequency(frequency, duration, pulse):
	global loop
	for s in sounds:
		if s is None:
			sounds.remove(s)
			continue
		while s.get_busy():
			pygame.time.wait(100)
		sounds.remove(s)
	
	frequency = float(frequency)
	duration = float(duration)
	
	sound = get_sound(frequency, duration)
	sounds.append(sound.play(0, 0))
	if pulse:
		sound = get_sound(frequency+math.pi/3, duration)
		sounds.append(sound.play(0, 0))
		sound = get_sound(frequency+math.pi*2/3, duration)
		sounds.append(sound.play(0, 0))
		sound = get_sound(frequency+math.pi, duration)
		sounds.append(sound.play(0, 0))

def quit_pygame():
	pygame.quit()
