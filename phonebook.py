import json
import sys


def load_book(path: str) -> list[dict]:
    """Завантажує книгу з JSON-файлу або завершує програму з повідомленням."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            book = json.load(f)
    except FileNotFoundError:
        raise SystemExit(f'Файл {path} не знайдено')
    except json.JSONDecodeError:
        raise SystemExit(f'Файл {path} не є коректним JSON')

    if not isinstance(book, list):
        raise SystemExit("Очікується JSON-список контактів")

    return book


def save_book(book: list[dict], path: str) -> None:
    """Зберігає книгу у JSON-файл."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(book, f, indent=2, ensure_ascii=False)


def add_entry(phonebook: list[dict]) -> None:
    """Додаємо новий контакт."""
    phone = input("Введіть номер телефону: ").strip()
    while True:
        if not phone:
            print("Рядок не може бути пустим")
            phone = input("Введіть номер телефону: ").strip()
        else:
            break
    for contact in phonebook:
        if contact['phone'] == phone:
            print('Телефон вже зайнятий!')
            return
    first_name = input("Введіть ім'я: ").strip()
    while True:
        if not first_name:
            print("Рядок не може бути пустим")
            first_name = input("Введіть ім'я: ").strip()
        else:
            break
    last_name = input("Введіть прізвище: ").strip()
    while True:
        if not last_name:
            print("Рядок не може бути пустим")
            last_name = input("Введіть прізвище: ").strip()
        else:
            break
    city = input("Введіть місто: ").strip()
    state = input("Введіть область: ").strip()

    new_contact = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'city': city,
        'state': state,
    }
    phonebook.append(new_contact)


def print_contact(contact: dict) -> None:
    """Виводить один контакт в один рядок."""
    full_name = f"{contact['first_name']} {contact['last_name']}"
    location = f"{contact['city']}, {contact['state']}"
    print(f"{full_name} | {contact['phone']} | {location}")


def show_all(phonebook: list[dict]) -> None:
    """Виводить усі контакти книги по одному в рядок."""
    if not phonebook:
        print('Книга порожня')
        return
    for contact in phonebook:
        print_contact(contact)


def delete_entry(phonebook: list[dict]) -> None:
    """Видаляє вибраний контакт за номером телефону."""
    phone = input("Введіть номер телефону: ").strip()
    for contact in phonebook:
        if contact['phone'] == phone:
            phonebook.remove(contact)
            return

    print('Такого номера немає')


def update_entry(phonebook: list[dict]) -> None:
    """Оновлення за номером телефону."""
    phone = input("Введіть номер телефону: ").strip()
    for contact in phonebook:
        if contact['phone'] == phone:
            new_first_name = input(f"Нове ім'я ({contact['first_name']}): ").strip()
            new_last_name = input(f"Нове прізвище ({contact['last_name']}): ").strip()
            new_city = input(f"Нове місто ({contact['city']}): ").strip()
            new_state = input(f"Нова область ({contact['state']}): ").strip()
            contact['first_name'] = new_first_name or contact['first_name']
            contact['last_name'] = new_last_name or contact['last_name']
            contact['city'] = new_city or contact['city']
            contact['state'] = new_state or contact['state']
            return

    print("Такого номера немає")


def search(phonebook: list[dict], key: str, prompt: str) -> None:
    """Пошук за одним полем без урахування регістру."""
    query = input(prompt).lower().strip()
    found = False

    for contact in phonebook:
        if contact[key].lower() == query:
            print_contact(contact)
            found = True

    if not found:
        print("Нічого не знайдено")


def search_by_full_name(phonebook: list[dict]) -> None:
    """Пошук за ім'ям та прізвищем."""
    full_name_entry = input("Введіть ім'я та прізвище: ").lower().strip()
    found = False

    for contact in phonebook:
        full_name = f"{contact['first_name']} {contact['last_name']}".lower()
        if full_name == full_name_entry:
            print_contact(contact)
            found = True

    if not found:
        print("Нічого не знайдено")


def search_by_city_or_state(phonebook: list[dict]) -> None:
    """Пошук за містом та областю."""
    query = input("Введіть місто/область: ").lower().strip()
    found = False

    for contact in phonebook:
        if query == contact['city'].lower() or contact['state'].lower() == query:
            print_contact(contact)
            found = True

    if not found:
        print("Нічого не знайдено")


def main() -> None:
    """Запускає меню телефонної книги.

    Назва JSON-файлу береться з першого аргументу командного рядка.
    Після виходу з меню дані зберігаються у цей самий файл.
    """
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python phonebook.py <phonebook.json>')

    path = sys.argv[1]
    phonebook = load_book(path)

    try:
        while True:
            print("""
            1. Додати контакт
            2. Показати всі контакти
            3. Видалити контакт
            4. Оновити дані
            5. Пошук за ім'ям
            6. Пошук за прізвищем
            7. Пошук за повним ім'ям
            8. Пошук за номером телефону
            9. Пошук за містом або областю
            0. Вийти""")
            choice = input('Оберіть пункт: ')

            if choice == '1':
                add_entry(phonebook)
            elif choice == '2':
                show_all(phonebook)
            elif choice == '3':
                delete_entry(phonebook)
            elif choice == '4':
                update_entry(phonebook)
            elif choice == '5':
                search(phonebook, 'first_name', "Введіть ім'я: ")
            elif choice == '6':
                search(phonebook, 'last_name', "Введіть прізвище: ")
            elif choice == '7':
                search_by_full_name(phonebook)
            elif choice == '8':
                search(phonebook, 'phone', "Введіть номер телефону: ")
            elif choice == '9':
                search_by_city_or_state(phonebook)
            elif choice == '0':
                break
            else:
                print('Такого пункту немає')
    except (KeyboardInterrupt, EOFError):
        print("\nВихід зі збереженням")

    save_book(phonebook, path)


if __name__ == "__main__":
    main()
