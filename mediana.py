# -*- coding: utf-8 -*-
"""MEDIANA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dKbZgUSoC1i45NadYP2UhfZqV_24lOml
"""

from pyspark.sql import SparkSession

from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Estadística_mediana").getOrCreate()

A_notas = spark.read.csv("nota_alumno.csv")

A_notas.show()

A_notas = spark.read.csv("nota_alumno.csv", header=True, inferSchema=True)

A_notas = A_notas.withColumnRenamed("_c0", "Nombre").withColumnRenamed("_c1", "Nota")

A_notas.show()

median_nota = A_notas.approxQuantile("Nota", [0.5], 0.0)[0]

print("Median of Nota:", median_nota)