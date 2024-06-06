from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tareas</title>
</head>
<body>
    <h3>Agustina Hernandez Martinez 9B 20200700</h3>
    <img src="https://tiendadepromocionales.com/cdn/shop/products/LIBRETA_GREEN_AZUL_2_1024x1024.PNG?v=1567005662" alt="Libretita" style="width:100px;">
    <h2>Agregar Tarea</h2>
    <form method="POST">
        <label for="tarea">Tarea:</label>
        <input type="text" id="tarea" name="tarea">
        <input type="submit" value="Agregar">
    </form>
    <ul>
        {% for tarea in tareas %}
            <li>{{ tarea }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""
tareas = []
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nueva_tarea = request.form.get('tarea')
        if nueva_tarea:
            tareas.append(nueva_tarea)
    return render_template_string(HTML_TEMPLATE, tareas=tareas)

if __name__ == '__main__':
    app.run(debug=True)
