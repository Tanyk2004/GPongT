# Future Goals

### Current goal

- parse summary messages so that they are easier to read

### Immediate next steps

- working game objects
    - handle parameters in generated code
- pass in the existing state of gpt_generated_dynamic to the next prompt
    - make it so that it prefers the previous stuff it has done

### Before Hackathon Ends

- refactor code
    - put calling llm stuff into gpt_api class (game.py)
    - load and store one function in at a time (game.py)
- add a function list that gpt can call (get_api.py)
### try-catch GPT generated functions
- display updates made to the code
- LLM can work with tick_count so not every func is runnning on every tick

### Reaches

- sprites
- user controls how many changes are made per round and other settings
- have all prompts occur in one conversation so that functions can easily 
    build on each other
- another LLM will look at and check the codes for bugs

