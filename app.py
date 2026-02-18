
@app.route('/captures')
def captures():
    """Return a JSON list of capture files and their paths."""
    capture_path = 'path/to/capture_directory'  # replace with your capture directory path
    capture_files = os.listdir(capture_path)
    return jsonify({'capture_path': capture_path, 'files': capture_files})

