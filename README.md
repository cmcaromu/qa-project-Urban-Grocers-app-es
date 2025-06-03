# 🛒 Proyecto Urban Grocers

**Autor:** Carolina Muñoz Correa  
**Cohorte:** 29  
**Sprint:** 7

## 📄 Descripción

Este proyecto contiene pruebas automatizadas para la aplicación **Urban Grocers**, enfocadas en verificar el comportamiento del endpoint de creación de kits con diferentes valores para el campo `name`.

## ▶️ Cómo ejecutar las pruebas

1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
3. Instala las dependencias necesarias:
   ```bash
   pip install requests pytest
4. Asegúrate de que el intérprete de Python esté apuntando al entorno virtual (si usas un editor como VSCode).
5. Ejecuta las pruebas con el siguiente comando:
   ```bash
   pytest create_kit_name_kit_test.py
