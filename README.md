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
│   ├── environment.py          # Configuracion del browser
│   └── steps/
│       └── login_steps.py      # Step definitions con Selenium
└── README.md
```

## Requisitos

- Python 3.10+
- Firefox
- pip

## Instalacion

```bash
python3 -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
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

## Ejecutar las pruebas

Con la app corriendo, en otra terminal:

```bash
source venv/bin/activate
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
| Firefox (headless) | Browser |
