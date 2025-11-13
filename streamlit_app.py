import json

class JackKnowledgeBase:
    def __init__(self, filename="jack_kb.json"):
        self.filename = filename
        self.name = "Jack"
        self.knowledge = {}
        self.load()

    def load(self):
        """Load saved knowledge from file."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.knowledge = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.knowledge = {}

    def save(self):
        """Save the knowledge base to file."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.knowledge, f, indent=4, ensure_ascii=False)

    def greet(self):
        print(f"Hello Señor! I am {self.name}, your intelligent knowledge assistant.")
        print("How can I help you today?\n")

    def add_word(self, word: str, definition: str):
        """Add or update a word definition."""
        word = word.lower()
        self.knowledge[word] = definition
        self.save()
        print(f"{self.name}: Added '{word}' to your knowledge base, Señor.")

    def get_definition(self, word: str):
        """Retrieve the definition of a word."""
        word = word.lower()
        if word in self.knowledge:
            print(f"{self.name}: {word.capitalize()} means \"{self.knowledge[word]}\", Señor.")
            return self.knowledge[word]
        else:
            print(f"{self.name}: I’m sorry Señor, I don’t know that word yet.")
            return None

    def search(self, keyword: str):
        """Search for words or definitions containing a keyword."""
        keyword = keyword.lower()
        results = {w: d for w, d in self.knowledge.items() if keyword in w or keyword in d}
        if results:
            print(f"{self.name}: I found {len(results)} results for '{keyword}', Señor:")
            for w, d in results.items():
                print(f" - {w.capitalize()}: {d}")
        else:
            print(f"{self.name}: No matches found for '{keyword}', Señor.")
        return results


if __name__ == "__main__":
    # Initialize Jack
    jack = JackKnowledgeBase()
    jack.greet()

    # === Preloaded Knowledge — Expanded Word Bank ===
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
        # Sprinkled extra words
        "nanotechnology": "The branch of technology that deals with dimensions and tolerances of less than 100 nanometers.",
        "cybersecurity": "The practice of protecting systems, networks, and programs from digital attacks.",
        "renaissance": "The revival of art and literature under the influence of classical models in the 14th–16th centuries.",
        "demography": "The statistical study of populations, including the structure, distribution, and trends.",
        "cryptography": "The art of writing or solving codes.",
        "aurora": "A natural electrical phenomenon characterized by the appearance of streamers of reddish or greenish light in the sky."
    }

    # Load all words into Jack’s knowledge base
    for word, definition in bulk_data.items():
        jack.add_word(word, definition)

    # === Example Interactions ===
    jack.get_definition("gravity")
    jack.search("science")
    jack.get_definition("aurora")
