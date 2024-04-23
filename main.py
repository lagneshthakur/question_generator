from flask import Flask, request
from question_generator import question_generator_pipeline
from multiple_question_generator import generate_multiple_questions

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/generate_question")
def generate_question():
    query = request.args
    for key,value in query.items():
        # Return question for the given text in the query
        if key == 'text':
            question = question_generator_pipeline.invoke(value)
            return {'question': question}

@app.route("/generate_questions")
def generate_multiple_question():
    query = request.args
    for key,value in query.items():
      # Return questions for the given text in the query
      if key == 'text':
        question_list = generate_multiple_questions(value)
        return {'questions': question_list}

if __name__ == '__main__':
    app.run(debug=True, port=8001)