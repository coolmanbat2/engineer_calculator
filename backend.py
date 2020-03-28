from flask import Flask, flash, redirect, jsonify, request, session, abort
from os import environ
from sympy import solve, symbols
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)
class Formulas():
    """
    Formulas interface that provides all types of engineering
    formulas in the server.
    Author: Thanusun
    Date: October 18th, 2019
    """
    def square(length, width, area):
        """
        Returns the solution given any of the two above inputs.
        NOTE: Two inputs can only be provided, one of them MUST be
        an empty string.
        Examples:
        ========================
        >>> length = 4
        >>> area = 10
        >>> width = ""
        >>> Square.formula(length, width, area)
        10/4
        >>> length = 3
        >>> width = 4
        >>> area = ""
        >>> Square.formula(length, width, area)
        12
        >>> length = ""
        >>> width = 4
        >>> area = 8
        >>> Square.formula(length, width, area)
        2
        Author: Thanusun
        Date: October 20th, 2019
        """
        # Finds which variable must be solved.
        if not length:
            # if length is blank, then a formula is made in terms of length.
            length = symbols('l')
            formula = length*width
            formula = solve(area-formula, length)[0]
        elif not width:
            # otherwise, if width is length; then make a formula in terms of width
            width = symbols('w')
            formula = length*width
            formula = solve(area-formula, width)[0]
        elif not area:
            formula = length*width
        return formula

    def springConstant(K, F, X, X_0):
        if not K:
            formula = F/(X-X_0)
        elif not F:
            F = symbols('f');
            formula = F/(X-X_0)
            formula = solve(K-formula, F)[0]
        elif not X:
            X = symbols('X')
            formula = F/(X-X_0)
            formula = solve(K-formula, X)[0]
        elif not X_0:
            X_0 = symbols('G')
            formula = F/(X-X_0)
            formula = solve(K-formula, X_0)[0]
        return formula

@app.route("/")
def index():
    return render_template("Hello world! Click here <a href=\"/rectangle\">Here</a>")

@app.route('/rectangle', methods=['GET', 'POST'])
def rectangleArea():
    """
    Returns the JSON object that contains the
    area of a rectangle.
    NOTE: This function can only be called via "fetch".
    Examples:
    =========================

    """
    length = ""
    width = ""
    areaValue = ""
    solution = ""
    if request.method == 'POST':
        data = request.get_json()
        length = data['length']
        length = None if length == "" else int(length)
        width = data['width']
        width = None if width == "" else int(width)
        areaValue = data['area']
        areaValue = None if areaValue == "" else int(areaValue)
        solution = Formulas.square(length, width, areaValue)
        solution = float(round(solution, 2))
    return jsonify(solution)

@app.route('/sc', methods=['GET', 'POST'])
def scArea():
    K = ""
    F = ""
    X = ""
    X_0 = ""
    solution = ""
    if request.method == 'POST':
        data = request.get_json()
        K = data['sc']
        K = None if K == "" else int(K)
        F = data['force']
        F = None if F == "" else int(F)
        X = data['distE']
        X = None if X == "" else int(X)
        X_0 = data['sprE']
        X_0 = "" if X_0 == "" else int(X_0)
        solution = Formulas.springConstant(K, F, X, X_0)
        solution = float(round(solution, 2))
    return jsonify(solution)

if __name__ == "__main__":
    app.listen(process.env.PORT || 5000);
