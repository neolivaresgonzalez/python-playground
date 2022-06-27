def xor(a, b):
  xor = False
  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable xor
  if((a == True and b == False) or (a == False and b == True)):
    xor = True
  # recuerda que los datos están en las variables a y b
  return xor

print(xor(True, True))
print(xor(True, False))
print(xor(False, True))
print(xor(False, False))