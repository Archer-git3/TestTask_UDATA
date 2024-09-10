from flask import Flask, render_template, url_for, jsonify, abort
import json

app = Flask(__name__)

with open('desc.json', 'r', encoding='utf-8') as f:
    products_data = json.load(f)

@app.route('/')
def index():
    products = [{'name': product['Навза'], 'url': url_for('get_product', product_name=product['Навза'])} for product in products_data]
    return render_template('index.html', products=products)


@app.route('/all_products/')
def get_all_products():
    return jsonify(products_data)

@app.route('/products/<product_name>')
def get_product(product_name):
    product = next((item for item in products_data if item['Навза'].lower() == product_name.lower()), None)
    if product:
        return render_template('product.html', product=product)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
