import pandas as pd #necesaria para todo lo que son las operaciones y el manejo de los datos 
import numpy as np # necesaria para la parte matricial de las tablas de datos 
import matplotlib.pyplot as plt #necesaria para las operaciones matemáticas 

#Se puede crear una serie por medio del siguiente comando: 
#llamaremos malla a nuestro primer data frame, y en el se pondran todos los tamaños de tamiz de la serie en su notación estándar 
malla = pd.Series([
      "1 1/2", #tamiz de 1 1/2"
      "1" , #tamiz de 1"
      "3/4",#tamiz de 3/4"
      "3/8", #tamiz de 3/8"
      "#4" ,#tamiz # 4
      "#10",# tamiz # 10
      "#20",# tamiz # 20
      "#40",# tamiz # 40
      "#60",# tamiz # 60
      "#100",# tamiz # 100
      "#140",#tamiz # 140
      "#200",# tamiz # 200

      
])
#Se crea otro data frame con el tamaño de los tamices anteriormente citados expresados en (mm)
abertura = pd.Series([
      "37.5", #tamiz de 1 1/2"
      "25", #tamiz de 1"
      "19", #tamiz de 3/4"
      "9.5",#tamiz de 3/8"
      "4.75" ,#tamiz # 4
      "2.00" ,#tamiz # 10
      "0.85" ,#tamiz # 20
      "0.425" ,#tamiz # 40
      "0.25" ,#tamiz # 60
      "0.150" ,#tamiz # 100
      "0.075" ,#tamiz # 200
])
abertura