from flask import Flask, request

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
def new_entry():
    global entries

    title_from_user = request.args.get('title')
    description_from_user = request.args.get('description')

    entries.append({
        "title": title_from_user,
        "description": description_from_user
    })

    return "Success"
