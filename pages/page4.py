import streamlit as st
import requests
from navigation import make_sidebar, check_user_inactivity

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

########################################################################################

# Updated list of words
words = [
    "abandon", "absent", "absolute", "academy", "ache",
    "address", "adult", "afterglow", "against", "airliner", "alley", "allspice", "almond", "already", "alter",
    "ambition", "amusement", "ancestor", "annual", "apology", "appetite", "argue", "artist", "assign", "astronomer",
    "athlete", "autograph", "autumn", "awesome", "backpack", "badger", "bagel", "bait", "banana", "barefoot",
    "bark", "barley", "barrier", "baste", "beaver", "beehive", "beige", "beverage", "beware", "biology",
    "black hole", "blade", "blockage", "blueberry", "blurt", "blush", "borrow", "bottom", "bravery", "bridesmaid",
    "bridle", "bronco", "brownie", "building", "built-in", "buttermilk", "calm", "camel", "canine", "capsule", "California", 
    "cashew", "caterpillar", "catwalk", "cautious", "cement", "century", "champion", "charming", "cheerful", "childish",
    "chuckle", "circuit", "circulate", "citizenship", "climate", "coconut", "collection", "comma", "company", "compel",
    "computer", "concern", "condone", "copy", "cousin", "creakier", "creepy", "cricket", "curtsy", "custard",
    "dairy", "dazzled", "deaden", "decaf", "decent", "decimal", "decline", "dentist", "dependable", "desktop",
    "dessert", "develop", "diary", "dipper", "direction", "disappoint", "disease", "dishonest", "dismiss", "dispute",
    "distrust", "dizzy", "doggy", "dose", "downwind", "dramatic", "dribble", "drinkable", "drudge", "duet",
    "eagle", "earnings", "easiest", "easygoing", "echo", "economical", "edition", "educate", "eggplant", "either",
    "elderly", "electrify", "element", "elevator", "elude", "emotion", "empower", "enable", "ending", "energy",
    "entirely", "entrap", "entry", "error", "essay", "esteem", "ever", "example", "exchange", "exercise",
    "export", "eye-catching", "eyelash", "factual", "falcon", "famous", "farmstead", "faucet", "fearless", "ferret",
    "festival", "fidget", "field", "filmstrip", "fizzling", "flavor", "fleece", "foliage", "footstep", "foresight",
    "forestry", "formula", "forthright", "framed", "frank", "freaky", "frightful", "frown", "fudge", "funnel",
    "furry", "gadget", "gala", "galaxy", "garden", "garment", "garnish", "gathering", "generous", "genius",
    "gentlefolk", "geology", "German", "germfree", "giggle", "giraffe", "glassblower", "glimpse", "gloomy", "goalpost", "goggles",
    "gosling", "grader", "granite", "graph", "gravity", "gravy", "greedy", "griddle", "grime", "grungy",
    "guardian", "guide", "guitar", "gummy", "gusto", "hairdresser", "hallway", "halt", "handful", "handsaw",
    "hapless", "harmonica", "harp", "harvest", "hateful", "hawk", "headfirst", "healer", "heavenly", "hefty",
    "hemline", "heritage", "hipbone", "Hispanic", "history", "hoarse", "honorable", "hotel", "hottest", "housemaid", "humid",
    "hurricane", "hurried", "igloo", "illness", "image", "immune", "impact", "imprint", "imprison", "incoming",
    "index", "indigo", "infest", "inform", "inherit", "injury", "inkling", "inland", "inquest", "inscribe",
    "insertion", "insulate", "interest", "intrude", "inventive", "Irish", "iron", "irritate", "jabbed", "jacket", "jailbird",
    "janitor", "jawbone", "jelly", "journal", "June", "junior", "kennel", "keynote", "kidnap", "kindness", "kitty",
    "knuckle", "kook", "landing", "landscape", "larva", "lately", "latitude", "lavender", "lawyer", "leader",
    "leakage", "leap", "legally", "leotard", "liberty", "ligament", "light-footed", "likeness", "limiting", "linger",
    "lining", "listen", "liven", "lofty", "logbook", "longhorn", "loudness", "loveliness", "luminous", "lure",
    "lush", "machine", "magazine", "magical", "magnet", "majority", "mammoth", "manager", "marine", "massage",
    "massive", "mechanical", "medicine", "medley", "meow", "merge", "mermaid", "microwave", "migrant", "mineral",
    "mingled", "minimal", "misshapen", "mistletoe", "mistreat", "modest", "modify", "molasses", "muffler", "muscle",
    "mystery", "myth", "napkin", "narrate", "national", "naturalize", "nearby", "necessary", "necklace", "neglect",
    "nephew", "newlywed", "nineteenth", "noel", "noggin", "nomad", "nonfiction", "nonviolent", "normal", "nosebleed",
    "noted", "notion", "nourish", "novel", "noxious", "nudging", "numeric", "nunnery", "nuzzle", "nylon",
    "oarsman", "obsess", "obstinate", "obtain", "oddity", "offense", "oilcloth", "okra", "once", "oodles",
    "oozy", "operate", "opposite", "opt", "orbit", "ordeal", "ore", "organ", "origin", "ouch",
    "ounce", "outlandish", "outside", "overcome", "overripe", "ozone", "painful", "panic", "parasite", "parish",
    "particle", "pastry", "pasture", "patrolman", "peach", "peacock", "pecan", "pedicure", "percent", "perky",
    "perplex", "perspire", "phonics", "phrase", "physical", "pierce", "pledge", "pliable", "pointless", "positive",
    "poultice", "preacher", "precious", "predict", "priceless", "primary", "prosper", "proverb", "purebred", "quail",
    "quaint", "quart", "quash", "quest", "quibbling", "quilt", "quirk", "quite", "quoted", "radar",
    "radio", "raggedy", "raisin", "readable", "rebate", "recess", "recollect", "refashion", "regardful", "register",
    "release", "relic", "remedy", "reporter", "reptile", "respond", "retail", "retreat", "revenge", "rhino",
    "riflery", "romance", "rooster", "rotating", "rough", "rowdy", "ruby", "rudeness", "rust", "sacred",
    "salmon", "salute", "sarcastic", "sawdust", "scientist", "scorpion", "seamstress", "secretary", "seventh", "several",
    "shabbily", "sibling", "sketch", "slippery", "sluggish", "snoopy", "soccer", "soprano", "sourdough", "soybean",
    "spirited", "sponsor", "stadium", "stomach", "struggle", "subtract", "succeed", "suddenly", "superior", "syllable",
    "system", "tabulate", "talent", "tattered", "tattletale", "teethe", "tempting", "tennis", "term", "textbook",
    "thankfully", "theft", "thermostat", "thicken", "thievery", "throat", "thumbnail", "thunderbolt", "tickling", "timid",
    "together", "toughen", "tourism", "treasure", "tremor", "tribal", "trombone", "trouble", "tulip", "tuneful",
    "turmoil", "twitter", "typhoon", "umpire", "unable", "underhand", "underneath", "unfair", "unicorn", "uninstall",
    "unit", "universe", "unlisted", "unpleasant", "unseal", "unsure", "untangle", "upright", "upturn", "urban",
    "usable", "utterly", "vacate", "valor", "valuable", "variety", "vast", "vehicle", "venom", "verdict",
    "vibrant", "victor", "vinegar", "violence", "visiting", "visual", "vocal", "vowel", "voyage", "vulture",
    "wakeful", "waltz", "watermelon", "weather", "welcome", "westerly", "whitener", "wholesome", "wisdom", "worrisome",
    "writing", "xylem", "yank", "yardage", "yearly", "yoga", "youthful", "zap", "zest", "zookeeper"
]

