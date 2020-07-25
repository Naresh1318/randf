import json
from flask import Flask, render_template, jsonify, request


# Change jinja template syntax
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_start_string='%%',
        variable_end_string='%%',
    ))


app = CustomFlask(__name__)
db_path = "data/choices.json"


class ComplexDB:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as f:
            items = json.load(f)["items"]
        self._items = items

    def get(self):
        return self._items

    def set(self, item):
        try:
            self._items.append(item)
            return True
        except:
            return False

    def delete(self, item):
        item_len = len(self._items)
        self._items = [i for i in self._items if i != item]
        return True if item_len < len(self._items) else False

    def commit(self):
        with open(self.path, "w") as f:
            json.dump({"items": self._items}, f)


complex_db = ComplexDB(db_path)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/choices", methods=["GET"])
def choices():
    return jsonify({"items": complex_db.get()})


@app.route("/add", methods=["POST"])
def add():
    item = request.json["item"]
    complex_db.set(item)
    complex_db.commit()
    return jsonify({"INFO": True})


@app.route("/delete", methods=["POST"])
def delete():
    item = request.json["item"]
    done = complex_db.delete(item)
    complex_db.commit()
    return jsonify({"INFO": done})


if __name__ == "__main__":
    app.run(debug=True)
