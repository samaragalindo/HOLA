import pandas as pd

datos={
    "nombres":["Maria","Jose","Juan"],
    "edad": [20,21,22],
    "promedio": [100,79,64]
}

df_datos=pd.DataFrame(datos)
print(df_datos)

print("\n\n")
df=pd.read_csv("https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv",
            sep=";",decimal=",")
print(df)
print(df.info())
print(df.describe())
print("\n\n)HEAD")
print(df.head())
print("\n\n)TAIL")
print(df.tail())
print("\n\n)SAMPLE")
print(df.sample(8))

print("\n\n)ATRIBUTOS")
print(df.shape)#numero total de datos
print(df.size)#numero total de dtaos 8renglones por columnas)
print(df.columns)#nombre de todas las columnas
print(df.index)#indices, es decir nombre de los renglones
print(df.dtypes)#todas las columnas con su tipo de datos correspondientes. tipos de datos de cada columna

print("\n\n)SELECT COLUMNAS")
print(df.n)


#24/08/23

def repetidos(nums):
    return len (nums) != len(set(nums))





