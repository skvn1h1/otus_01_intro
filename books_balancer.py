import csv
import json
import sys


def read_books(path):
    with open(path, encoding='utf-8') as file:
        return [
            {
                'title': row['Title'],
                'author': row['Author'],
                'pages': int(row['Pages']),
                'genre': row['Genre'],
            }
            for row in csv.DictReader(file)
        ]


def read_users(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def main():
    books = read_books(sys.argv[1])
    users = read_users(sys.argv[2])
    base, extra = divmod(len(books), len(users))

    result = []
    cursor = 0
    for index, user in enumerate(users):
        count = base + 1 if index < extra else base
        result.append({
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': books[cursor:cursor + count],
        })
        cursor += count

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
