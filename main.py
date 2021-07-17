from flask import Flask, request, redirect, render_template
from data import data_store

app = Flask(__name__)


@app.route("/")
def home():
    entries = data_store.get_entries()
    filter_city = request.args.get('city')
    filtered_entries = []
    if filter_city == None:
        filtered_entries = entries
    else:
        for entry in entries: 
            city = entry['city']
            if city.lower().strip() == filter_city.lower().strip():
                filtered_entries.append(entry)
        

    return render_template(
        'home.html',
        entries=reversed(filtered_entries),
        location_types=[
            'Restaurant',
            'Hotel',
            'Museum',
            'Venues']
    )


@app.route("/details")
def details():
    index = int(request.args.get('index'))
    return render_template('details.html', entry=data_store.get_entry_with_id(index))


@app.route("/new_entry", methods=['GET'])
def new_entry():
    type_of_new_entry = request.args.get('type')
    title_from_user = request.args.get('title')
    city_from_user = request.args.get('city')
    description_from_user = request.args.get('description')
    rating_from_user = request.args.get('rating')

    data_store.add_entry({
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

