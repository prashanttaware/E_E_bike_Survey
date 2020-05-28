from django.db import migrations
from django.utils import timezone


def add_initial_questions(apps, schema_editor):
    Question = apps.get_model("survey", "Question")
    add_question(
        Question,
        "Which is your location?",
        ["Pune", "Mumbai", "Delhi", "Bengaluru", "Chennai", "Panji","Nagpur","Nashik"],
    )
    add_question(Question, "Your age?",
                 ["15 - 25", "25 - 35", "35 - 45", "45 - 55","55 - 65"])
    add_question(Question, "Do you own electric vehicle?",
                 ["Yes", "No"])
    add_question(Question, "Number of vehicles you own?",
                 ["2", "3", "4", "5"])
    add_question(Question, "Are you planning to buy electric vehicles ?",
                 ["Yes", "No"])
    add_question(Question, "How much will you pay for electric bike(in rs)?",
                 ["40000", "45000","50000","55000","60000"])
    add_question(Question, "Maximum speed of electric vehicle according to you(km/hr)?",
                 ["80", "100","120","140","160"])
    add_question(Question, "Are electric bike dangerous?",
                 ["Yes","No"])
    add_question(Question, "Whats good about electric bike?",
                 ["Environment friendly","Less expensive","Enjoy ridding","Not using fuel"])
    add_question(Question, "Which year are you planning to buy electric bike?",
                 ["2020","2021","2022","2023"])
    add_question(Question, "How far will electric vehicle go when once charge full(km)?",
                 ["100","150","200","250"])
    add_question(Question, "Battery charge cost?",
                 ["100","150","200","250"])
    add_question(Question, "Any electric vehicle showroom near you?",
                 ["Yes","No"])
    add_question(Question, "How cool is this app?", ["👌", "👏", "👍", "👎", "💩"])

def add_question(question_model, question_text, choices) :
    question = question_model(question_text=question_text,
                              pub_date=timezone.now())
    question.save()
    for choice in choices:
        question.choices.create(choice_text=choice)


class Migration(migrations.Migration):

    dependencies = [("survey", "0002_auto_001")]

    operations = [migrations.RunPython(add_initial_questions)]
