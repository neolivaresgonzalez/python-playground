# Usar imagen 3.7 de python
FROM python:3.7

# Crear directorio de trabajo
WORKDIR /app

# Instalar modulos (dependencias) 
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar scripts a WORKDIR
COPY . .

# Ejecutar scripts
CMD [ "python", "./christmas-tree.py" ]