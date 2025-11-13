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
        self.friends = [
            "Magnus Chase", "Alex Fierro", "Mallory Keen",
            "Halfborn Gunderson", "Samirah al-Abbas", "Thomas Jefferson Jr. (T.J.)"
        ]
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

    def generate_response(self, message: str, moral_compass: float):
        """
        Fully generative Jack response.
        moral_compass: 0 = fully chaotic/immoral, 1 = fully ethical/moral
        Influences tone, advice, and humor.
        """

        message_lower = message.lower().strip()

        # If the user asks about a known word, generate a creative response
        if message_lower in self.knowledge:
            definition = self.knowledge[message_lower]
            # Moral compass affects how Jack explains it
            if moral_compass > 0.7:
                tone = f"Alright Señor, here's the noble truth: {definition}."
            elif moral_compass < 0.3:
                tone = f"Yeah, {message}? Technically it's {definition}, but you could bend it if you want… 😉"
            else:
                tone = f"{message.capitalize()} is basically this: {definition}. Magnus would probably nod."
            # Sometimes mention a friend
            if random.random() < 0.4:
                friend = random.choice(self.friends)
                tone += f" {friend} would probably have an opinion too."
            return tone

        # Otherwise, generate a creative answer
        actions = [
            "ponder", "slice through the problem", "joke about it", "give a clever answer", "reference my friends"
        ]
        action = random.choice(actions)

        if moral_compass > 0.7:
            tone = f"Señor, I {action} responsibly: I think about the ethical choice here."
        elif moral_compass < 0.3:
            tone = f"Señor, I {action} recklessly. Why not? Chaos is fun 😏"
        else:
            tone = f"Señor, I {action}… kinda neutral this time."

        # Add a friend reference sometimes
        if random.random() < 0.4:
            friend = random.choice(self.friends)
            tone += f" Maybe {friend} would have a sarcastic remark about this."

        return tone

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
        "democracy": "A system of government by the whole population, typically through elected representatives."
        # Add more knowledge as needed...
    }
    for word, definition in bulk_data.items():
        jack.add_word(word, definition)

# -----------------------------
# Streamlit Interface
# -----------------------------
st.title("Jack - The Sword from Magnus Chase Universe 🗡️")
st.write(
    "Hello Señor! I’m Jack, the sword. I generate knowledge creatively, reference my friends, "
    "and sometimes give advice influenced by my moral compass."
)

# Moral compass as a black and white circle slider
moral_compass = st.slider(
    "Jack's moral compass (turn the knob to influence my ethical side)", 0.0, 1.0, 0.5, 0.01
)
st.caption("0 = chaotic/reckless, 1 = fully moral/ethical")

# Chat input
user_input = st.text_input("You:", placeholder="Type a question or message for Jack")
if st.button("Send"):
    if user_input:
        response = jack.generate_response(user_input, moral_compass)
        st.text_area("Jack:", value=response, height=200)
