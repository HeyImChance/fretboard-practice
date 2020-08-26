import json
import random
from flask import Flask

sharp_notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
flat_notes = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

string_data = json.load(open('strings.json'))

def get_random_sharp():
    return sharp_notes[random.randint(0, len(sharp_notes) - 1 )]

def get_random_flat():
    return flat_notes[random.randint(0, len(flat_notes) - 1)]

print("Find the note: " + get_random_sharp())


def get_note(string_num, fret_num):
    return string_data["strings"][string_num]["frets"][fret_num]

print (get_note(1, 1))


app = Flask(__name__)

@app.route("/")
def hello_name(name):
    return "Hello "+ name

if __name__ == "__main__":
    app.run(debug=True)

