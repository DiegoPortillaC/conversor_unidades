# Conversor de Unidades 📏

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Una biblioteca Python para realizar conversiones entre diferentes sistemas de unidades de medida. Ideal para aplicaciones que requieren transformaciones precisas entre sistemas métricos e imperiales.

## 📋 Características

- 📏 Conversión de unidades de longitud (inches/cm, km/m, yardas/m)
- 📏 Conversión de unidades de masa (g/kg, lb/kg, oz/g)
- 🌡️ Conversión de temperatura (Celsius/Kelvin/Fahrenheit)
- 🧪 Tests unitarios para todas las conversiones
- 📚 Documentación detallada
- 🚀 Fácil de usar y extensible

## 📚 Módulos Disponibles

### 1. Longitud 📏

| Conversión | Descripción |
|------------|-------------|
| `inch_cm` | Pulgadas a Centímetros |
| `cm_inch` | Centímetros a Pulgadas |
| `km_meters` | Kilómetros a Metros |
| `meters_km` | Metros a Kilómetros |
| `yard_meter` | Yardas a Metros |
| `meter_yard` | Metros a Yardas |

### 2. Masa 📐

| Conversión | Descripción |
|------------|-------------|
| `gram_kilo` | Gramos a Kilogramos |
| `kilo_gram` | Kilogramos a Gramos |
| `lb_kilo` | Libras a Kilogramos |
| `kilo_lb` | Kilogramos a Libras |
| `ounce_gram` | Onzas a Gramos |
| `gram_ounce` | Gramos a Onzas |

### 3. Temperatura 🌡️

| Conversión | Descripción |
|------------|-------------|
| `celsius_kelvin` | Celsius a Kelvin |
| `kelvin_celsius` | Kelvin a Celsius |
| `celsius_fahren` | Celsius a Fahrenheit |
| `fahren_celsius` | Fahrenheit a Celsius |

## 🛠️ Estructura del Proyecto

```
conversor_unidades/
├── src/
│     └──conversores/       # Código fuente
│        ├── longitud.py    # Conversiones de longitud
│        ├── masa.py        # Conversiones de masa
│        └── temperatura.py # Conversiones de temperatura
├── tests/             # Tests unitarios
│   └── test_conversor.py
└── requirements.txt   # Dependencias del proyecto
```

## 🚀 Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/DiegoPortillaC/conversor_unidades.git
   cd conversor_unidades
   ```

2. Crear y activar un entorno virtual:
   ```bash
   # Crear el entorno virtual
   python -m venv venv
   
   # Activar el entorno
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Instalar el paquete en modo editable:
   ```bash
   pip install -e.
   ```

## 🧪 Ejecución de Tests

Para ejecutar los tests de la aplicación:

```bash
python -m unittest tests/test_conversor.py
# Alternativa
cd tests
python .\test_conversor.py
```

## 📝 Ejemplos de Uso

```python
from src.longitud import Longitud
from src.masa import Masa
from src.temperatura import Temperatura

# Ejemplo de longitud
print(Longitud.inch_cm(1))  # 2.54 cm
print(Longitud.cm_inch(5))  # 1.968505 pulgadas

# Ejemplo de masa
print(Masa.kilo_gram(1))  # 1000 gramos
print(Masa.lb_kilo(1))    # 0.453592 kilogramos

# Ejemplo de temperatura
print(Temperatura.celsius_kelvin(0))    # 273.15 K
print(Temperatura.celsius_fahren(100))  # 212 °F
```
