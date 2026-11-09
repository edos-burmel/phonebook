import json
import pytest
from phonebook import load_book, delete_entry


@pytest.fixture
def phonebook():
    return [
        {
            "first_name": "John",
            "last_name": "Smith",
            "phone": "0505050505",
            "city": "Boston",
            "state": "Massachusetts",
        },
        {
            "first_name": "Smitty",
            "last_name": "Smith",
            "phone": "0505050506",
            "city": "Los-Angeles",
            "state": "California",
        },
    ]


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


def test_delete_entry(monkeypatch, phonebook):
    monkeypatch.setattr("builtins.input", lambda _: "0505050505")

    delete_entry(phonebook)

    assert len(phonebook) == 1
    assert phonebook[0]["phone"] == "0505050506"


def test_delete_entry_not_found(monkeypatch, capsys, phonebook):
    before = list(phonebook)

    monkeypatch.setattr("builtins.input", lambda _: "999")

    delete_entry(phonebook)

    captured = capsys.readouterr()

    assert phonebook == before

    assert "Такого номера немає" in captured.out
