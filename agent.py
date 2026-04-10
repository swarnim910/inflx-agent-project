from rag import get_answer

class Agent:
    def __init__(self):
        self.lead_mode = False
        self.user_data = {}

    def handle_input(self, user_input):
        user_input = user_input.lower()

        # Step 1: Greeting
        if any(word in user_input for word in ["hi", "hello", "hey"]):
            return "Hi! 👋 How can I help you today?"

        # Step 2: High Intent Detection (IMPORTANT)
        if any(word in user_input for word in ["buy", "purchase", "subscribe"]):
            self.lead_mode = True
            self.user_data = {}
            return "Great! Let's get you started 😊\nWhat's your name?"

        # Step 3: Lead Capture Flow
        if self.lead_mode:
            if "name" not in self.user_data:
                self.user_data["name"] = user_input
                return "Please enter your email:"

            elif "email" not in self.user_data:
                self.user_data["email"] = user_input
                return "Which platform do you create content on?"

            elif "platform" not in self.user_data:
                self.user_data["platform"] = user_input
                self.lead_mode = False

                # Simulate tool execution
                print("\n📌 Captured Lead Data:", self.user_data)

                return "✅ Lead captured successfully!\n🎉 Our team will contact you soon."

        # Step 4: RAG fallback
        return get_answer(user_input)