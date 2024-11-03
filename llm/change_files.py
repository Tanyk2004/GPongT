def read_file(file_path: str) -> str:
    """
        Read the file with the given file path

        @param file_path: The path to the file

    """
    f = open(f"{file_path}", "r")
    return f.read()

def read_functions_from_file(file_name: str):
    """
        Read the functions from the file with the given file name

        @param file_name: The name of the file to be read

    """
    file_content = read_file(file_name)
    """
tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
] 
    """

    file_lines = file_content.split("\n")
    
    for line in file_lines:
        
        if "def" in line:
            print(line)
            function_name = line.split("def ")[1].split("(")[0]
            # function_description = line.split("# description: ")[1]
            print(f"Function name: {function_name}")
            
    functions = []

    return functions

def write_to_python_file(content: str, file_name: str = "output.py"):
    """
    Writes the given content to a Python file.

    Parameters:
        content (str): The content to write to the file.
        file_name (str): The name of the Python file to create or overwrite.
                         Default is "output.py".

    Returns:
        None
    """
    try:
        with open(file_name, "w") as file:
            file.write(content)
        print(f"Content successfully written to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
  
def append_to_python_file(content: str, file_name: str = "output.py"):
    """
    Appends the given content to a Python file.

    Parameters:
        content (str): The content to append to the file.
        file_name (str): The name of the Python file to append to.
                         Default is "output.py".

    Returns:
        None
    """
    try:
        with open(file_name, "a") as file:
            file.write(content)
        print(f"Content successfully appended to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_summary(file_name):
    """
    Returns the summary text starting from the # Summary line and including all subsequent lines.
    """
    summary = ""
    
    try:
        with open(file_name, 'r') as file:
          file_content = file.read()
          file_lines = file_content.split("\n")
          last_index = -1
          for line_number in range(len(file_lines)):
            if file_lines[line_number].startswith("# Summary:"):
              last_index = line_number 

          if last_index != -1:
              summary = "\n".join(file_lines[last_index:])          

    except FileNotFoundError:
        print(f"File {file_name} not found.")
    
    return summary.strip().split("# Summary:")[1]


def truncate_file(file_name: str):
    """
        Truncate the file with the given file name

        @param file_name: The name of the file to be truncated

    """
    f = open(file_name, "w")
    f.truncate()
    f.close()

if __name__ == "__main__":
    read_file("sample.py")