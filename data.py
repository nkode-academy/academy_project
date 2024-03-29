from flask import Flask, request, redirect, render_template
import csv
import os
import tempfile

ENTRIES_FILE_NAME = 'entries.csv'

IS_APP_ENGINE = os.environ.get('GAE_ENV', None) is not None


class LocalCSVDataStorage:
    def __init__(self):
        self._entries = []
        self._initialize_entries()

    def _initialize_entries(self):
        try:
            input_file = csv.DictReader(open(ENTRIES_FILE_NAME))
            for row in input_file:
                self._entries.append(row)
        except:
            print("No entries file found. Starting with zero entries.")

    def get_entries(self):
        return self._entries

    def get_entry_with_id(self, identifier):
        return self._entries[identifier]

    def add_entry(self, new_entry):
        new_entry["id"] = len(self._entries)
        self._entries.append(new_entry)

        with open(ENTRIES_FILE_NAME, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, self._entries[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(self._entries)


class CloudStorageCSVDataStorage:
    def __init__(self):
        from google.cloud import storage
        self._client = storage.Client()
        self._bucket = self._client.get_bucket(
            os.environ.get('CLOUD_STORAGE_BUCKET'))
        self._initialize_entries()
        self._entries = []

    def _initialize_entries(self):
        try:
            self._entries = []
            blob = self._bucket.get_blob(ENTRIES_FILE_NAME)
            csv_string = blob.download_as_string()
            csv_lines = csv_string.splitlines()
            input_file = csv.DictReader(csv_lines)
            for row in input_file:
                self._entries.append(row)
        except:
            print("No entries file found. Starting with zero entries.")

    def get_entries(self):
        self._initialize_entries()
        return self._entries

    def get_entry_with_id(self, identifier):
        return self._entries[identifier]

    def add_entry(self, new_entry):
        new_entry["id"] = len(self._entries)
        self._entries.append(new_entry)

        with tempfile.NamedTemporaryFile(mode='w') as output_file:
            dict_writer = csv.DictWriter(output_file, self._entries[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(self._entries)
            blob = self._bucket.blob(ENTRIES_FILE_NAME)
            blob.upload_from_filename(output_file.name)


ENTITY_TYPE = "RestiReview"


class CloudDataStorage:
    def __init__(self):
        from google.cloud import datastore
        self._datastore = datastore
        self._client = datastore.Client()

    def get_entries(self):
        query = self._client.query(kind=ENTITY_TYPE)
        return list({**entity, 'id': entity.id} for entity in query.fetch())

    def get_entry_with_id(self, identifier):
        key = self._client.key(ENTITY_TYPE, identifier)
        review = self._client.get(key)
        return review

    def add_entry(self, new_entry):
        identifier = self._client.key(ENTITY_TYPE)
        review = self._datastore.Entity(identifier)
        review.update(new_entry)
        self._client.put(review)


data_store = LocalCSVDataStorage() if not IS_APP_ENGINE else CloudDataStorage()
