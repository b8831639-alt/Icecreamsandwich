import streamlit as st
import json
import random

# -----------------------------
# Jack Knowledge Base Class
# -----------------------------
class JackKnowledgeBase:
    def __init__(self, filename="jack_kb.json"):
        self.filename = filename
        self.name = "Jack"  # the sword
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
        return f"Alright Señor, '{word}' is now part of my knowledge."

    def generate_response(self, message: str):
        """
        Fully generative, original-text response by Jack.
        Can reference friends and creatively use knowledge base.
        """
        message_lower = message.lower().strip()

        # If user asks about a known word, use it creatively
        if message_lower in self.knowledge:
            definition = self.knowledge[message_lower]
            # Build original response using definition
            response = f"Hmm, {message.capitalize()}… thinking about it, it means {definition}"
            # 30% chance to reference a friend
            if random.random() < 0.3:
                friend = random.choice(self.friends)
                response += f". {friend} would probably have something witty to add about that."
            return response

        # Otherwise, generate a creative, original answer
        # Jack "thinks" like a sword with personality
        intros = [
            "Well, let me think…",
            "If I were to slice through this idea…",
            "Pondering that, Señor…",
            "Huh, this is interesting…"
        ]
        middles = [
            f"I imagine Magnus would nod at this.",
            f"Alex might have a sarcastic comment about it.",
            f"Mallory could probably point out something clever here.",
            f"Halfborn would just shrug.",
            f"Sam would roll her eyes.",
            f"T.J. would probably jump in excitedly."
        ]
        endings = [
            "Honestly, it's a puzzle, but I like it.",
            "Not too complicated for a sword to think about.",
            "Could be dangerous, could be fun…",
            "That's my take on it, Señor."
        ]

        # Randomly combine for fully original response
        response = f"{random.choice(intros)} {random.choice(middles)} {random.choice(endings)}"
        return response

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
        # Add more knowledge as desired
    }
    for word, definition in bulk_data.items():
        jack.add_word(word, definition)

# -----------------------------
# Streamlit Interface
# -----------------------------
st.title("Jack")


# Chat input
user_input = st.text_input("You:", placeholder="Type a question or message for Jack")
if st.button("Send"):
    if user_input:
        response = jack.generate_response(user_input)
        st.text_area("Jack:", value=response, height=200)
