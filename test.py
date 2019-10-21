from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

class FormulaInterface():
    """
    Formula interface that provides conveinence in creating equations
    for other developers.
    Contains number of Inputs and outputs for each formula given.
    NOTE: We are assuming that developer knows how many inputs and outputs
    exist in the formula, and they must be provided accordingly.
    Author: Thanusun
    Date: October 18th, 2019
    """
    numInputs = 0
    numOutputs = 0
    def getInputs():
        raise NotImplementedError("You Must Implement This :)")
    def getOutputs():
        raise NotImplementedError("You Must Implement This :)")
    def formula(**args):
        raise NotImplementedError("You Must Implement This :)")

# Area of a Square formula.
class Square(FormulaInterface):
    """
    Inherits FormulaInterface
    Provides formula of a Square, and contains 2 inputs with 1 output.
    Author: Thanusun
    Date: October 20th, 2019
    """
    FormulaInterface.numInputs = 2
    FormulaInterface.numOutputs = 1
    def getInputs():
        return FormulaInterface.numInputs
    def getOutputs():
        return FormulaInterface.numOutputs
    def formula(length, width):
        return int(length)*int(width)

# Homepage
@app.route("/")
def index():
    return "Click me! <br></br> <a href='/areasquare/' class='button'>Square</button>"

# Finds the area, then posts it on the page.
@app.route('/areasquare/', methods=['GET', 'POST'])
def areas():
	areaValue = ""
	length = ""
	width = ""
	if request.method == 'POST':
		length = request.form['length']
		width = request.form['width']
		areaValue = Square.formula(length, width)

	return render_template('mathcalc.html', areaValue=areaValue,
											length=length,
											width=width)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
