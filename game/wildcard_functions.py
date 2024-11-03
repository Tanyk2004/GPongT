import importlib
import os
import inspect
import game.globals
import sys

def wildcard_function(*functions): 
    for function in functions:
        function()

def load_and_execute_functions(module_name):
    """
    Loads all functions from a specified file and passes them to wildcard_function.

    Parameters:
        module_name (str): The name of the Python module to load functions from (take care of hierarchy).
        wildcard_function (function): The function that takes other functions as arguments and executes them.

    Returns:
        List[function]: A list of functions loaded from the specified module.
    """
    # Dynamically import the module
    if module_name in sys.modules:
        del sys.modules[module_name]

    module = importlib.import_module(module_name)
    
    # Get all functions defined in the module
    functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]
    print("Functions Loaded just now are: ", functions)
    return functions


