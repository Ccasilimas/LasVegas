from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes (dominios)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv("datos.csv")

# Asegurarse de que la columna 'Zipcode' sea de tipo cadena
df['Zipcode'] = df['Zipcode'].astype(str)

@app.get("/search")
async def search(
    min_price: int = Query(None),
    max_price: int = Query(None),
    beds: int = Query(None),
    baths: int = Query(None),
    zipcode: str = Query(None)
):
    # Filtrar los resultados basados en los parámetros
    result = df
    if min_price is not None:
        result = result[result['Price'] >= min_price]
    if max_price is not None:
        result = result[result['Price'] <= max_price]
    if beds is not None:
        result = result[result['Beds'] >= beds]
    if baths is not None:
        result = result[result['Bathrooms'] >= baths]
    if zipcode:
        result = result[result['Zipcode'].str.contains(zipcode, case=False)]
    
    # Reemplazar NaN e infinitos por None
    result = result.replace({np.nan: None, np.inf: None, -np.inf: None})
    
    return result[[
        'zpid', 'Status Type', 'Status Text', 'Time On Zillow', 'Price', 
        'Area', 'Price Per Sqft', 'Zestimate', 'Zestimate Price Per Sqft', 
        'Rent Zestimate', 'Lot Area', 'Lot Area Unit', 'Beds', 'Bathrooms', 
        'Address', 'Street', 'City', 'State', 'Zipcode', 'Latitude', 
        'Longitude', 'Broker Name', 'is zillow owned', 'Sold Date', 
        'Sold Price', 'Image URL'
    ]].to_dict(orient="records")
