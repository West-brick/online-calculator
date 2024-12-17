import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # 监听 $PORT 环境变量
    app.run(host='0.0.0.0', port=port)
