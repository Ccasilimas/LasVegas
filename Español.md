# API de Búsqueda de Bienes Raíces (Las Vegas)

Este proyecto implementa una aplicación web basada en FastAPI que permite a los usuarios buscar propiedades inmobiliarias según diversos criterios, como rango de precios, número de habitaciones, baños y código postal.

## Características

- Parámetros de búsqueda flexibles para filtrar propiedades.
- Devuelve una lista de propiedades que cumplen con los criterios del usuario.
- Soporte para CORS, permitiendo acceso desde diferentes dominios.

## Tecnologías Utilizadas

- Python
- FastAPI
- Pandas
- Uvicorn
- Docker

## Comenzando

### Requisitos Previos

- Python 3.7 o superior.
- Docker (opcional, para contenedores).

### Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd <directorio-del-repositorio>
   ```

2. Instala los paquetes requeridos:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución de la Aplicación

Para ejecutar la aplicación FastAPI, utiliza el siguiente comando:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Ahora puedes acceder a la API en `http://localhost:8000`.

### Endpoints de la API

- `GET /search`: Busca propiedades utilizando los siguientes parámetros de consulta:
  - `min_price`: Precio mínimo de la propiedad.
  - `max_price`: Precio máximo de la propiedad.
  - `beds`: Número mínimo de habitaciones.
  - `baths`: Número mínimo de baños.
  - `zipcode`: Código postal del área.

#### Ejemplo de Solicitud
```http
GET /search?min_price=500000&max_price=1000000&beds=3&zipcode=89141
```

### Ejecución con Docker

Para construir y ejecutar la aplicación usando Docker, ejecuta:
```bash
docker build -t real-estate-search .
docker run -p 8000:8000 real-estate-search
```

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

