import requests
import sqlite3
import json


def request_cat_facts():
    count = int(input("რამდენი ფაქტი გსურთ კატების შესახებ? "))
    url = f'https://meowfacts.herokuapp.com/?count={count}'
    response = requests.get(url)
    info = json.loads(response.text)
    header = response.headers #სამწუხაროდ, ჰედერის არაინფორმატიულობის გამო მისი გამოყენება ვერსად ვერ მოვახერხე.
    status_code = response.status_code

    if status_code == 200:
        return info
    else:
        return f'სამწუხაროდ API-სთან კავშირის დამყარება ვერ მოხერხდა. შეცდომის კოდია {status_code}'


def save_into_file():

    data = request_cat_facts()

    if data:
        with open('facts_about_cat.json', 'w') as file:
            json.dump(data, file, indent=3)
        print("ფაილში მონაცემების ჩაწერა წარმატებით განხორციელდა!")

    else:
        print("ფაილში მონაცემების ჩაწერა ვერ მოხერხდა!")



def display_facts():
    data = request_cat_facts()

    if data:
        info = data['data']
        for index, item in enumerate(info, start=1):
            print(f'{index}. {item}')

    else:
        print("მონაცემების ჩვენება ვერ მოხერხდა!")


#მონაცემთა ბაზაში ინახება ის ფაქტები, რომელსაც API-სგან წამოვიღებთ.
#ბაზაში განსაზღვრულია ფაქტისთვის დამახასიათებელი უნიკალური ID და VARCHAR ტიპის გრაფა, რომელშიც თვითონ ფაქტი ჩაიწერება
def save_into_database():
    data = request_cat_facts()

    if data:
        data = request()["data"]
        conn = sqlite3.connect('Cats_facts.sqlite')
        cursor = conn.cursor()

        cursor.execute('''
    CREATE TABLE IF NOT EXISTS cats_facts
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Facts VARCHAR(400)
    )''')

        facts = [(fact,) for fact in data]
        cursor.executemany('''INSERT INTO cats_facts (Facts) VALUES (?)''', facts)

        conn.commit()
        conn.close()

    else:
        print("მონაცემების ბაზაში შეტანა ვერ მოხერხდა!")


if __name__ == '__main__':
    def main():
        display_facts()
        save_into_file()
        save_into_database()

main()
