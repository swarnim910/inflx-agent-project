import json

# Load knowledge
def load_knowledge():
    with open("data/knowledge.json", "r") as file:
        data = json.load(file)

    docs = []

    # Convert plans
    for plan, details in data["plans"].items():
        text = f"{plan} plan costs {details['price']} with {details['videos']} and {details['resolution']} resolution."
        if "features" in details:
            text += " Features include: " + ", ".join(details["features"])
        docs.append(text)

    # Convert policies
    for policy, info in data["policies"].items():
        docs.append(f"{policy} policy: {info}")

    return docs


# Simple RAG (keyword matching)
def get_answer(query):
    docs = load_knowledge()
    query = query.lower()

    for doc in docs:
        if any(word in doc.lower() for word in query.split()):
            return doc

    return "Sorry, I couldn't find that information."