from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/18Zu55T6VB8i25tv9xlgZ_BZwjVipPNPe', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
