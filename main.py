import requests
import sqlite3


def get_coindesk_data():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    return response.json()


def insert_data_into_database(data):
    conn = sqlite3.connect("coindesk_data.db")
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS coindesk_prices (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        currency VARCHAR(10),
                        rate FLOAT
                    )''')

    # Insert data into the table
    cursor.execute("INSERT INTO coindesk_prices (currency, rate) VALUES (?, ?)",
                   (data["bpi"]["USD"]["code"], data["bpi"]["USD"]["rate_float"]))

    conn.commit()
    conn.close()


coindesk_data = get_coindesk_data()

if __name__ == "__main__":
    insert_data_into_database(coindesk_data)


