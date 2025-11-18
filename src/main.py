from fastapi import FastAPI

from domains.user.router import router as user_router

app = FastAPI()

app.include_router(
    router=user_router,
)

@app.get("/")
def health():
    return {"status": "ok"}
