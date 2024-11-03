def read_file(file_path: str):
    """
        Read the file with the given file path

        @param file_path: The path to the file

    """
    f = open(f"./{file_path}", "r")
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
            function_name = line.split("def ")[1].split("(")[0]
            function_description = line.split("# description: ")[1]
            print(f"Function name: {function_name}")
            parameters_list_raw = line.split("(")[1].split(")")[0].split(",")
            print(f"Parameters: {parameters_list_raw}")
            parameters_list = []
            for parameter in parameters_list_raw:
                parameter_name = parameter.split(":")[0]
                parameter_type = parameter.split(":")[1]
                parameters_list.append({"name": parameter_name, "type": parameter_type, "optional": "=" in parameter})
            print(f"Parameters: {parameters_list}")

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

if __name__ == "__main__":
    read_file("sample.py")
    
