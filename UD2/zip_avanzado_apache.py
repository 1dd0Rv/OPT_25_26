from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def notas_estudiantes():
    # --- 1. TU LÓGICA DE DATOS (Exactamente igual que tu código) ---
    # Python maneja listas y diccionarios de forma nativa 
    estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
    notas_matematicas = [8, 7, 9, 6]
    notas_fisica = [9, 6, 10, 7]
    notas_quimica = [7, 8, 9, 5]
    resultado_final = {}

    # Procesamiento usando zip() para iterar estructuras [cite: 18]
    for est, mat, fis, qui in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):
        promedio = round((mat + fis + qui) / 3, 2)

        # Lógica de control de flujo (if/elif/else) [cite: 18]
        estado = ""
        if promedio >= 6.5:
            estado = "Aprobado"
        elif promedio >= 5:
            estado = "En recuperación"
        else:
            estado = "Reprobado"

        # Guardamos en el diccionario [cite: 22]
        resultado_final[est] = {
            "Matemáticas": mat,
            "Física": fis,
            "Química": qui,
            "Promedio": promedio,
            "Estado": estado
        }

    # --- 2. LA PRESENTACIÓN (HTML) ---
    # En lugar de print(), inyectamos el diccionario 'resultado_final' en el HTML
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Notas de Estudiantes</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 40px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
            th { background-color: #f2f2f2; }
            tr:hover { background-color: #f5f5f5; }
            .estado-aprobado { color: green; font-weight: bold; }
            .estado-recuperacion { color: orange; font-weight: bold; }
            .estado-reprobado { color: red; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>Boletín de Notas</h1>
        <table>
            <thead>
                <tr>
                    <th>Estudiante</th>
                    <th>Matemáticas</th>
                    <th>Física</th>
                    <th>Química</th>
                    <th>Promedio</th>
                    <th>Estado</th>
                </tr>
            </thead>
            <tbody>
                {% for nombre, datos in resultados.items() %}
                <tr>
                    <td>{{ nombre }}</td>
                    <td>{{ datos['Matemáticas'] }}</td>
                    <td>{{ datos['Física'] }}</td>
                    <td>{{ datos['Química'] }}</td>
                    <td><strong>{{ datos['Promedio'] }}</strong></td>
                    <td>
                        {% if datos['Estado'] == 'Aprobado' %}
                            <span class="estado-aprobado">{{ datos['Estado'] }}</span>
                        {% elif datos['Estado'] == 'En recuperación' %}
                            <span class="estado-recuperacion">{{ datos['Estado'] }}</span>
                        {% else %}
                            <span class="estado-reprobado">{{ datos['Estado'] }}</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """
    
    # Renderizamos la plantilla pasando tus datos calculados
    return render_template_string(html_template, resultados=resultado_final)

if __name__ == "__main__":
    app.run()
