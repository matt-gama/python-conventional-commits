from fastapi import FastAPI


app = FastAPI()



@app.get('/')
async def main():
    return {'message': 'Python is beautiful', 'status': 'OK'}