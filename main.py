from fastapi import FastAPI
from api.routes import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.get("/")
def get_root():
    return {"message":"hello world!"}

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://127.0.0.1:5500"] if you're running frontend from VSCode Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
