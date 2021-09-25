from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello this is the new version!"
	
if __name__ == '__main__':
	PORT = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=PORT, debug=False)
