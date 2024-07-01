from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Static wordsearch grid (10x10)
wordsearch_grid = [
    [{'letter': 'A', 'col': 0}, {'letter': 'L', 'col': 1}, {'letter': 'P', 'col': 2}, {'letter': 'H', 'col': 3}, {'letter': 'A', 'col': 4}, {'letter': 'B', 'col': 5}, {'letter': 'E', 'col': 6}, {'letter': 'T', 'col': 7}, {'letter': 'G', 'col': 8}, {'letter': 'D', 'col': 9}],
    [{'letter': 'Q', 'col': 0}, {'letter': 'E', 'col': 1}, {'letter': 'G', 'col': 2}, {'letter': 'W', 'col': 3}, {'letter': 'X', 'col': 4}, {'letter': 'P', 'col': 5}, {'letter': 'M', 'col': 6}, {'letter': 'I', 'col': 7}, {'letter': 'N', 'col': 8}, {'letter': 'O', 'col': 9}],
    [{'letter': 'E', 'col': 0}, {'letter': 'L', 'col': 1}, {'letter': 'E', 'col': 2}, {'letter': 'P', 'col': 3}, {'letter': 'H', 'col': 4}, {'letter': 'A', 'col': 5}, {'letter': 'N', 'col': 6}, {'letter': 'T', 'col': 7}, {'letter': 'Z', 'col': 8}, {'letter': 'Q', 'col': 9}],
    [{'letter': 'T', 'col': 0}, {'letter': 'A', 'col': 1}, {'letter': 'E', 'col': 2}, {'letter': 'E', 'col': 3}, {'letter': 'B', 'col': 4}, {'letter': 'N', 'col': 5}, {'letter': 'P', 'col': 6}, {'letter': 'W', 'col': 7}, {'letter': 'O', 'col': 8}, {'letter': 'P', 'col': 9}],
    [{'letter': 'H', 'col': 0}, {'letter': 'S', 'col': 1}, {'letter': 'L', 'col': 2}, {'letter': 'D', 'col': 3}, {'letter': 'G', 'col': 4}, {'letter': 'A', 'col': 5}, {'letter': 'Y', 'col': 6}, {'letter': 'K', 'col': 7}, {'letter': 'L', 'col': 8}, {'letter': 'Z', 'col': 9}],
    [{'letter': 'Y', 'col': 0}, {'letter': 'E', 'col': 1}, {'letter': 'S', 'col': 2}, {'letter': 'T', 'col': 3}, {'letter': 'E', 'col': 4}, {'letter': 'R', 'col': 5}, {'letter': 'D', 'col': 6}, {'letter': 'A', 'col': 7}, {'letter': 'Y', 'col': 8}, {'letter': 'X', 'col': 9}],
    [{'letter': 'J', 'col': 0}, {'letter': 'K', 'col': 1}, {'letter': 'N', 'col': 2}, {'letter': 'M', 'col': 3}, {'letter': 'O', 'col': 4}, {'letter': 'P', 'col': 5}, {'letter': 'Q', 'col': 6}, {'letter': 'R', 'col': 7}, {'letter': 'S', 'col': 8}, {'letter': 'T', 'col': 9}],
    [{'letter': 'U', 'col': 0}, {'letter': 'V', 'col': 1}, {'letter': 'W', 'col': 2}, {'letter': 'X', 'col': 3}, {'letter': 'Y', 'col': 4}, {'letter': 'Z', 'col': 5}, {'letter': 'A', 'col': 6}, {'letter': 'B', 'col': 7}, {'letter': 'C', 'col': 8}, {'letter': 'D', 'col': 9}],
    [{'letter': 'B', 'col': 0}, {'letter': 'E', 'col': 1}, {'letter': 'P', 'col': 2}, {'letter': 'P', 'col': 3}, {'letter': 'I', 'col': 4}, {'letter': 'Z', 'col': 5}, {'letter': 'Z', 'col': 6}, {'letter': 'A', 'col': 7}, {'letter': 'R', 'col': 8}, {'letter': 'T', 'col': 9}],
    [{'letter': 'L', 'col': 0}, {'letter': 'M', 'col': 1}, {'letter': 'N', 'col': 2}, {'letter': 'O', 'col': 3}, {'letter': 'P', 'col': 4}, {'letter': 'Q', 'col': 5}, {'letter': 'R', 'col': 6}, {'letter': 'S', 'col': 7}, {'letter': 'T', 'col': 8}, {'letter': 'U', 'col': 9}]
]

# List to store collected times and names
times_collected = []

@app.route('/')
def index():
    return render_template('index.html', wordsearch_grid=wordsearch_grid, times_collected=times_collected)

@app.route('/submit_time', methods=['POST'])
def submit_time():
    data = request.json
    name = data['name']
    time_taken = data['time']
    times_collected.append({'name': name, 'time': time_taken})
    return jsonify({'message': 'Time submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
