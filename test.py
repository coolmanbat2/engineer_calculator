from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
# app = Flask(__name__,template_folder='E:\Programming\Python Projects\Flask')
def index():
    return "Flask App!"
	
# Area of a Square formula.
def areaOfSquareFormula(length, width): 
	return int(length)*int(width)
	
	
# Finds the area, then posts it on the page. 
@app.route('/areasquare/', methods=['GET', 'POST'])
def areas(): 
	
	areaValue = ""
	length = ""
	width = ""
	if request.method == 'POST': 
		length = request.form['length']
		width = request.form['width']
		areaValue = areaOfSquareFormula(length, width)
		
	return render_template('mathcalc.html', areaValue=areaValue, 
											length=length, 
											width=width)

	
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
	
	