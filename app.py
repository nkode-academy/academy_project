from flask import Flask

app = Flask(__name__)

entries = []


@app.route("/")
def hello_world():
    result = ""
    for entry in entries:
        result += "<p>{title} - {description}</p>".format(
            title=entry["title"],
            description=entry["description"])

    return result


@app.route("/new_entry")
def good_bye():
    global entries

    entries.append({
        "title": "new entry",
        "description": "new description"
    })

    return "Success"
