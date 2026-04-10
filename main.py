from agent import Agent

agent = Agent()

print("🤖 AutoStream AI Agent (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    response = agent.handle_input(user_input)
    print("Agent:", response)