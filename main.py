# Загружаем Flask
from flask import Flask, render_template

# Загружаем функции
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

# Задаём экземпляр Flask
app = Flask(__name__)


@app.route("/")
def main_page():
    """
    Функция возвращает список кандидатов, с ссылками на их страницы
    """
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:idx>")
def candidate_page(idx):
    """
    Функция возвращает страницу кандидата по его id
    """
    candidate = get_candidate(idx)
    if not candidate:
        return "Кандидат не найден"
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidate_by_name_page(candidate_name):
    """
    Функция возвращает страницу с кандидатами по указанному имени
    """
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def search_candidate_by_skill_page(skill_name):
    """
    Функция возвращает страницу с кандидатами по указанному навыку
    """
    candidates = get_candidates_by_skill(skill_name)
    return render_template("search.html", scill=skill_name, candidates=candidates)


app.run(host='127.0.0.1', port=4999)
