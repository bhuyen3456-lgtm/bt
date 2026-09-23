from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Biểu đồ số sinh viên nam nữ</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            width: 500px;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        label {
            font-weight: bold;
        }
        input {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        button {
            padding: 10px 15px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #0056b3;
        }
        .chart {
            margin-top: 25px;
            display: flex;
            justify-content: space-around;
            align-items: end;
            height: 260px;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
            background: linear-gradient(to top, #f9fbff, #ffffff);
        }
        .bar-group {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            width: 120px;
        }
        .bar {
            width: 70px;
            border-radius: 8px 8px 0 0;
            display: flex;
            align-items: flex-start;
            justify-content: center;
            color: white;
            font-weight: bold;
            padding-top: 8px;
        }
        .male {
            background: #4dabf7;
        }
        .female {
            background: #ff6b6b;
        }
        .label {
            font-weight: bold;
            color: #333;
        }
        .result {
            margin-top: 20px;
            font-size: 18px;
            color: #333;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Nhập số sinh viên nam nữ</h2>
        <form method="POST">
            <label for="nam">Số sinh viên nam:</label>
            <input type="number" id="nam" name="nam" min="0" required>

            <label for="nu">Số sinh viên nữ:</label>
            <input type="number" id="nu" name="nu" min="0" required>

            <button type="submit">Hiển thị biểu đồ</button>
        </form>

        {% if nam is not none and nu is not none %}
            <div class="result">
                Tổng số sinh viên: {{ nam + nu }}
            </div>
            <div class="chart">
                <div class="bar-group">
                    <div class="bar male" style="height: {{ (nam / max_value * 100) if max_value else 0 }}%;">
                        {{ nam }}
                    </div>
                    <div class="label">Nam</div>
                </div>
                <div class="bar-group">
                    <div class="bar female" style="height: {{ (nu / max_value * 100) if max_value else 0 }}%;">
                        {{ nu }}
                    </div>
                    <div class="label">Nữ</div>
                </div>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    nam = None
    nu = None
    max_value = 0

    if request.method == 'POST':
        nam = int(request.form.get('nam', 0))
        nu = int(request.form.get('nu', 0))
        max_value = max(nam, nu, 1)

    return render_template_string(HTML_PAGE, nam=nam, nu=nu, max_value=max_value)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5175)
