import sqlite3

# # CREAR BASE DE DATOS
# with sqlite3.connect("./bd_test.db") as conexion:
#     try:
#         sentencia = '''CREATE TABLE personajes
#                         (
#                             id INTEGER PRIMARY KEY AUTOINCREMENT,
#                             nombre TEXT,
#                             apellido TEXT,
#                             anio REAL
#                         )
#                     '''
#         conexion.execute(sentencia)
#         print("Se creó la tabla personajes")
#     except sqlite3.OperationalError:
#         print("La tabla personajes ya existe")


# AGREGAR DATOS
# with sqlite3.connect("./bd_test.db") as conexion:
#     try:
#         conexion.execute("insert into personajes(nombre, apellido, anio) values (?,?,?)", ("Renato", "Nani", "1968"))
#         conexion.execute("insert into personajes(nombre, apellido, anio) values (?,?,?)", ("David", "Fernandez", "1994"))
#         conexion.commit() #Actualiza los datos realmente en la tabla
#     except:
#         print("error")

# TRAER DATOS
# with sqlite3.connect("./bd_test.db") as conexion:
#     cursor = conexion.execute("SELECT * FROM personajes")
#     for fila in cursor:
#         print(fila[2]) #Trae apellido


# TRAE DATAO ESPECIFICO
# id = 1
# with sqlite3.connect("./bd_test.db") as conexion:
#     sentencia = "SELECT * FROM personajes WHERE id=? ORDER BY apellido ASC, nombre DESC"
#     cursor = conexion.execute(sentencia,(id,))
#     for fila in cursor:
#         print(fila)


# # MODIFICAR
# id = "7"
# with sqlite3.connect("./bd_test.db") as conexion:
#     sentencia = "UPDATE personajes SET apellido = 'Fernandez' WHERE id=?"
#     cursor = conexion.execute(sentencia,(id,))
#     filas = cursor.fetchall()
#     for fila in filas:
#         print(fila)
#     conexion.commit()

# BORRAR
# with sqlite3.connect("./bd_test.db") as conexion:
#     try:
#         id_a_eliminar = 1  # ID de la fila que deseas eliminar

#         # Utiliza una sentencia SQL DELETE con la cláusula WHERE para eliminar la fila con el ID específico
#         conexion.execute("DELETE FROM personajes WHERE id = ?", (id_a_eliminar,))
#         conexion.commit()
#         print(f"Se eliminó la fila con ID {id_a_eliminar}")
#     except:
#         print("Error al eliminar la fila")


