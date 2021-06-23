from flask import Flask, request, redirect, render_template
import csv

app = Flask(__name__)

entries = []

try:
    input_file = csv.DictReader(open("entries.csv"))
    for row in input_file:
        entries.append(row)
except:
    print("No entries file found. Starting with zero entries.")


@app.route("/")
def home():
    return render_template('home.html', entries=reversed(entries), location_types=['Restaurant', 'Hotel', 'Museum', 'Venues'])


@app.route("/details")
def details():
    index = int(request.args.get('index'))

    return render_template('details.html', entry=entries[index])


@app.route("/new_entry", methods=['GET'])
def new_entry():
    global entries

    type_of_new_entry = request.args.get('type')
    title_from_user = request.args.get('title')
    city_from_user = request.args.get('city')
    description_from_user = request.args.get('description')
    rating_from_user = request.args.get('rating')

    entries.append({
        "id": len(entries),
        "type": type_of_new_entry,
        "title": title_from_user,
        "city": city_from_user,
        "description": description_from_user,
        "rating": rating_from_user
    })

    with open('entries.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, entries[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(entries)

    return redirect("/")


if __name__ == '__main__':
    # this is run when clicking the run button in VSCode
    app.run(host='127.0.0.1', port=8080, debug=True)
