from flask import Flask, request, redirect, render_template
import csv

entries = []

ENTRIES_FILE_NAME = 'entries.csv'


def initialize_entries():
    try:
        input_file = csv.DictReader(open(ENTRIES_FILE_NAME))
        for row in input_file:
            entries.append(row)
    except:
        print("No entries file found. Starting with zero entries.")


def get_entries():
    return entries


def get_entry_with_id(identifier):
    return entries[identifier]


def add_entry(new_entry):
    new_entry["id"] = len(entries)
    entries.append(new_entry)

    with open(ENTRIES_FILE_NAME, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, entries[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(entries)


initialize_entries()
