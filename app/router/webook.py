from fastapi import APIRouter


router = APIRouter()

@router.post('receive-data')
async def receive_data(data:dict):
    print('-'*90)
    print(data)
    print('-'*90)

    return {'message': 'Success received data', 'status':'OK'}