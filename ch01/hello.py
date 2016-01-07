# -*- coding: utf-8 -*-

from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		return json.dumps(request.form)
	else:
		return "<h1>Hello World!</h>"

if __name__ == "__main__":
	app.run(debug=True)
