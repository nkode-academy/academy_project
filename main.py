from flask import Flask, request, redirect, render_template
from data import add_entry, get_entries, get_entry_with_id

app = Flask(__name__)


@app.route("/")
def home():
    entries = get_entries()
    return render_template(
        'home.html',
        entries=reversed(entries),
        location_types=[
            'Restaurant',
            'Hotel',
            'Museum',
            'Venues']
    )


@app.route("/details")
def details():
    index = int(request.args.get('index'))
    return render_template('details.html', entry=get_entry_with_id(index))


@app.route("/new_entry", methods=['GET'])
def new_entry():
    type_of_new_entry = request.args.get('type')
    title_from_user = request.args.get('title')
    city_from_user = request.args.get('city')
    description_from_user = request.args.get('description')
    rating_from_user = request.args.get('rating')

    add_entry({
        "type": type_of_new_entry,
        "title": title_from_user,
        "city": city_from_user,
        "description": description_from_user,
        "rating": rating_from_user
    })

    return redirect("/")


if __name__ == '__main__':
    # this is run when clicking the run button in VSCode
    app.run(host='127.0.0.1', port=8080, debug=True)
