from fastapi import FastAPI
from app.router import webook

app = FastAPI()



@app.get('/')
async def main():
    return {'message': 'Python is beautiful', 'status': 'OK'}


app.include_router(webook.router, prefix='/api/v1')