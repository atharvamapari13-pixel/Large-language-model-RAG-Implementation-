from ollama import chat

messages = [
    {
        "role" : "system",
        "content" : "You are a python programming teacher"
    }
]

print("Marvellous python tutor")
print("Type exit to stop")

while True:
    # Accept user input
    print("-"*40)
    question = input("\nYou :").strip()
    # Stop chat bot
    if question.lower() == "exit":
        print("Thank u for using Marvellous bot")
        break
    # ignore empty line
    if not question:
        continue
    messages.append(
        {
            "role" : "system",
            "content" : question

        }
    )
    response = chat(
        model = "llama3.2",
        messages= messages
    )
    answer = response.message.content

    print("\nMarvellous AI:", answer)

    messages.append(
        {
            "role" : "assistant",
            "content" : answer
        }
    )