from flask import Flask, request, jsonify, render_template
from ocr_processor import process_task
from models import db, OCRResult
import psutil

app = Flask(__name__)
app.config.from_object('settings')
db.init_app(app)

@app.route('/extract_text', methods=['POST'])
def extract_text():     
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    file_path = f"uploads/{file.filename}"
    file.save(file_path)
    text = process_task(file_path)
    result = OCRResult(file_path=file_path, extracted_text=text)
    db.session.add(result)
    db.session.commit()
    return jsonify({'extracted_text': text}), 200

@app.route('/')
def index():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    return render_template('dashboard.html', cpu_usage=cpu_usage, memory_usage=memory_usage)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)