# Create 26 tests (A-Z)
def create_tests(words_list):
    tests = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        filtered_words = [word for word in words_list if word.startswith(letter)]
        tests[letter] = filtered_words
    return tests

tests = create_tests(words)

# Streamlit application
st.title("👍 5th-6th Grade - Spelling Game")

def pronounce(word):
    # Embed the ResponsiveVoice script into Streamlit using components
    st.components.v1.html(f"""
    <script src="https://code.responsivevoice.org/responsivevoice.js?key=Ytp4Wvua"></script>
    <script>
        responsiveVoice.speak("{word}", "UK English Male");
    </script>
    """, height=0)  # Set height=0 to hide the script output

# Select test
letter = st.sidebar.selectbox("Select a letter below:", list(tests.keys()))
words_to_test = tests[letter]

# Initialize session state for tracking the current word index and incorrect words
if 'current_word_index' not in st.session_state:
    st.session_state.current_word_index = 0
    st.session_state.score = 0
    st.session_state.incorrect_words = []  # List to track incorrect words
    st.session_state.retest = False  # Flag to indicate retesting mode

# Get the current word based on the index
current_word_index = st.session_state.current_word_index

# Show the current word
if current_word_index < len(words_to_test):
    current_word = words_to_test[current_word_index]

    st.subheader("◼️ Instructions - How to play the spelling game:")
    st.write("◾️ STEP-1. Select a spelling game and a letter from the [LEFT SIDEBAR]")
    st.write("◾️ STEP-2. Press [BUTTON-🔴Pronounce Word] to hear the spelling word")
    st.write("◾️ STEP-3. The word will be pronounced once")
    st.write("◾️ STEP-4. Place your cursor in the ✏️ TEXT BOX-Your Answer below")
    st.write("◾️ STEP-5. Type your answer in the ✏️ TEXT BOX-Your Answer below")
    st.write("◾️ STEP-6. Press [BUTTON-🟡Submit] to submit your answer")
    st.write("◾️ STEP-7. Press [BUTTON-🟢Next Word] to proceed after you get the result")
    st.write("(🔺 Users are logged out after 15 minutes of inactivity!)")

    # Show pronunciation button
    if st.button("🔴Pronounce Word", key="pronounce"):
        pronounce(current_word)

    # Input field for user's answer
    user_input = st.text_input(
        "✏️ Your answer (hidden word):",
        key=f"input_{current_word_index}",  # Unique key to force resetting input field
    )

    # Handle button display logic
    submit_button = st.button("🟡Submit", key="submit")
    next_word_button = st.button("🟢Next Word", key="next_word")
    
    # CSS for custom button styles
    st.markdown("""
    <style>
        .stButton>button {
            background-color: green;
            color: white;
            font-weight: bold;
            border-radius: 5px;
        }
        .stTextInput input {
            font-size: 18px;
        }
        .score-text {
            color: blue;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    # Handle the logic when the submit button is clicked
    if submit_button:
        # Pronounce the next word right after the user submits
        if user_input.strip().lower() == current_word:
            st.success("Correct! ✔️")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect! ❌ The correct spelling is: {current_word}")
            # Add the word to the list of incorrectly spelled words
            if current_word not in st.session_state.incorrect_words:
                st.session_state.incorrect_words.append(current_word)
        
        # Hide the Pronounce and Submit buttons, show Next Word button
        submit_button = None
        st.session_state.current_word_index += 1

    # Display the current score (correct answers / total_words)
    st.markdown(f"**Your current score: {st.session_state.score} / {current_word_index + 1}**", unsafe_allow_html=True)

    # If at the end, reset or display the final score
    if st.session_state.current_word_index >= len(words_to_test) and not st.session_state.retest:
        st.markdown(f"**Your final score is: {st.session_state.score} / {len(words_to_test)}**", unsafe_allow_html=True)
        if len(st.session_state.incorrect_words) > 0:
            retest_button = st.button("Retake Incorrect Words Test")
            if retest_button:
                st.session_state.retest = True
                st.session_state.current_word_index = 0  # Reset to the beginning of the retest
        else:
            st.success("All words spelled correctly! 🎉")

    # If in retest mode, show the incorrect words
    if st.session_state.retest:
        if len(st.session_state.incorrect_words) > 0:
            st.subheader("Retest - Incorrect Words:")
            word_to_test = st.session_state.incorrect_words[st.session_state.current_word_index]

            # Show word and input box for retest
            st.write(f"Spelling word: {word_to_test}")
            retest_input = st.text_input(f"Your answer for: {word_to_test}")

            if st.button("🟡Submit Retest"):
                if retest_input.strip().lower() == word_to_test:
                    st.success("Correct! ✔️")
                    st.session_state.incorrect_words.remove(word_to_test)  # Remove correct words from retest
                else:
                    st.error(f"Incorrect! ❌ The correct spelling is: {word_to_test}")
                st.session_state.current_word_index += 1

            # Show final message after retest
            if len(st.session_state.incorrect_words) == 0:
                st.success("All incorrect words are now correct! 🎉")

            # Option to restart retest
            if st.session_state.current_word_index >= len(st.session_state.incorrect_words):
                st.session_state.retest = False
                st.session_state.current_word_index = 0
        else:
            st.success("All incorrect words are now correct! 🎉")

    # If at the end of the list, give the option to restart
    if st.session_state.current_word_index >= len(words_to_test) and not st.session_state.retest:
        if st.button("Restart"):
            st.session_state.current_word_index = 0
            st.session_state.score = 0
            st.session_state.incorrect_words = []
else:
    st.markdown(f"**Your final score is: {st.session_state.score} / {len(words_to_test)}**", unsafe_allow_html=True)
    if st.button("Restart"):
        st.session_state.current_word_index = 0
        st.session_state.score = 0
