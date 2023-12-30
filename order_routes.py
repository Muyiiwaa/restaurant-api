from fastapi import APIRouter

# to be able to route to this specific location
order_router = APIRouter(
    prefix= '/order',
    tags= ['orders']
    
)

# first test get request
@order_router.get("/")
async def hello():
    return {"message": "hello world"}