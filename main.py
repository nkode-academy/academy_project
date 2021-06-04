from flask import Flask, request, redirect, render_template

app = Flask(__name__)

entries = []


@app.route("/")
def hello_world():
    return render_template('home.jinja', entries=reversed(entries), location_types=['Restaurant', 'Hotel', 'Museum', 'Location'])


@app.route("/new_entry", methods=['GET'])
def new_entry():
    global entries

    type_of_new_entry = request.args.get('type')
    title_from_user = request.args.get('title')
    description_from_user = request.args.get('description')

    entries.append({
        "type": type_of_new_entry,
        "title": title_from_user,
        "description": description_from_user
    })

    return redirect("/")


if __name__ == '__main__':
    # this is run when clicking the run button in VSCode
    app.run(host='127.0.0.1', port=8080, debug=True)
