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