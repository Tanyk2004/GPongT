def read_file(file_name: str):
    """
        Read the file with the given file name

        @param file_name: The name of the file to be read

    """
    f = open(f"./game/{file_name}", "r")
    return f

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
    write_to_python_file(code, "greet.py")
