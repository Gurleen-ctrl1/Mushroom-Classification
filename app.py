from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and encoders
model = joblib.load("models/mushroom_model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

# Extract feature names (excluding the target 'class')
feature_names = [col for col in label_encoders.keys() if col != "class"]

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error_message = None

    if request.method == "POST":
        try:
            # Collect user inputs
            user_input = {}
            for feature in feature_names:
                user_input[feature] = request.form.get(feature)

            print("Raw User Input:", user_input)  # DEBUGGING

            # Convert categorical inputs to encoded values
            input_data = []
            for feature in feature_names:
                if feature in label_encoders:
                    if user_input[feature] not in label_encoders[feature].classes_:
                        raise ValueError(f"Invalid value for {feature}: {user_input[feature]}")  # Validation check
                    encoded_value = label_encoders[feature].transform([user_input[feature]])[0]
                    input_data.append(encoded_value)
                    print(f"Encoded {feature}: {user_input[feature]} -> {encoded_value}")  # DEBUGGING
                else:
                    input_data.append(int(user_input[feature]))  # If already numeric

            print("Final Encoded Input:", input_data)  # DEBUGGING

            # Convert to NumPy array and reshape
            input_array = np.array(input_data).reshape(1, -1)

            # Make prediction
            prediction_numeric = model.predict(input_array)[0]

            # Decode the prediction back to categorical value
            prediction = "Edible 🍄" if prediction_numeric == 0 else "Poisonous ☠️"

        except Exception as e:
            error_message = f"Error: {str(e)}"
            print("ERROR:", error_message)  # DEBUGGING

    return render_template("index.html", feature_names=feature_names, label_encoders=label_encoders, prediction=prediction, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
