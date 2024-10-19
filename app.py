from flask import Flask, render_template, request
import qrcode
from qrcode.image.pure import PyPNGImage
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['response']
    if url == '':
        e = 'No URL entered. Please enter a valid URL'
        return render_template('error.html', error=e)
    else:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                img = qrcode.make(url, image_factory=PyPNGImage)
                img.save('static/qrcode.png')
                return render_template("qrcode.html")
        except:
            e = "Invalid URL. Please try again"
            return render_template('error.html', error=e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
