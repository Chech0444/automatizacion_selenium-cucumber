# Automatización Selenium + Cucumber

Proyecto de pruebas automatizadas usando **Selenium WebDriver** + **Cucumber (Behave)** sobre una aplicación Flask de login.

## Estructura

```
.
├── app/                        # Aplicacion web bajo prueba
│   ├── app.py                  # API Flask con login
│   └── templates/
│       └── login.html          # Formulario de login
├── features/                   # Pruebas Cucumber
│   ├── login.feature           # Escenarios en Gherkin
│   ├── environment.py          # Configuracion del browser (Firefox o Chrome)
│   └── steps/
│       └── login_steps.py      # Step definitions con Selenium
└── README.md
```

## Requisitos

- Python 3.10+
- pip
- **Firefox** o **Chrome** (segun el browser a usar)

## Instalacion

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask selenium behave
```

### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate
pip install flask selenium behave
```

## Ejecutar la app

```bash
python app/app.py
```

La app corre en `http://127.0.0.1:5000`.

Usuarios de prueba:
- `admin` / `1234`
- `user` / `pass`

Si el puerto 5000 esta ocupado, cambialo en `app/app.py`:
```python
app.run(debug=True, host="0.0.0.0", port=5001)
```

## Ejecutar las pruebas

Con la app corriendo, en otra terminal:

### Con Firefox (por defecto)

```bash
source venv/bin/activate      # Linux/macOS
# o en Windows: venv\Scripts\activate
behave features/
```

### Con Chrome

```bash
# Linux/macOS
BROWSER=chrome source venv/bin/activate && behave features/

# Windows (PowerShell)
$env:BROWSER="chrome"; behave features/

# Windows (CMD)
set BROWSER=chrome && behave features/
```

Selenium Manager descarga automaticamente el driver (chromedriver o geckodriver) segun el browser que uses.

## Clonar y ejecutar desde cero (Linux/macOS)

```bash
git clone https://github.com/Chech0444/automatizacion_selenium-cucumber.git
cd automatizacion_selenium-cucumber
python3 -m venv venv
source venv/bin/activate
pip install flask selenium behave
python app/app.py &
behave features/
```

## Clonar y ejecutar desde cero (Windows)

```powershell
git clone https://github.com/Chech0444/automatizacion_selenium-cucumber.git
cd automatizacion_selenium-cucumber
python -m venv venv
venv\Scripts\activate
pip install flask selenium behave

# Terminal 1: iniciar la app
Start-Process powershell -ArgumentList "python app/app.py"

# Terminal 2: ejecutar pruebas
$env:BROWSER="firefox"
behave features/
```

Para usar Chrome en Windows:
```powershell
$env:BROWSER="chrome"
behave features/
```

## Escenarios

1. **Login exitoso** – ingresa credenciales validas y redirige al dashboard
2. **Login fallido** – ingresa credenciales invalidas y muestra error

## Stack

| Herramienta | Proposito |
|---|---|
| Python | Lenguaje |
| Flask | App bajo prueba |
| Selenium WebDriver | Automatizacion del browser |
| Behave (Cucumber) | Framework BDD |
| Firefox / Chrome | Browsers soportados |
