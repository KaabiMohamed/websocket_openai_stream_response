from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controllers.controllers_config import all_routers
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    Instrumentator().instrument(app).expose(app)
    uvicorn.run(app, host="0.0.0.0", port=8000)
