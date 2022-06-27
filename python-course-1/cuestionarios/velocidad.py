def velocidad(distancia, tiempo):
  resultado = ""
  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable resultado
  res_en_km_h = distancia / (tiempo / 3600)
  res_en_m_s = (distancia*1000) / tiempo
  resultado = "La velocidad es "+ str(res_en_km_h) + " km/h o "+ str(res_en_m_s) + " m/s" 
  # recuerda que los datos están en las variables distancia y tiempo
  return resultado


print(velocidad(0.01,1))