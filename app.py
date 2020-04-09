from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# setup mongo connection
# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_dict = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars_dict=mars_dict)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_dict = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)





# connect to mongo db and collection
#db = client.mars
#collection = db.produce

# connect to mongo db and collection

# db = client.store_inventory
# collection = db.produce