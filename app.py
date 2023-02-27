from flask import Flask,request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    fruits=db.all()
    
    html ='<html>'
    html +="""<style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
    </style>"""
    html += '<head><title>Fruit</title></head>'
    html += '<body>'
    html += '<h1>Fruit</h1>'
  
    html += '<table>'
    for fruit in fruits:
        
        html +=f'<tr><th>{fruit["name"]}</th> <th>{fruit["quantity"]}</th>  <th>{fruit["price"]}</th> <th>{fruit["type"]}</th> <tr>'
    html += '</table>'
    html += '</body>'
    html += '</html>'
    return html


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    ali=request.get_json(force=True)
    db.add(ali)
    return 'Qushildi'


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    fruits=db.get_by_type(type)
    
    html ='<html>'
    html +="""<style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
    </style>"""
    html += '<head><title>Fruit</title></head>'
    html += '<body>'
    html += '<h1>Fruit</h1>'
  
    html += '<table>'
    for fruit in fruits:
        
        html +=f'<tr><th>{fruit["name"]}</th> <th>{fruit["quantity"]}</th>  <th>{fruit["price"]}</th> <th>{fruit["type"]}</th> <tr>'
    html += '</table>'
    html += '</body>'
    html += '</html>'
    return html


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    fruits=db.get_by_name(name)
    
    html ='<html>'
    html +="""<style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
    </style>"""
    html += '<head><title>Fruit</title></head>'
    html += '<body>'
    html += '<h1>Fruit</h1>'
  
    html += '<table>'
    for fruit in fruits:
        
        html +=f'<tr><th>{fruit["name"]}</th> <th>{fruit["quantity"]}</th>  <th>{fruit["price"]}</th> <th>{fruit["type"]}</th> <tr>'
    html += '</table>'
    html += '</body>'
    html += '</html>'
    return html


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    fruits=db.get_by_price(price)
    
    html ='<html>'
    html +="""<style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
    </style>"""
    html += '<head><title>Fruit</title></head>'
    html += '<body>'
    html += '<h1>Fruit</h1>'
  
    html += '<table>'
    for fruit in fruits:
        
        html +=f'<tr><th>{fruit["name"]}</th> <th>{fruit["quantity"]}</th>  <th>{fruit["price"]}</th> <th>{fruit["type"]}</th> <tr>'
    html += '</table>'
    html += '</body>'
    html += '</html>'
    return html



if __name__ == '__main__':
    app.run(debug=True)