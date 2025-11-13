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
        return f"Alright Señor, '{word}' is now part of my brain. Magnus would be proud… maybe."

    def generate_response(self, message: str, chill_level: float):
        """
        Generates a response as Jack (the sword) with Magnus Chase-style personality.
        chill_level: 0 = sharp, formal; 1 = sarcastic, witty, laid-back
        """
        message_lower = message.lower().strip()

        # Check if asking about a known word
        if message_lower in self.knowledge:
            definition = self.knowledge[message_lower]
            if chill_level < 0.4:
                return f"{message.capitalize()}: {definition}"
            else:
                twists = [
                    f"{message}? Well, it's basically this: {definition}. Magnus would probably roll his eyes. 😏",
                    f"Ah, {message}! Fun fact: {definition}. Alex might argue about this too.",
                    f"Alright, if you really want to know, Señor: {definition}. Mallory might give me a 'tsk', but whatever."
                ]
                return random.choice(twists)

        # Check for search
        if message_lower.startswith("search "):
            keyword = message_lower.replace("search ", "")
            results = {w: d for w, d in self.knowledge.items() if keyword in w or keyword in d}
            if results:
                response = f"Found {len(results)} matches for '{keyword}', Señor:\n"
                for w, d in results.items():
                    response += f"- {w.capitalize()}: {d}\n"
                if chill_level > 0.5:
                    friend = random.choice(self.friends)
                    response += f"\nNot too shabby, right? {friend} would approve. 😎"
                return response
            else:
                return f"No luck finding '{keyword}', Señor. Even T.J. might have trouble with this one."

        # General conversational Jack-style responses
        casual_phrases = [
            "You think you can stump me? Try harder. 😏",
            "Alright, Señor, let's see what happens.",
            "Sure, yeah… that sounds like a plan.",
            "Classic move, gotta admit, pretty clever.",
            "Meh, could be worse. Let's roll with it.",
            "Honestly, that's kinda funny 😎."
        ]

        formal_phrases = [
            "Acknowledged, Señor.",
            "Understood. Let me process that.",
            "Interesting… noted.",
            "Alright, we can proceed accordingly.",
            "Thank you for the clarification."
        ]

        # Add references to friends if chill_level is high
        if chill_level > 0.5 and random.random() < 0.3:  # 30% chance to mention a friend
            friend = random.choice(self.friends)
            casual_phrases.append(f"By the way, {friend} would have something to say about that. 😏")

        # Adjust response length based on chill_level
        length_multiplier = int(1 + chill_level * 3)  # 1-4 sentences
        response_list = casual_phrases if chill_level > 0.5 else formal_phrases
        response = " ".join(random.choices(response_list, k=length_multiplier))
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
        "algorithm": "A process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.",
        "entropy": "A measure of disorder or randomness in a system.",
        "quantum": "The minimum amount of any physical entity involved in an interaction.",
        "biodiversity": "The variety of plant and animal life in the world or in a particular habitat.",
        "ecosystem": "A biological community of interacting organisms and their physical environment.",
        "blockchain": "A system in which a record of transactions made in cryptocurrency is maintained across several computers linked in a peer-to-peer network.",
        "photosphere": "The luminous envelope of a star from which its light and heat radiate.",
        "volcano": "A rupture in the crust of a planetary body that allows hot lava, volcanic ash, and gases to escape from below the surface.",
        "tsunami": "A long, high sea wave caused by an earthquake, submarine landslide, or other disturbance.",
        "black hole": "A region of space having a gravitational field so intense that no matter or radiation can escape.",
        "machine learning": "A branch of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.",
        "genome": "The complete set of genes or genetic material present in a cell or organism.",
        "oxygen": "A chemical element essential for most forms of life on Earth.",
        "hydrogen": "The lightest chemical element, often found as a gas, and a key component of water.",
        "computer": "An electronic device for storing and processing data according to instructions given to it in a program.",
        "internet": "A global computer network providing a variety of information and communication facilities.",
        "solar system": "The collection of eight planets and their moons in orbit around the sun.",
        "planet": "A celestial body moving in an elliptical orbit around a star.",
        "artificial intelligence": "The simulation of human intelligence processes by machines, especially computer systems.",
        "robotics": "The branch of technology that deals with the design, construction, operation, and application of robots.",
        "metabolism": "The chemical processes that occur within a living organism to maintain life.",
        "psychology": "The scientific study of the human mind and its functions, especially those affecting behavior.",
        "sociology": "The study of the development, structure, and functioning of human society.",
        "philosophy": "The study of the fundamental nature of knowledge, reality, and existence.",
        "economics": "The branch of knowledge concerned with the production, consumption, and transfer of wealth.",
        "chemistry": "The branch of science that deals with the identification of the substances of which matter is composed.",
        "physics": "The branch of science concerned with the nature and properties of matter and energy.",
        "mathematics": "The abstract science of number, quantity, and space.",
        "geometry": "The branch of mathematics concerned with the properties and relations of points, lines, surfaces, and solids.",
        "history": "The study of past events, particularly in human affairs.",
        "literature": "Written works, especially those considered of superior or lasting artistic merit.",
        "music": "The art of arranging sounds in time to produce a composition through elements of melody, harmony, rhythm, and timbre.",
        "art": "The expression or application of human creative skill and imagination, producing works to be appreciated primarily for their beauty or emotional power.",
        "language": "A system of communication used by a particular country or community.",
        "culture": "The customs, arts, social institutions, and achievements of a particular nation or people.",
        "ethics": "Moral principles that govern a person's behavior or the conducting of an activity.",
        "justice": "Just behavior or treatment; the quality of being fair and reasonable.",
        "law": "The system of rules recognized by a particular country or community as regulating the actions of its members.",
        "medicine": "The science or practice of the diagnosis, treatment, and prevention of disease.",
        "biology": "The study of living organisms, divided into many specialized fields.",
        "zoology": "The scientific study of the behavior, structure, physiology, classification, and distribution of animals.",
        "botany": "The scientific study of plants.",
        "geology": "The science that deals with the earth's physical structure and substance.",
        "meteorology": "The branch of science concerned with the processes and phenomena of the atmosphere.",
        "astronomy": "The branch of science that deals with celestial objects, space, and the universe as a whole.",
        "cosmology": "The science of the origin and development of the universe.",
        "nanotechnology": "The branch of technology that deals with dimensions and tolerances of less than 100 nanometers.",
        "cybersecurity": "The practice of protecting systems, networks, and programs from digital attacks.",
        "renaissance": "The revival of art and literature under the influence of classical models in the 14th–16th centuries.",
        "demography": "The statistical study of populations, including the structure, distribution, and trends.",
        "cryptography": "The art of writing or solving codes.",
        "aurora": "A natural electrical phenomenon characterized by the appearance of streamers of reddish or greenish light in the sky."
    }

    for word, definition in bulk_data.items():
        jack.add_word(word, definition)

# -----------------------------
# Streamlit Interface
# -----------------------------
st.title("Jack - The Sword from Magnus Chase Universe 🗡️")
st.write("Hello Señor! I'm Jack, witty, sarcastic, and fully chill. Chat with me, ask questions, or search my knowledge base. I might reference Magnus and my friends!")

# Chill/laid-back slider
chill_level = st.slider("Jack's chill level", 0.0, 1.0, 0.6, 0.05)
st.caption("0 = sharp/formal, 1 = sarcastic, witty, and laid-back")

# Chat input
user_input = st.text_input("You:", placeholder="Type a message or ask a question...")
if st.button("Send"):
    if user_input:
        response = jack.generate_response(user_input, chill_level)
        st.text_area("Jack:", value=response, height=200)
