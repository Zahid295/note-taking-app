# app.py

from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api

app = Flask(__name__, static_folder='static')
api = Api(app)

notes = []

class NoteList(Resource):
    def get(self):
        return notes, 200

    def post(self):
        note = request.json.get('note')
        if note:
            notes.append(note)
            return {'message': 'Note added successfully'}, 201
        return {'message': 'No note provided'}, 400

class NoteDetail(Resource):
    def get(self, note_id):
        if 0 <= note_id < len(notes):
            return notes[note_id], 200
        return {'message': 'Note not found'}, 404

    def delete(self, note_id):
        if 0 <= note_id < len(notes):
            note = notes.pop(note_id)
            return {'message': f'Note {note} deleted'}, 200
        return {'message': 'Note not found'}, 404

api.add_resource(NoteList, '/notes')
api.add_resource(NoteDetail, '/notes/<int:note_id>')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
