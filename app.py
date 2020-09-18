# Import Dependencies
from flask import Flask, render_template

# Initialize flask
app = Flask(__name__)

@app.route('/')
def index():
    # Render an index.html template and pass it the data you retrieved from the database
    return render_template("dashboard.html", text="#")

if __name__ == "__main__":
    app.run(debug=False)