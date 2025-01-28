from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

# تحديد مجلد حفظ الصور
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# تأكيد حجم الصورة المسموح به (اختياري)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    file = request.files['image']
    filename = secure_filename(file.filename)  # تأمين اسم الملف

    try:
        # فتح الصورة باستخدام مكتبة Pillow
        image = Image.open(file)
        # التحقق من نوع الصورة
        if image.format not in ['JPEG', 'PNG', 'GIF', 'BMP']:
            return jsonify({"error": "Invalid image file type"}), 400
        
        width, height = image.size  # استخراج أبعاد الصورة
        
        # حفظ الصورة في مجلد static/images
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(file_path)

        # العودة برسالة تؤكد نجاح رفع الصورة مع معلومات عنها
        return jsonify({
            "message": "Image uploaded successfully",
            "filename": filename,
            "width": width,
            "height": height
        })
    except Exception as e:
        return jsonify({"error": f"Unable to process image: {str(e)}"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5002)
