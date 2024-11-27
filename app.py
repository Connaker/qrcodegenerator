from flask import Flask, render_template, request
import qrcode
from qrcode.image.pure import PyPNGImage
import requests


"""
    This program creates a qrcode based on a website submitted.

    This program is broken into 2 functions
    index: renders the index.html page
    generate: Retrieves the POST dta from index.html form. Creates a qrcode based on the url
"""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['response']
    """
        IF statement veriefs if an input was given, otherwise errors out.
        try/except used to identify errors.
        IF statement used to verify the URL is valid and if it is, creates the QR code
    """
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
    app.run(host='0.0.0.0', port=5000, debug=True)
