from llm.gpt_api import GPT
from llm.change_files import read_file, write_to_python_file, read_functions_from_file

# Example usage
code = """def greet():
    print("Hello, world!")

greet()
"""
# TODO: have the llm return a sentence summarizing what it did. Put that into the program as text that will show up on the screen
if __name__ == "__main__":
    game_file_state = read_file("./game/base_game.py")
    prompt = read_file("./llm/prompt.txt")

    resp = GPT().text_completion(system_prompt=prompt, user_prompt="Make the game harder by introducing new elements in the game")
    print(resp)