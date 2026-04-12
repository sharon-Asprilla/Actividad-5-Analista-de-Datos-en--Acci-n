import pandas as pd
import numpy as np

# Creación de nuestro ÚNICO dataframe principal de trabajo
datos_ventas = {
    'id_venta': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'sucursal': ['Norte', 'Sur', 'Centro', 'Norte', 'Centro', 'Sur', 'Norte', 'Sur', 'Centro', 'Norte', 'Sur', 'Centro', 'Norte', 'Norte', 'Sur'],
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Laptop', 'Monitor', 'Teclado', 'Mouse', 'Monitor', 'Laptop', 'Mouse', 'Teclado', 'Monitor', 'Laptop', 'Monitor', 'Teclado'],
    'cantidad': [2, np.nan, 5, 1, 2, 4, np.nan, 3, 2, 5, 3, np.nan, 4, 1, 2],
    'precio_base': ['1200.50', '25.00', '45.00', '1200.50', '250.00', '45.00', '25.00', '250.00', '1200.50', '25.00', '45.00', '250.00', '1200.50', '250.00', '45.00'],
    'categoria': ['Computación', 'Accesorios', 'Accesorios', 'Computación', 'Periféricos', 'Accesorios', 'Accesorios', 'Periféricos', 'Computación', 'Accesorios', 'Accesorios', 'Periféricos', 'Computación', 'Periféricos', 'Accesorios'],
    'columna_basura': ['x', 'y', 'z', 'w', 'a', 'b', 'c', 'x', 'y', 'z', 'a', 'b', 'c', 'w', 'x']
}

df_ventas = pd.DataFrame(datos_ventas)

print(df_ventas)


df = df_ventas.drop(columns=['columna_basura'], errors='ignore') 

df = df.rename(columns={'precio_base': 'precio_unitario'})

ranking = df.sort_values(by='id_venta', ascending=False)
print(df)


print()
filtro_sucursal= df['sucursal'].value_counts()
print(filtro_sucursal)
print()
print("total de productos del inventario")
total_categoria = df['producto'].nunique()
print(total_categoria)
print()
print("frecuencia del producto")
filtro_producto= df['producto'].value_counts()
print(filtro_producto)

print()
print("manejo de nulos")
df['cantidad'] = df['cantidad'].fillna(1)
print(df['cantidad'])
print()


print("astype ")
df['precio_unitario'] = df['precio_unitario'].astype(float)
df['sucursal'] = df['sucursal'].astype("category")
print(df.dtypes)
print()

print("filtro precio_unitario > 150")
ventas_fuertes = df[df['precio_unitario'] > 150.0]
print(ventas_fuertes)
print()

print("filtro  sucursal 'Norte' y cantidad >= 2")
ventas_norte = df[(df['sucursal'] == 'Norte') & (df['cantidad'] >= 2)]
print(ventas_norte)
print()

df['total_venta'] = df['cantidad'] * df['precio_unitario']
print("DataFrame con columna total_venta")
print(df[['id_venta','producto','cantidad','precio_unitario','total_venta']])
print()

print("agrupacion por sucursal ")
metricas_sucursal = df.groupby('sucursal')['total_venta'].agg(['sum','mean'])
print(metricas_sucursal)
print()

print("Agrupación por sucursal (sum y mean)")
metricas_sucursal = df.groupby('sucursal')['total_venta'].agg(['sum','mean'])
print(metricas_sucursal)
print()


df_presupuestos = pd.DataFrame({
    'categoria': ['Computación', 'Accesorios', 'Periféricos'],
    'presupuesto_marketing': [5000, 1500, 2000]
})
print("DataFrame de presupuestos")
print(df_presupuestos)
print()


df_merge = pd.merge(df, df_presupuestos, on='categoria', how='left')
print("DataFrame fusionado con presupuestos")
print(df_merge)
print()




