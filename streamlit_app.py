import streamlit as st
import json
import random

# -----------------------------
# Jack Knowledge Base Class
# -----------------------------
class JackKnowledgeBase:
    def __init__(self, filename="jack_kb.json"):
        self.filename = filename
        self.name = "Jack"  # always Jack
        self.knowledge = {}
        self.friends = ["Magnus", "Alex", "Mallory", "Halfborn", "Sam", "T.J."]
        self.load()

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.knowledge = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.knowledge = {}

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.knowledge, f, indent=4, ensure_ascii=False)

    def add_word(self, word: str, definition: str):
        word = word.lower()
        self.knowledge[word] = definition
        self.save()
        return f"Alright Señor, '{word}' is now part of Jack's knowledge."

    def generate_response(self, message: str):
        """
        Fully generative, original responses by Jack.
        Friends only mentioned if explicitly prompted.
        """
        message_lower = message.lower().strip()

        # If user asks about a known word
        if message_lower in self.knowledge:
            definition = self.knowledge[message_lower]
            return f"{message.capitalize()}… Jack thinks it means {definition}."

        # If the user asks about a friend
        for friend in self.friends:
            if friend.lower() in message_lower:
                return f"You asked about {friend}? Jack can tell you something interesting about them."

        # Otherwise, fully generative response
        verbs = ["ponder", "analyze", "slice through", "examine", "weigh"]
        actions = ["the idea", "the concept", "the situation", "the question", "this matter"]
        descriptors = ["carefully", "with precision", "thoughtfully", "unexpectedly", "curiously"]

        verb = random.choice(verbs)
        action = random.choice(actions)
        descriptor = random.choice(descriptors)

        return f"Jack decides to {verb} {action} {descriptor}."

# -----------------------------
# Initialize Jack
# -----------------------------
jack = JackKnowledgeBase()

# Preload knowledge if empty
if not jack.knowledge:
    bulk_data = {
        "atom": "The smallest unit of ordinary matter that forms a chemical element.",
        "gravity": "The natural force that attracts a body toward the center of the earth, or toward any other physical body having mass.",
        "photosynthesis": "The process by which green plants use sunlight to synthesize foods from carbon dioxide and water.",
        "evolution": "The process by which different kinds of living organisms are thought to have developed from earlier forms during the history of the earth.",
        "neuron": "A specialized cell transmitting nerve impulses; a nerve cell.",
        "galaxy": "A system of millions or billions of stars, together with gas and dust, held together by gravitational attraction.",
        "democracy": "A system of government by the whole population, typically through elected representatives.",
        "algorithm": "A process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer."
    }
    for word, definition in bulk_data.items():
        jack.add_word(word, definition)

# -----------------------------
# Streamlit Interface
# -----------------------------
st.title("Jack")


# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.text_input("You:", placeholder="Type a message for Jack")
if st.button("Send"):
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append(f"Señor: {user_input}")
        # Generate Jack's response
        response = jack.generate_response(user_input)
        st.session_state.chat_history.append(f"Jack: {response}")

# Display chat history
st.text_area("Chat History", value="\n".join(st.session_state.chat_history), height=400, key="chat_area")
