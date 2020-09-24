import torch
import os
import time
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

#Creating a wtform for the page
class InputsForm(FlaskForm):
    query = StringField("Query")
    context = TextAreaField("Context")
    submit = SubmitField("Compute")


app = Flask(__name__)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-distilled-squad")
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased-distilled-squad")

#ensuring that we can reach the page directly from the ip or the index page
@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"]) 
def index():
    answer = {"val": "", "time": ""} # to record the time and value
    form = InputsForm(meta={'csrf':False}) #initializing the form object
    # if we get a post request with the form
    if form.validate_on_submit():
        query = form.query.data
        context = form.context.data
        start_time = time.time()
        inputs = tokenizer.encode_plus(query, context, return_tensors="pt") # inputs are tokenized
        answer_start_scores, answer_end_scores = model(**inputs)
        answer_start = torch.argmax(answer_start_scores) # index with maximum probability
        answer_end = torch.argmax(answer_end_scores) + 1
        result = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end])) # tokenizer is used to convert token ids back to tokens
        end_time = time.time()
        answer["val"] = result
        answer["time"] = "Computed in: " + str(end_time - start_time)

    return render_template('index.html', answer=answer, form=form)
