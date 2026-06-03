from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

DB_CONFIG = {
    "host": "mysql-trainee115.alwaysdata.net",
    #"port": 3306,
    "user": "trainee115",
    "password": "clase1234",
    "database": "trainee115_registroestudiantes"
}

def conectar_db():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():

    conn = conectar_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM estudiantes ORDER BY id DESC")

    estudiantes = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(estudiantes)

@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():

    try:

        datos = request.json

        print("DATOS RECIBIDOS:", datos)

        conn = conectar_db()
        cursor = conn.cursor()

        sql = """
        INSERT INTO estudiantes
        (nombre, apellido, cedula, edad, curso)
        VALUES (%s,%s,%s,%s,%s)
        """

        valores = (
            datos['nombre'],
            datos['apellido'],
            datos['cedula'],
            datos['edad'],
            datos['curso']
        )

        cursor.execute(sql, valores)

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({
            "mensaje":"Estudiante agregado correctamente"
        })

    except Error as e:

        return jsonify({
            "error": str(e)
        }),400


@app.route('/estudiantes/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):

    datos = request.json

    conn = conectar_db()
    cursor = conn.cursor()

    sql = """
    UPDATE estudiantes
    SET nombre=%s,
        apellido=%s,
        cedula=%s,
        edad=%s,
        curso=%s
    WHERE id=%s
    """

    valores = (
        datos['nombre'],
        datos['apellido'],
        datos['cedula'],
        datos['edad'],
        datos['curso'],
        id
    )

    cursor.execute(sql, valores)

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "mensaje":"Estudiante actualizado correctamente"
    })


@app.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM estudiantes WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "mensaje":"Estudiante eliminado correctamente"
    })


if __name__ == '__main__':
    app.run(debug=True)