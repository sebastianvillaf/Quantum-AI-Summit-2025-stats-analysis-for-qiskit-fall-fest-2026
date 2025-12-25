
import pandas as pd
import numpy as np
import matplotlib as mpl

predata=pd.read_csv(r"C:/Users/aaron/Downloads/hola.csv")

z=predata.isna()
data=predata.fillna(value="")

day1=(data["Asistencia día 1"]=="VERDADERO").sum()
day2=(data["Asistencia día 2"]=="VERDADERO").sum()
day3=(data["Asistencia día 3"]=="VERDADERO").sum()

print(f"asistieron {day1} personas el Viernes 19")
print(f"asistieron {day2} personas el Sabado 20")
print(f"asistieron {day3} personas el Domingo 21")















