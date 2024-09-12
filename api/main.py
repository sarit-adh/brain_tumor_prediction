from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI()

# Add CORS middleware to allow requests from frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include API routes

app.include_router(router)

if __name__=="__main__":
    import uvicorn #Use ASGI (Asynchronous Server Gateway Interface)
    uvicorn.run(app, host="0.0.0.0", port=8080)