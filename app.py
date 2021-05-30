from flask import Flask, request, redirect, render_template

app = Flask(__name__)

entries = []


@app.route("/")
def home():
    return render_template('home.html', entries=entries)


@app.route("/new_entry")
def new_entry():
    global entries

    title_from_user = request.args.get('title')
    description_from_user = request.args.get('description')

    entries.append({
        "title": title_from_user,
        "description": description_from_user
    })

    return redirect("/")
