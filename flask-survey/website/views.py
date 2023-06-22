from flask import Blueprint, render_template, redirect, request, session
from surveys import satisfaction_survey


views = Blueprint('views', __name__)

user_responses = 'responses'

@views.route('/')
def home():
    return render_template("survey.html")


@views.route('/start', methods=['POST'])
def start():
    # redirect user to first question 
    session[user_responses] = []
    
    return redirect('/questions/0')


@views.route('/questions/<int:qid>')
def show_question(qid):
    
    #if (len(session.get(user_responses)) == len(satisfaction_survey.questions)):
    #    return redirect('/complete')
    question = satisfaction_survey.questions[qid]
    return render_template('question.html', question = question)


@views.route('/answer', methods=['POST'])
def get_answer():


    
    responses = session[user_responses]
    responses.append(request.form['answer'])

    session[user_responses] = responses

    if (len(responses) == len(satisfaction_survey.questions)):
        return render_template('/complete.html')

    return redirect(f'/questions/{len(session[user_responses])}')




