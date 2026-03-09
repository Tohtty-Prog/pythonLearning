import os
import json

class NoteStorage:

    def __init__(self,filename = "notes.json"):
        self.filename = filename
        self.check_file()
    
    def check_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({"notes": []}, f)

    def load_data(self):
        with open(self.filename, "r") as f:
            return json.load(f)
        
    def save_data(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def get_next_id(self):
        data = self.load_data()
        if not data["notes"]:
            return 1
        return data["notes"][-1]["id"] + 1
    
    def get_notes(self):
        data = self.load_data()
        return data["notes"]
    
    def add_note(self, note_data):
        data = self.load_data()

        note_data["id"] = self.get_next_id()

        data["notes"].append(note_data)

        self.save_data(data)

        return note_data
    
