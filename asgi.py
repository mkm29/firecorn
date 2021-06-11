import os

# Get environment variables
log_level = os.getenv('LOGLEVEL', 'info')
debug = os.getenv("DEBUG", "False").upper() == 'TRUE'

if __name__ == "__main__":
    import uvicorn
    from src.app import create_app
    app = create_app(debug=debug)
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level=log_level)
