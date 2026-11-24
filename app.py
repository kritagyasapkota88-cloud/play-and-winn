from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Play & Win</title>
    </head>
    <body style="background:#080b16;color:white;text-align:center;padding:100px;">
        <h1>PLAY & WIN</h1>
        <h2>Online Lucky Draw Platform</h2>
        <p>Founded by Kritagya Sapkota</p>
        <h3>Coming Soon!</h3>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
