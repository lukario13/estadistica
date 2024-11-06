# -*- coding: utf-8 -*-
"""correlacion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10RBD7ZJRgtS0Q7oXnlVLhao8iL8x3NGf
"""

from pyspark.sql import SparkSession

from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Estadística_correlacion").getOrCreate()

A_notas = spark.read.csv("nota_alumno.csv")

A_notas.show()

A_notas = spark.read.csv("nota_alumno.csv", header=True, inferSchema=True)

A_notas = A_notas.withColumnRenamed("_c0", "Nombre").withColumnRenamed("_c1", "Nota")

A_notas.show()

A_notas = A_notas.withColumn("Nota2", col("Nota") + 2)

A_notas.show()

correlacion = A_notas.stat.corr("Nota", "Nota2")

print(f"Correlación entre 'Nota' y 'Nota2': {correlacion}")