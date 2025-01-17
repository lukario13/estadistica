# -*- coding: utf-8 -*-
"""MODA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ehly5s1H8JnNTF_zBUZs0D-AKKRdwi9M
"""

from pyspark.sql import SparkSession

from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Estadística_moda").getOrCreate()

A_notas = spark.read.csv("nota_alumno.csv")

A_notas.show()

A_notas = spark.read.csv("nota_alumno.csv", header=True, inferSchema=True)

A_notas = A_notas.withColumnRenamed("_c0", "Nombre").withColumnRenamed("_c1", "Nota")

A_notas.show()

moda_nota = (
    A_notas.groupBy("Nota")
    .count()
    .orderBy(col("count").desc())
    .first()
)

nota_moda = moda_nota["Nota"]

frecuencia_moda = moda_nota["count"]

print("Moda de las notas:", nota_moda)

print("Frecuencia de la moda:", frecuencia_moda)