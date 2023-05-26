from flask import Flask, request
import joblib
from flasgger import Swagger
import pickle
import preprocess
import os
import remla12_lib_release.version_util as version_util

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/", methods=["POST"])
def predict():
    """
    Make a hardcoded prediction
    ---
    consumes:
      - application/json
    parameters:
        - name: input_data
          in: body
          description: message to be classified.
          required: True
          schema:
            type: object
            required: sms
            properties:
                msg:
                    type: string
                    example: This is an example msg.
    responses:
      200:
        description: Some result
    """
    msg = request.get_json().get("msg")
    # print(msg)
    script_dir = os.path.dirname(os.path.realpath(__file__))

    classifier_name = "tfidf_svm_classifier_sentiment_model"
    textual_represenation_path = "tfidf_svm_sentiment_model.pkl"
    classifier_path = os.path.join(script_dir, "models", classifier_name)
    classifier = joblib.load(classifier_path)

    cv_path = os.path.join(script_dir, "tfidf", textual_represenation_path)
    cv = pickle.load(open(cv_path, "rb"))

    # classifier = joblib.load('models/classifier_sentiment_model')
    # cv = pickle.load(open('bow/bow_sentiment_model.pkl', 'rb'))
    result = classifier.predict(
        cv.transform([preprocess.preprocess_review(msg)]).toarray()
    )[0]
    return {
        "result": result.item(),
        "message": msg,
        "lib_version": version_util.get_version(),
        "classifier": classifier_name,
        "textual_representation_model": textual_represenation_path,
    }


app.run(host="0.0.0.0", port=8080, debug=True)
