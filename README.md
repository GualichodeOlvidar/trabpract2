# 📊 TP Lab2 – Finanzas: Dashboard Interactivo con PostgreSQL y Colab

Este proyecto forma parte del **Segundo Módulo de Programación Avanzada en Ciencia de Datos**.  
Tiene como objetivo aplicar el ciclo completo de trabajo con datos:
1. Obtención desde una fuente pública.
2. Almacenamiento en una base de datos relacional (PostgreSQL).
3. Construcción de un dashboard interactivo en una notebook de Google Colab.

---

## 📂 Estructura del Repositorio

```
TP_Lab2_Finanzas/
├── README.md
├── requirements.txt
├── repo_url.txt
├── src/
│   ├── load_data.py
│   ├── database_schema.sql
│   └── config.py
├── notebooks/
│   └── TP_Lab2_Finanzas.ipynb
└── docs/
    └── dashboard_preview.png
```

---

## 🌐 Dataset
**Fuente:** [Yahoo Finance](https://finance.yahoo.com/)  
**Descripción:** Datos históricos de precios de acciones, con columnas como *Date, Open, Close, Volume, High, Low*.  
El dataset se descarga automáticamente desde la API de `yfinance`.

---

## 🛠️ Base de Datos

**Motor:** PostgreSQL  
**Tabla:** `stock_data`  
**Script:** `src/load_data.py` y `src/database_schema.sql`

**Estructura:**
| Columna | Tipo | Descripción |
|----------|------|--------------|
| date | DATE | Fecha de cotización |
| open | FLOAT | Precio de apertura |
| close | FLOAT | Precio de cierre |
| high | FLOAT | Máximo del día |
| low | FLOAT | Mínimo del día |
| volume | BIGINT | Volumen operado |

---

## ⚙️ Configuración y Ejecución

### 1️⃣ Requisitos
Instalar dependencias:

```bash
pip install -r requirements.txt
```

### 2️⃣ Configurar conexión PostgreSQL
Editar `src/config.py` con tus credenciales:
```python
DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': 'tu_password',
    'database': 'finanzas_db'
}
```

### 3️⃣ Cargar los datos
Ejecutar:
```bash
python src/load_data.py
```

### 4️⃣ Dashboard interactivo
Abrir la notebook en Google Colab:  
👉 [`notebooks/TP_Lab2_Finanzas.ipynb`](notebooks/TP_Lab2_Finanzas.ipynb)

Ejecutar todas las celdas para visualizar el dashboard con Plotly.

---

## 📦 Librerías Principales
- pandas  
- numpy  
- plotly  
- yfinance  
- sqlalchemy  
- psycopg2-binary  

---

## 👥 Autor
**Nombre:** Pablo Lujan_  
**Curso:** Programación Avanzada en Ciencia de Datos  
**Institución:** GCBA

---

## 🪪 Licencia
Este proyecto se distribuye bajo licencia MIT.
