from flask import Flask, request

app = Flask(__name__)

entries = []


@app.route("/")
def hello_world():
    result = """<form action="/new_entry">
    <label for="title">Title:</label><br>
    <input type="text" id="title" name="title"><br>
    <label for="description">Description:</label><br>
    <input type="text" id="description" name="description">
    <input type="submit" value="Submit">
    </form>"""

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
