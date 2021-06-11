import os

# Get environment variables
log_level = os.getenv('LOGLEVEL', 'info')
debug = os.getenv("DEBUG")

if __name__ == "__main__":
    import uvicorn
    from src.app import create_app
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level=log_level, debug=debug)
