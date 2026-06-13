from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
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

    cursor.execute(
        "SELECT * FROM estudiantes ORDER BY id DESC"
    )

    estudiantes = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(estudiantes)

@app.route('/estudiantes/<int:id>', methods=['GET'])
def obtener_estudiante(id):

    try:

        conn = conectar_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM estudiantes WHERE id=%s",
            (id,)
        )

        estudiante = cursor.fetchone()

        cursor.close()
        conn.close()

        if not estudiante:
            return jsonify({
                "error": "Estudiante no encontrado"
            }), 404

        return jsonify(estudiante)

    except Error as e:

        return jsonify({
            "error": str(e)
        }), 400
    
def validar_estudiante(datos):

    if not datos:
        return "No se recibieron datos"

    if not datos.get('nombre', '').strip():
        return "El nombre es obligatorio"

    if not datos.get('apellido', '').strip():
        return "El apellido es obligatorio"

    try:
        edad = int(datos['edad'])
    except:
        return "La edad debe ser numérica"

    if edad <= 0:
        return "La edad debe ser mayor que cero"

    if edad > 120:
        return "La edad no es válida"

    return None

@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():

    try:
        datos = request.json

        error = validar_estudiante(datos)

        if error:
            return jsonify({
                "error": error
            }), 400


        print("DATOS RECIBIDOS:", datos)

        conn = conectar_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM estudiantes WHERE cedula = %s",
            (datos['cedula'],)
        )

        estudiante = cursor.fetchone()

        if estudiante:
            cursor.close()
            conn.close()

            return jsonify({
                "error": "La cédula ya está registrada"
            }), 400
            
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

        if cursor.rowcount == 0:
                cursor.close()
                conn.close()

                return jsonify({
                    "error": "Estudiante no encontrado"
                }), 404

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({
                "mensaje":"Estudiante agregado correctamente v2"
            })

    except Error as e:

        return jsonify({
            "error": str(e)
        }),400


@app.route('/estudiantes/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):

    try:
        datos = request.json

        error = validar_estudiante(datos)

        if error:
            return jsonify({
                "error": error
            }), 400

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

        if cursor.rowcount == 0:
            cursor.close()
            conn.close()

            return jsonify({
                "error": "Estudiante no encontrado"
            }), 404
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({
            "mensaje":"Estudiante actualizado correctamente"
        })

    except Error as e:

        return jsonify({
            "error": str(e)
        }), 400


@app.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):

    try:

        conn = conectar_db()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM estudiantes WHERE id=%s",
            (id,)
        )

        if cursor.rowcount == 0:
            cursor.close()
            conn.close()

            return jsonify({
                "error": "Estudiante no encontrado"
            }), 404

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({
            "mensaje":"Estudiante eliminado correctamente"
        })

    except Error as e:

        return jsonify({
            "error": str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
