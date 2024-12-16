import config
from cpu_bound_functions import getPrime

from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def root(num: int, request: Request):
    calculated_prime = getPrime(num)
    return JSONResponse(content={"prime": calculated_prime}, status_code=200)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=config.UNIT_PORT,
    )