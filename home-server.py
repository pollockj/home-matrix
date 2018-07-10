from flask import Flask, request
app = Flask(__name__)
from museum import Museum
from langtonant import LangtonAnt
from os import fork
import signal

@app.route('/', methods=['POST','GET'])
def result():
	if request.method == 'POST':
		var = request.form['var']
		print(var)
		if var == "musuem":
			try: 
				killChild(app.pid)
			except:	
				app.pid = fork()
				if app.pid == 0:
					print("Starting musuem...")
					m = Museum()
					m.run()
				print("Spawning child {}".format(app.pid))
				return "Received musuem"
		elif var == "ants":
			try:
				killChild(app.pid)
			except:	
				app.pid = fork()
				if app.pid == 0:
					print("Starting Langton's Ant...")
					a = LangtonAnt()
					a.run()
				return "Received ants"
		elif var == "stop":
			try:
				print("killing child")
				killChild(app.pid)
			except:
				print("Nothing to kill.")
				pass
			return "Stopping matrix"
	else:
		return "Hello World!"

def killChild(pid):
	print(pid)
	if pid == -1:
		print("Killing child {}".format(pid))
		os.kill(pid,signal.SIGKILL)
		
if __name__ == '__main__':
    app.run(debug=False,host='192.168.0.35')
    app.pid = -1
