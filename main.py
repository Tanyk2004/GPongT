from llm.gpt_api import GPT
from llm.change_files import read_file, write_to_python_file, read_functions_from_file, truncate_file
# from game.wildcard_functions import wildcard_function, load_and_execute_functions
# import game.globals
# from llm.change_files import get_summary
from game.game import GameClass
import pygame

# # Example usage
# code = """def greet():
#     print("Hello, world!")

# greet()
# """
if __name__ == "__main__":
    global g

    truncate_file("game/gpt_generated_dynamic.py")
    import_string = "import game.globals\nimport random\nimport pygame\nfrom game.game import GameClass\nimport math\n"
    write_to_python_file(import_string,
                          "game/gpt_generated_dynamic.py")
    g = GameClass()

    g.entry_point()

