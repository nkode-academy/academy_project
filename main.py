from flask import Flask, request, redirect, render_template

app = Flask(__name__)

entries = []


@app.route("/")
def home():
    return render_template('home.html', entries=reversed(entries), location_types=['Restaurant', 'Hotel', 'Museum', 'Venues'])


@app.route("/details")
def details():
    title = request.args.get('title')
    description = request.args.get('description')

    return render_template('details.html', title=title, description=description)


@app.route("/new_entry", methods=['GET'])
def new_entry():
    global entries

    type_of_new_entry = request.args.get('type')
    title_from_user = request.args.get('title')
    city_from_user = request.args.get('city')
    description_from_user = request.args.get('description')

    entries.append({
        "type": type_of_new_entry,
        "title": title_from_user,
        "city": city_from_user,
        "description": description_from_user
    })

    return redirect("/")


if __name__ == '__main__':
    # this is run when clicking the run button in VSCode
    app.run(host='127.0.0.1', port=8080, debug=True)
