from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

# Create an instance of Flask
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

@app.route('/')
def home():
    mars_data = mongo.db.mission_to_mars.find_one()

    return render_template("index.html", mars_data=mars_data)

@app.route('/scrape')
def scrape_mars():
    
    # Run the scrape function
    mars_dict = mission_to_mars.scrape_mars()

    # Update the Mongo database using update and upsert=True
    mongo.db.mission_to_mars.update({}, mars_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)