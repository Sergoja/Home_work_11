# Загружаем библиотеку json
import json


def load_candidates_from_json():
    """
    Функция возвращает список кандидатов
    """
    with open("candidates.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id: int):
    """
    Функция возвращает кандидата по его id
    """
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str):
    """
    Функция возвращает кандидата по имени
    """
    result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name: str):
    """
    Функция возвращает кандидата по навыку
    """
    result = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
