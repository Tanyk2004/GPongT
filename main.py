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

    # * Test Code 1
    # resp = GPT().text_completion(system_prompt=read_file("./llm/prompt.txt"), user_prompt=read_file("./llm/user_prompt.txt"))
    # new_resp = ""
    # for line in resp.split("\n"):
    #     if '```' not in line:
    #         new_resp += line + "\n"
    # print(new_resp)

    # * Actual Main
    truncate_file("game/gpt_generated_dynamic.py")
    write_to_python_file("import game.globals\nimport random\nimport pygame\nfrom game.game import GameClass\n",
                          "game/gpt_generated_dynamic.py")
    g = GameClass()

    g.entry_point()

    # game_file_state = read_file("./game/game.py")
    # prompt = read_file("./llm/prompt.txt")
    # user_prompt = read_file("./llm/user_prompt.txt")

    # resp = GPT().text_completion(system_prompt=prompt, user_prompt=user_prompt)
    # resp = "import game.globals\n" + resp
    # write_to_python_file(resp, "game/gpt_generated_dynamic.py")

    # functions = load_and_execute_functions("game.gpt_generated_dynamic")
    # print(functions)
    # wildcard_function(*functions)
    # print(game.globals.ball_speed_x)
    # print(game.globals.ball_speed_y)
    # print(get_summary("./game/gpt_generated_dynamic.py"))
