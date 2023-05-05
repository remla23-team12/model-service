from flask import Flask, request
import joblib
from flasgger import Swagger
import pickle
import preprocess


app = Flask(__name__)
swagger = Swagger(app)

@app.route('/', methods=['POST'])
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
    msg = request.get_json().get('msg')
    classifier = joblib.load('models/classifier_sentiment_model')
    cv = pickle.load(open('bow/bow_sentiment_model.pkl', 'rb'))
    result = classifier.predict(cv.transform([preprocess.preprocess_review(msg)]).toarray())[0]
    return {
        "result": result.item(),
        "message": msg
    }

app.run(host="0.0.0.0", port=8080, debug=True)
