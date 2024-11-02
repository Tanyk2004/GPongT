from llm.gpt_api import GPT
from llm.change_files import read_file, write_to_python_file

# Example usage
code = """def greet():
    print("Hello, world!")

greet()
"""

if __name__ == "__main__":
    read_file("sample.py") 
    write_to_python_file(code, "greet.py")
    