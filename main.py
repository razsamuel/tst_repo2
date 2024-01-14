from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def read_file_content(file_name):
    # Potentially vulnerable code
    file_path = os.path.join('/path/to/files', file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

@app.route('/api/readfile', methods=['POST'])
def api_read_file():
    try:
        user_input = request.json['file_name']
        # Potentially vulnerable code: using user input in a filesystem operation
        file_content = read_file_content(user_input)
        return jsonify({'success': True, 'content': file_content})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
