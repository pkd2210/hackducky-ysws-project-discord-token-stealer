from flask import Flask, request, jsonify
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    if data:
        content = data.get('content', '')
        file = 'tokens.xlsx'
        if os.path.exists(file):
            wb = load_workbook(file)
            ws = wb.active
        else:
            wb = Workbook()
            ws = wb.active
        row = 1
        while ws.cell(row=row, column=1).value is not None:
            row+=1
        ws.cell(row=row, column=1, value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        ws.cell(row=row, column=2, value=content)
        wb.save(file)
        return jsonify({"message": "success"})
    else:
        return jsonify({"message": "error"})

if __name__ == '__main__':
    app.run(debug=False, port=5001)
    hgf