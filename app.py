from flask import Flask, render_template, request
import pandas as pd
import pickle

# Create the Flask app
app = Flask(__name__)

# Load the trained model
model_path = "/home/aryan/AI/Project 2/notebooks/xgbreg"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Route for homepage
@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        # Get values from form
        screen_time = float(request.form["screen_time_hours"])
        platforms = int(request.form["social_media_platforms_used"])
        tiktok = float(request.form["hours_on_TikTok"])
        sleep = float(request.form["sleep_hours"])

        # Create input DataFrame
        input_df = pd.DataFrame([{
            "screen_time_hours": screen_time,
            "social_media_platforms_used": platforms,
            "hours_on_TikTok": tiktok,
            "sleep_hours": sleep
        }])

        # Predict
        prediction = model.predict(input_df)[0]

    return render_template("index.html", prediction=prediction)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
