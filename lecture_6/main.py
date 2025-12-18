from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
async def healthcheck() -> dict:
    """
    Healthcheck endpoint to verify that the application is running.

    Returns:
        dict: Application status.
    """
    return {"status": "ok"}