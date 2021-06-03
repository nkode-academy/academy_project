from flask import Flask, request, redirect, render_template

app = Flask(__name__)

entries = []


@app.route("/")
def hello_world():
    
    return render_template('home.html', entries=entries)


@app.route("/new_entry")
def new_entry():
    global entries

    def type_dropdown():
        types = ['Restaurant', 'Hotel', 'Museum', 'Location']
        return type_of_new_entry

    type_of_new_entry = request.args.get('type')
    title_from_user = request.args.get('title')
    description_from_user = request.args.get('description')

    entries.append({
        "type": type_of_new_entry,
        "title": title_from_user,
        "description": description_from_user
    })


    return redirect("/")
