import importlib.util
import sys
import tempfile

def load_function_from_code(code: str, function_name: str, *args):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
        temp_file.write(code.encode('utf-8'))
        temp_file.close()

        spec = importlib.util.spec_from_file_location("dynamic_module", temp_file.name)
        dynamic_module = importlib.util.module_from_spec(spec)
        sys.modules["dynamic_module"] = dynamic_module
        spec.loader.exec_module(dynamic_module)

        if hasattr(dynamic_module, function_name):
            func = getattr(dynamic_module, function_name)
            return lambda: func(*args)  # Return a callable that includes args
        else:
            raise AttributeError(f"{function_name} not found in the dynamically loaded module.")

# Example usage:
code = """
def new_mechanic():
    print("New mechanic activated!")
"""
new_mechanic_func = load_function_from_code(code, "new_mechanic")
# new_mechanic_func()  # This will output: New mechanic activated!

