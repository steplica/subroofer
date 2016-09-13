import os
import sys
import main
import math
import threading
from flask import Flask,request
loopThread = None
loop = False
app = Flask(__name__)

class SoundLoop(threading.Thread):
	def __init__(self, frequency, pulse):
		super(SoundLoop, self).__init__()
		self._stop = threading.Event()
		self.frequency = frequency
		self.pulse = pulse
 
	def run(self):
		global loop
		print(self.pulse)
		while loop:
			main.play_frequency(self.frequency, 2*math.pi, self.pulse)


@app.route('/sendPost', methods=["GET", "POST"])
def send_post():
	frequency = float(request.args['frequency'])
	duration = float(request.args['duration'])
	pulse = request.args['altFreq']
	global loopThread
	global loop	

	if duration == 0:
		loop = True
		loopThread = SoundLoop(frequency, pulse == 'true')
		loopThread.start()
	else:
		loop = False
		main.play_frequency(frequency, duration, pulse == 'true')
	return ""

if __name__ == '__main__':
	try:
		main.set_up_pygame()
		app.run('steplica.student.rit.edu',port=5000, debug=True)
	finally:
		main.quit_pygame()


