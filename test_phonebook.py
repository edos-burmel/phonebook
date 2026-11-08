import json
import pytest
from phonebook import load_book

def test_load_book(tmp_path):
    expected = [{
        "first_name": "John",
        "last_name": "Smith",
        "phone": "0505050505",
        "city": "Boston",
        "state": "Massachusetts"
    }]
    path = tmp_path / "book.json"

    path.write_text(json.dumps(expected, ensure_ascii=False), encoding='utf-8')

    result = load_book(str(path))

    assert result == expected


def test_load_book_file_not_found(tmp_path):
    path = tmp_path / "missing.json"

    with pytest.raises(SystemExit) as error:
        load_book(str(path))

    assert str(error.value) == f'Файл {path} не знайдено'


def test_load_book_invalid_json(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("{'invalid_json': missing_quotes }", encoding='utf-8')

    with pytest.raises(SystemExit) as error:
        load_book(str(path))

    assert str(error.value) == f"Файл {path} не є коректним JSON"


def test_load_book_not_a_list(tmp_path):
    path = tmp_path / "not_a_list.json"
    path.write_text(json.dumps({"invalid_json": []}), encoding='utf-8')

    with pytest.raises(SystemExit) as error:
        load_book(str(path))

    assert str(error.value) == "Очікується JSON-список контактів"