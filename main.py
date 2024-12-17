from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

SONGS_DB = [
    {"id": 1, "title": "Like a Rolling Stone", "artist": "Bob Dylan"},
    {"id": 2, "title": "Imagine", "artist": "John Lennon"},
    {"id": 3, "title": "Smells Like Teen Spirit", "artist": "Nirvana"},
    {"id": 4, "title": "Comfortably Numb", "artist": "Pink Floyd"}
]

@app.route('/')
def home():
    return render_template('index.html', songs=SONGS_DB)

@app.route('/api/songs', methods=['GET'])
def get_songs():
    return jsonify(SONGS_DB)

@app.route('/api/songs', methods=['POST'])
def add_song():
    new_song = request.json
    new_song['id'] = len(SONGS_DB) + 1
    SONGS_DB.append(new_song)
    return jsonify(new_song), 201

@app.route('/api/songs/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    global SONGS_DB
    SONGS_DB = [song for song in SONGS_DB if song['id'] != song_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
