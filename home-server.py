from flask import Flask, request
app = Flask(__name__)
from museum import Museum

@app.route('/', methods=['POST','GET'])
def result():
	if request.method == 'POST':
		var = request.form['var']
		print(var)
		if var == "musuem":
			print("Starting musuem...")
			m = Museum()
			m.run()
		return 'received'

	else:
		return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
