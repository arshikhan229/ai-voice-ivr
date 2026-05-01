from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True) or {}

    # ===== Dialogflow request =====
    if 'queryResult' in data:
        intent = data.get('queryResult', {}).get('intent', {}).get('displayName', 'unknown')

        if intent == "Support":
            reply = "Connecting you to support"
        elif intent == "Sales":
            reply = "Connecting you to sales"
        elif intent == "Billing":
            reply = "I understand you have a billing issue. Please tell me more."
        else:
            reply = "Sorry, I did not understand"

        return jsonify({"fulfillmentText": reply})

    # ===== Twilio request =====
    else:
        speech = request.form.get('SpeechResult')

        if speech:
            speech = speech.lower()

            if "support" in speech:
                reply = "Connecting you to support"
            elif "sales" in speech:
                reply = "Connecting you to sales"
            elif "billing" in speech:
                reply = "I understand you have a billing issue. Please tell me more."
            else:
                reply = "Sorry, I did not understand"
        else:
            reply = "I did not hear anything. Please try again."

        # 🔥 Continuous conversation (UPDATED PART)
        twiml = f"""
<Response>
    <Gather input="speech" action="/webhook" method="POST">
        <Say>{reply}</Say>
    </Gather>
</Response>
"""
        return Response(twiml, mimetype='text/xml')


@app.route('/menu', methods=['POST', 'GET'])
def menu():
    twiml = """
<Response>
  <Gather input="speech" action="/webhook" method="POST">
    <Say>Welcome. How can I help you today?</Say>
  </Gather>
</Response>
"""
    return Response(twiml, mimetype='text/xml')


if __name__ == '__main__':
    app.run(port=5000)