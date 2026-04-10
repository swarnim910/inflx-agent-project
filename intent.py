def detect_intent(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "greeting"
    elif "price" in user_input or "plan" in user_input:
        return "pricing"
    elif "buy" in user_input or "subscribe" in user_input or "pro plan" in user_input:
        return "high_intent"
    else:
        return "general"