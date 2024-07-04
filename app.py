from flask import Flask, render_template, request, redirect

app = Flask(__name__)

motherboards_json ={
    "motherboards": [
        {
            "brand": "ASUS",
            "model": "ROG Strix Z490-E",
            "price": 299.99
        },
        {
            "brand": "MSI",
            "model": "MPG Z490 Gaming Edge WiFi",
            "price": 199.99
        },
        {
            "brand": "Gigabyte",
            "model": "Z490 AORUS Ultra",
            "price": 329.99
        },
        {
            "brand": "ASRock",
            "model": "Z490 Taichi",
            "price": 289.99
        },
        {
            "brand": "ASUS",
            "model": "TUF Gaming B550-PLUS",
            "price": 169.99
        },
        {
            "brand": "MSI",
            "model": "B450 TOMAHAWK MAX",
            "price": 114.99
        },
        {
            "brand": "Gigabyte",
            "model": "B450 AORUS PRO WIFI",
            "price": 109.99
        },
        {
            "brand": "ASRock",
            "model": "B450M Steel Legend",
            "price": 94.99
        }
    ]
}
@app.route('/') # app es la instancia, route el metodo, '/' es el disparador
def index():
    return render_template(
        'index.html',
    )

@app.route('/products')
def products():
    return render_template(
        'products.html',
        motherboards = motherboards_json
    )

@app.route('/products_add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'GET':
        return render_template(
            'products_add.html',
        )
    if request.method == 'POST':
        data = request.form
        brand = data.get('brand_motherboard')
        model = data.get('model_motherboard')
        price = data.get('price_motherboard')

        new_motherboard = dict(
                brand = brand,
                model = model,
                price = price
        )
        
        motherboards_json.get('motherboards').append(new_motherboard)

        return redirect('products')
    nueva_linea = "1234"