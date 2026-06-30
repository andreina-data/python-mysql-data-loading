# Importar librerías necesarias. NO SE DEBE IMPORTAR NINGUNA OTRA LIBRERÍA.
import mysql.connector as db

# Conexión a la base de datos
conn = db.connect(
  host="localhost",
  user="root",
  password="mysql123", # Cambiar por la contraseña de su base de datos
  database="mp2"
)

# Crear cursor
cursor = conn.cursor()

# NO TOCAR. Función que encapsula lógica para ejecutar una consulta y mostrar los resultados.
def run_query(query, header):
  if not query or query == '':
    print("No se definió consulta para ejecutar")
    return
  try:
    cursor.execute(query)
    rows = cursor.fetchall()
    print(header + '\n')
    for row in rows:
      print(row)
  except Exception as e:
    print('Consulta resultó en error: ' + str(e))


# ---------- CONSULTA 1 ----------
# RELLENAR SOLAMENTE LA VARIABLE consulta_1
consulta_1 = """SELECT COUNT(*)
                FROM pedidos
                JOIN clientes ON pedidos.id_cliente = clientes.id
                WHERE clientes.email= 'jessicaflores@example.com';"""

print('\n\n' + '-'*10 + ' INICIO CONSULTA 1 ' + '-'*10 + '\n')
run_query(consulta_1, 'Número de pedidos realizados por cliente con email jessicaflores@example.com:')
print('\n' + '-'*10 + ' FIN CONSULTA 1 ' + '-'*10 + '\n')


# ---------- CONSULTA 2 ----------
# RELLENAR SOLAMENTE LA VARIABLE consulta_2
consulta_2 = """SELECT productos_pedidos.id_producto, productos.nombre, productos.precio, productos_pedidos.cantidad
                FROM productos_pedidos
                JOIN productos ON productos_pedidos.id_producto = productos.id
                WHERE productos_pedidos.id_pedido = 2
                ORDER BY productos_pedidos.id_producto ASC;"""

print('\n\n' + '-'*10 + ' INICIO CONSULTA 2 ' + '-'*10 + '\n')
run_query(consulta_2, 'id, nombre, precio y cantidad de productos solicitados en pedido con id 2:')
print('\n' + '-'*10 + ' FIN CONSULTA 2 ' + '-'*10 + '\n')


# ---------- CONSULTA 3 ----------
# RELLENAR SOLAMENTE LA VARIABLE consulta_3
consulta_3 = """ SELECT pedidos.id, pedidos.direccion, pedidos.detalle, pedidos.fecha
                FROM pedidos
                JOIN productos_pedidos ON pedidos.id = productos_pedidos.id_pedido
                JOIN productos ON productos_pedidos.id_producto = productos.id
                WHERE productos.nombre = 'Tablet'
                AND pedidos.fecha BETWEEN '2024-01-05' AND '2024-01-07'
                ORDER BY pedidos.fecha DESC;"""


print('\n\n' + '-'*10 + ' INICIO CONSULTA 3 ' + '-'*10 + '\n')
run_query(consulta_3, 'id, direccion, detalle y fecha de todos los pedidos entre el 5 de enero y el 7 de enero (incluyendo ambas fechas) que contengan un Tablet, ordenados por fecha descendentemente:')
print('\n' + '-'*10 + ' FIN CONSULTA 3 ' + '-'*10 + '\n')


cursor.close()
conn.close()
