# Importar librerías necesarias. NO SE DEBE IMPORTAR NINGUNA OTRA LIBRERÍA.

import mysql.connector as db
import csv

mydb = db.connect(
        host="localhost",
        user="root",
        passwd="mysql123",
        database="mp2")

cursor = mydb.cursor()

# Desde este punto en adelante se debe crear el código solicitado.

cursor.execute("DROP TABLE IF EXISTS productos_pedidos;")
cursor.execute("DROP TABLE IF EXISTS pedidos;")
cursor.execute("DROP TABLE IF EXISTS clientes;")
cursor.execute("DROP TABLE IF EXISTS productos;")

### CREACION DE TABLAS ###

# Tabla de Productos
crear_tabla_productos = """
CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    precio INT
); 
"""
cursor.execute(crear_tabla_productos)

# Tabla de Clientes
crear_tabla_clientes = """
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    email VARCHAR(255)
);
"""
cursor.execute(crear_tabla_clientes)

# Tabla de Pedidos
crear_tabla_pedidos = """
CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    fecha DATE,
    direccion VARCHAR(255),
    id_cliente INT,
    detalle VARCHAR(255),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
"""
cursor.execute(crear_tabla_pedidos)

#Tabla de Productos Pedidos
crear_tabla_productos_pedidos = """
CREATE TABLE productos_pedidos (
    id_producto INT,
    id_pedido INT,
    cantidad INT,
    PRIMARY KEY (id_producto, id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos (id),
    FOREIGN KEY (id_pedido) REFERENCES pedidos (id) 
);
"""
cursor.execute(crear_tabla_productos_pedidos)

### IMPORTACION DE ARCHIVOS .CSV A LAS TABLAS ###

# Insertar datos a Productos

with open ('./data/productos.csv', newline = '') as file:
    CSV_reader = csv.reader(file, delimiter=',')
    next(CSV_reader)
    filas =  []

    for row in CSV_reader:
        filas.append(row)

insert_productos = "INSERT INTO productos (id, nombre, descripcion, precio) VALUES (%s, %s, %s, %s)"
cursor.executemany(insert_productos, filas)

# Insertar datos a Clientes

with open('./data/clientes.csv', newline='') as file:
    CSV_reader = csv.reader(file, delimiter=',')
    next(CSV_reader)
    filas = []

    for row in CSV_reader:
        filas.append(row)

insert_clientes = "INSERT INTO clientes (id, nombre, email) VALUES (%s, %s, %s)"
cursor.executemany(insert_clientes, filas)

# Insertar datos a Pedidos

with open ('./data/pedidos.csv', newline = '') as file:
    CSV_reader = csv.reader(file, delimiter=',')
    next(CSV_reader)
    filas =  []

    for row in CSV_reader:
        filas.append(row)

insert_pedidos = "INSERT INTO pedidos (id, fecha, direccion, id_cliente, detalle) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(insert_pedidos, filas)

# Insertar datos a Productos pedidos

with open ('./data/productos_pedidos.csv', newline = '') as file:
    CSV_reader = csv.reader(file, delimiter=',')
    next(CSV_reader)
    filas =  []

    for row in CSV_reader:
        filas.append(row)

insert_productos_pedidos = "INSERT INTO productos_pedidos (id_producto, id_pedido, cantidad) VALUES (%s, %s, %s)"
cursor.executemany(insert_productos_pedidos, filas)

mydb.commit()
print("Todos los datos fueron cargados correctamente.")