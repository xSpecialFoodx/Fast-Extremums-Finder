#
# #
# # #
# # # # Equations Solver
# # #
# #
#

"""
Description:

    Solves equations that are given as texts
"""

from __future__ import annotations

from typing import Dict

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


def RunEquation(Equation: sympy.core.mul.Mul, Variables: Dict[str, float] = None) -> float:
    """
    Description:

        Runs the equation based on the variables

    Parameters:

        Equation: the equation to run
        Variables:
            the variables to input into the equation
            , the default value is None, which goes for not having any variables

    Returns:

        Returns the result (typically: "Y")
    """

    # Start

    return float(
        Equation.evalf(
            subs=(
                (
                    {
                        VariablesItem[0].upper(): VariablesItem[1]
                        for VariablesItem in Variables.items()
                    }
                )
                if Variables is not None
                else None
            )
        )
    )
