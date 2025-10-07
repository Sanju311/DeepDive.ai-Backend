# Interview AI Backend

add description

## Features



## Quick Start

### Using Docker Compose (Recommended)

1. **Build and run the application:**
   ```bash
   docker-compose up --build
   ```

2. **Run in development mode with hot reload:**
   ```bash
   docker-compose --profile dev up --build
   ```

3. **Run in background:**
   ```bash
   docker-compose up -d
   ```

### Using Docker directly

1. **Build the image:**
   ```bash
   docker build -t interview-ai-backend .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 interview-ai-backend
   ```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/v1/status` - API status and version info
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## Development

### Local Development (without Docker)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

3. **Or using uvicorn directly:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Environment Variables

Create a `.env` file in the root directory for environment-specific configurations:

```env
# Example .env file
DEBUG=True
LOG_LEVEL=INFO
```

## Project Structure

```
Interview-AI-Backend/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── .dockerignore          # Docker ignore file
└── README.md              # This file
```

## API Documentation

Once the application is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Health Monitoring

The application includes health check endpoints for monitoring:

- **Health Check**: http://localhost:8000/health
- **API Status**: http://localhost:8000/api/v1/status

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is licensed under the MIT License.