from flask import Flask
import json


with open('candidates.json', encoding="utf8") as f:
    items = json.load(f)

def take_person(person:dict)->str:
    result = ""
    name = person["name"]
    position = person["position"]
    skills = person["skills"]
    result += f"Имя кандидата -{name}\nПозиция кандидата {position}\nНавыки {skills}\n\n"
    return result

app = Flask(__name__)
@app.route("/")
def index():
    result = ""
    for i in items:
        result += take_person(i)
    return "<pre>" + result + "<pre>"

@app.route("/profile/<int:uid>")
def page_profile(uid):
    person = None
    for i in items:
        if uid == i["id"]:
            person = i
            break
    if person:
        img = person["picture"]
        info = take_person(person)
        result = f'<img src="{img}">\n<pre>{info}</pre>'
        return result
    return "404 Not found"

@app.route("/skills/<skill>")
def page_skills(skill):
    persons = []
    for i in items:
        if skill.lower() in i["skills"].lower():
            persons.append(i)
    if persons:
        result = ""
        for i in persons:
            result += take_person(i)
        return f"<pre> {result} </pre>"
    return "404 This skill has no anybody"

 # <pre>
 #  Имя кандидата -
 #  Позиция кандидата
 #  Навыки через запятую

app.run()