from ollama import chat

#select the LLM Local LLM
Model = "llama3.2"

# Define Prompts
prompts = [
    "Explain recursion.",

    "Explain recursion in python in 3 simple points.",

    """your are experienced python teacher.
    Explain recursion for beginner.
    Give one simple example.
""",

""" Convert programming languages to uppercase. 
    Example 1: 
    Input : python
    Output:PYTHON

    Example 2:
    Input : java
    Output : JAVA

    Input : Javascript
    Output :"""

]

# Execute every prompt

for index, prompt in enumerate(prompts, start = 1):
    print("-"*30)
    print("Prompt number :",index)
    print("input prompt :",prompt)

    response = chat(
        model = Model,
        messages=[
            {
            "role" : "user",
            "content" : prompt
            }
        ]
    )
    print("\nResponse from LLM is:")
    print(response.message.content)