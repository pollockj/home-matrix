from flask import Flask, request
app = Flask(__name__)
from museum import Museum
from langtonant import LangtonAnt

@app.route('/', methods=['POST','GET'])
def result():
	if request.method == 'POST':
		var = request.form['var']
		print(var)
		if var == "musuem":
			print("Starting musuem...")
			m = Museum()
			m.run()
			return "Received musuem"
		elif var == "ants":
			print("Starting Langton's Ant...")
			a = LangtonAnt()
			a.run()
			return "Received ants"

	else:
		return "Hello World!"


if __name__ == '__main__':
    app.run(debug=False,host='192.168.0.35')
