	from flask import Flask, render_template_string

app = Flask(__name__)

# এটি আপনার ওয়েবসাইটের ডিজাইন (HTML & CSS)
html_design = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>আমার পার্মানেন্ট ওয়েবসাইট</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; text-align: center; }
        .header { background-color: #333; color: white; padding: 40px; }
        .content { background: white; margin: 20px auto; padding: 30px; max-width: 600px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        p { color: #666; font-size: 18px; }
        .btn { background-color: #28a745; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>স্বাগতম আমার স্থায়ী ওয়েবসাইটে!</h1>
        <p>এটি Pydroid 3 এবং Flask দিয়ে তৈরি করা হয়েছে।</p>
    </div>
    <div class="content">
        <h2>আমার সম্পর্কে</h2>
        <p>হ্যালো! আমি মোবাইল দিয়ে কোডিং শিখছি। এটি পাইথন কোড দিয়ে তৈরি আমার জীবনের প্রথম ওয়েবসাইট।</p>
        <a href="#" class="btn">যোগাযোগ করুন</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_design)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
