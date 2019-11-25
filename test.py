from flask import Flask, flash, redirect, render_template, request, session, abort
from sympy import *

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
    def getInputs():
        return FormulaInterface.numInputs
    def getOutputs():
        return FormulaInterface.numOutputs
    def formula(length, width, Area):
        formula = int(length)*int(width)
        # Finds which variable must be solved.
        if not length:
            # uses the variable to make a symbol, then
            # creates a formula corresponding to it.
            length = symbols('l')
            formula = solve(Area-formula, width)
        elif not width:
            width = symbols('w')
            formula = solve(Area-formula, length)
        elif not Area:
            formula = int(length)*int(width)
        return formula


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
    area = ""
    if request.method == 'POST':
        length = request.form['length']
        width = request.form['width']
        area = request.form['areaValue']
        areaValue = Square.formula(length, width, area)

    return render_template('mathcalc.html', areaValue=areaValue,
											length=length,
											width=width)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
