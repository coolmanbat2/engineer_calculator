from flask import Flask, flash, redirect, render_template, request, session, abort

class FormulaInterface():
    """
    Formula interface that provides conveinence in creating equations
    for other developers.
    Author: Thanusun
    Date: October 18th, 2019
    """
    def formula(**args):
        raise NotImplementedError("You Must Implement This :)")

# Area of a Square formula.
class Square(FormulaInterface):
    """
    Provides all the properties of a Square, including its formula.
    """
    def formula(length, width):
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
		areaValue = Square.formula(length, width)

	return render_template('mathcalc.html', areaValue=areaValue,
											length=length,
											width=width)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
