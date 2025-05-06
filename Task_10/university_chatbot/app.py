from flask import Flask, render_template, request

app = Flask(__name__)


def get_response(user_input):
    user_input = user_input.lower()
    if "admission" in user_input:
        return "Admissions are open from June to August. You can apply online."
    elif "fee" in user_input:
        return "The tuition fee varies by program. Please visit our website for detailed information."
    elif "courses" in user_input or "programs" in user_input:
        return "We offer undergraduate and postgraduate programs in Engineering, Business, and Arts."
    elif "contact" in user_input:
        return "You can contact us at admissions@university.edu or call +1234567890."
    else:
        return "I'm sorry, I didn't understand that. Please ask about admissions, fees, courses, or contact information."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    return get_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
