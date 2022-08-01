#
# #
# # #
# # # # Fast Extremums Finder
# # #
# #
#

"""
Description:

    Finds extremums in an equation based on a given interval
"""

from __future__ import annotations

from typing import List, Dict

import sympy

# from __future__ import annotations ->
# must occur at the beginning of the file, this import makes it possible to use classes as defined types before runtime (this will be the default in python 4)
# for example: source_variable: SourceClass, in the past you would need to literate it like this: source_variable: "SourceClass", or check if the class has been
# defined before trying to use it as a type

# self is used in class objects and data objects
# @staticmethod is used only in class methods which are static


# Start


def CheckEquation(EquationText: str) -> sympy.core.mul.Mul:
    """
    Description:

        Checks equation based on equation text

    Parameters:

        EquationText: the equation as a string (for example: "x^2 + 3x + 2")

    Returns:

        Returns the equation
    """

    # Start

    return sympy.sympify(EquationText.replace('^', "**").replace('x', "X"))


def RunEquation(Equation: sympy.core.mul.Mul, Variables: Dict[str, float]) -> float:
    """
    Description:

        Runs the equation based on the variables

    Parameters:

        Equation: the equation to run
        Variables: the variables to input into the equation

    Returns:

        Returns the result (typically: "Y")
    """

    # Start

    return float(Equation.evalf(subs=Variables))


def FindExtremums(Equation: sympy.core.mul.Mul, Start: float, End: float, Interval: float) -> Dict[str, List[Dict[str, float]]]:
    """
    Description:

        Finds extremums in an equation by placing X's value at every interval from the start to end that are mentioned (including)

    Parameters:

        Equation: the equation to check extremums for (use the "CheckEquation" function to convert equation text to equation)
        Start: the starting point to check for extremums
        End: the ending point to check for extremums
        Interval: the interval of the extremums check

    Returns:

        Returns a dictionary with 2 cells, "Minimums" and "Maximums"
        , which are lists of dictionaries with 2 cells, "X" and "Y"
    """

    # Function Variables

    FunctionResult = None

    Minimums = []
    Minimum = None

    Maximums = []
    Maximum = None

    MinNumberX = None
    MinNumberY = None

    MaxNumberX = None
    MaxNumberY = None

    SecondNumberBeforeX = None
    SecondNumberBeforeY = None

    FirstNumberBeforeX = None
    FirstNumberBeforeY = None

    CurrentNumberX = None
    CurrentNumberY = None

    Index = Start

    # Start

    FunctionResult = {"Minimums": Minimums, "Maximums": Maximums}

    SecondNumberBeforeX = Index
    SecondNumberBeforeY = RunEquation(Equation, {"X": SecondNumberBeforeX})

    Index += Interval

    if Index <= End:
        FirstNumberBeforeX = Index
        FirstNumberBeforeY = RunEquation(Equation, {"X": FirstNumberBeforeX})

        if SecondNumberBeforeY < FirstNumberBeforeY:
            MinNumberX = SecondNumberBeforeX
            MinNumberY = SecondNumberBeforeY

            MaxNumberX = FirstNumberBeforeX
            MaxNumberY = FirstNumberBeforeY
        else:
            MinNumberX = FirstNumberBeforeX
            MinNumberY = FirstNumberBeforeY

            MaxNumberX = SecondNumberBeforeX
            MaxNumberY = SecondNumberBeforeY

        Index += Interval

        while Index <= End:
            CurrentNumberX = Index
            CurrentNumberY = RunEquation(Equation, {'X': CurrentNumberX})

            if FirstNumberBeforeY < SecondNumberBeforeY and FirstNumberBeforeY < CurrentNumberY:
                Minimum = {}

                Minimum["X"] = FirstNumberBeforeX
                Minimum["Y"] = FirstNumberBeforeY

                Minimums.append(Minimum)
            elif FirstNumberBeforeY > SecondNumberBeforeY and FirstNumberBeforeY > CurrentNumberY:
                Maximum = {}

                Maximum["X"] = FirstNumberBeforeX
                Maximum["Y"] = FirstNumberBeforeY

                Maximums.append(Maximum)

            if CurrentNumberY < MinNumberY:
                MinNumberX = CurrentNumberX
                MinNumberY = CurrentNumberY

            if CurrentNumberY > MaxNumberY:
                MaxNumberX = CurrentNumberX
                MaxNumberY = CurrentNumberY

            SecondNumberBeforeX = FirstNumberBeforeX
            SecondNumberBeforeY = FirstNumberBeforeY

            FirstNumberBeforeX = CurrentNumberX
            FirstNumberBeforeY = CurrentNumberY

            Index += Interval

    if MinNumberX is not None:
        if len(Minimums) > 0:
            if MinNumberY < min([Minimum["Y"] for Minimum in Minimums]):
                Minimum = {}

                Minimum["X"] = MinNumberX
                Minimum["Y"] = MinNumberY

                Minimums.append(Minimum)
                Minimums.sort(key=lambda Minimum: Minimum["X"])

    if MaxNumberX is not None:
        if len(Maximums) > 0:
            if MaxNumberY > max([Maximum["Y"] for Maximum in Maximums]):
                Maximum = {}

                Maximum["X"] = MaxNumberX
                Maximum["Y"] = MaxNumberY

                Maximums.append(Maximum)
                Maximums.sort(key=lambda Maximum: Maximum["X"])

    return FunctionResult
