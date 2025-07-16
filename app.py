from flask import Flask, render_template, request, jsonify, redirect
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime

app = Flask(__name__)

# ✅ Connect to DynamoDB (make sure AWS CLI is configured)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Expenses')  # ✅ Your working table name

# ✅ Home Page
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Set Monthly Budget
@app.route('/set-budget', methods=['POST'])
def set_budget():
    amount = int(request.form.get('budget'))
    month = datetime.now().strftime("%Y-%m")

    table.put_item(Item={
        'PK': f'BUDGET#{month}',
        'SK': 'INFO',
        'amount': amount
    })

    return redirect('/')

# ✅ Add a new expense
@app.route('/add-expense', methods=['POST'])
def add_expense():
    category = request.form.get('category')
    amount = int(request.form.get('amount'))
    date = request.form.get('date') or datetime.now().strftime("%Y-%m-%d")
    description = request.form.get('description', '')
    month = datetime.now().strftime("%Y-%m")

    table.put_item(Item={
        'PK': f'EXPENSE#{month}',
        'SK': f'{date}#{category}#{datetime.now().timestamp()}',
        'amount': amount,
        'category': category,
        'date': date,
        'description': description
    })

    return redirect('/')

# ✅ Dashboard Summary API (budget, spent, remaining)
@app.route('/summary')
def summary():
    month = datetime.now().strftime("%Y-%m")

    # Get monthly budget
    budget_item = table.get_item(
        Key={'PK': f'BUDGET#{month}', 'SK': 'INFO'}
    )
    budget = budget_item.get('Item', {}).get('amount', 0)

    # Get all expenses
    response = table.query(
        KeyConditionExpression=Key('PK').eq(f'EXPENSE#{month}')
    )
    expenses = response.get('Items', [])
    spent = sum(item.get('amount', 0) for item in expenses)

    return jsonify({
        'budget': budget,
        'spent': spent,
        'remaining': max(0, budget - spent)
    })

# ✅ API to get all expenses (for charts and recent)
@app.route('/expenses')
def get_expenses():
    month = datetime.now().strftime("%Y-%m")

    response = table.query(
        KeyConditionExpression=Key('PK').eq(f'EXPENSE#{month}')
    )
    items = response.get('Items', [])

    # Sort recent first
    sorted_items = sorted(items, key=lambda x: x['date'], reverse=True)

    return jsonify({'expenses': sorted_items})

# ✅ Run Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
