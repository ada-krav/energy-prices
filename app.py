import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return 'To get data for date you need to use next format "http://127.0.0.1:5000/data?date=2023-06-12'


@app.route("/data", methods=["GET"])
def get_data():
    date = request.args.get("date")
    data = read_data_from_database(date)

    if data:
        return jsonify({"data": data})

    return (
        jsonify({"error": "Data not found"}),
        404,
    )


def read_data_from_database(date):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT hour, price, sales_volume, purchase_volume, declared_sales_volume, declared_purchase_volume
        FROM data
        WHERE date = ?
    ''', (date,))

    rows = cursor.fetchall()

    data = {}
    for row in rows:
        hour = row[0]
        price = row[1]
        sales_volume = row[2]
        purchase_volume = row[3]
        declared_sales_volume = row[4]
        declared_purchase_volume = row[5]

        data[hour] = {
            "price": price,
            "sales_volume": sales_volume,
            "purchase_volume": purchase_volume,
            "declared_sales_volume": declared_sales_volume,
            "declared_purchase_volume": declared_purchase_volume
        }

    conn.close()

    return data


if __name__ == "__main__":
    app.run()
