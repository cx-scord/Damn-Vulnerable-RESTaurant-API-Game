from apis.router import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from init import load_initial_data


def start_application():
    app = FastAPI(
        title="Damn Vulnerable RESTaurant",
        description="An intentionally vulnerable API service designed for learning and training purposes for ethical hackers, security engineers, and developers.",
        version="1.0.0",
        servers=[{"url": "http://localhost:8091", "description": "Local API server"}],
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=".*.(restaurant.com|deliveryservice.com)",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)
    load_initial_data()
    return app


app = start_application()
