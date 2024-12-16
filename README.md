# Real Estate Search API

This project implements a FastAPI-based web application that allows users to search for real estate listings based on various criteria such as price range, number of beds, baths, and zip code.

## Features

- Flexible search parameters to filter properties
- Returns a list of properties meeting the user's criteria
- CORS support for access from different domains

## Technologies Used

- Python
- FastAPI
- Pandas
- Uvicorn
- Docker

## Getting Started

### Prerequisites

- Python 3.7+
- Docker (optional, for containerization)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the FastAPI application, use the command:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

You can now access the API at `http://localhost:8000`.

### API Endpoints

- `GET /search`: Search for properties using the following query parameters:
  - `min_price`: Minimum price of the property
  - `max_price`: Maximum price of the property
  - `beds`: Minimum number of beds
  - `baths`: Minimum number of baths
  - `zipcode`: Zip code of the area

#### Example Request
```http
GET /search?min_price=500000&max_price=1000000&beds=3&zipcode=89141
```

#### Example Response
```json
[
    {
        "zpid": "331665222",
        "Status Type": "FOR_SALE",
        "Status Text": "House for sale",
        "Time On Zillow": null,
        "Price": 479900,
        "Area": 1796,
        "Price Per Sqft": 267,
        "Zestimate": 475000,
        "Zestimate Price Per Sqft": 264,
        "Rent Zestimate": 2134,
        "Lot Area": 3484.8,
        "Lot Area Unit": "sqft",
        "Beds": 3,
        "Bathrooms": 3,
        "Address": "6276 Desert Orchid Way",
        "Street": "6276 Desert Orchid Way",
        "City": "Las Vegas",
        "State": "NV",
        "Zipcode": "89141",
        "Latitude": 35.998367,
        "Longitude": -115.22939,
        "Broker Name": "Real Broker LLC",
        "is zillow owned": "FALSE",
        "Sold Date": null,
        "Sold Price": null,
        "Image URL": "https://photos.zillowstatic.com/fp/faa93bdf5a545e30d437987caf9ec4c2-p_e.jpg"
    }
]
```

### Running with Docker

To build and run the application using Docker, execute:
```bash
docker build -t real-estate-search .
docker run -p 8000:8000 real-estate-search
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

- FastAPI documentation
- Docker documentation