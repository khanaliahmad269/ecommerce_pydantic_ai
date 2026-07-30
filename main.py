from fastapi import FastAPI
from backend.routes import cart,products,orders,chatbot
import os
import uvicorn
import logfire


#initialize FastAPI app
app=FastAPI()

#configure Logfire for observability

logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_fastapi(app)
logfire.instrument_pydantic()


#create uploads folder for product images

UPLOAD_FOLDER="uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


#include API route modules

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(cart.router)
app.include_router(chatbot.router)

#Serve uploaded files statically
from fastapi.staticfiles import StaticFiles
app.mount("/uploads",StaticFiles(directory="uploads"), name="uploads")


# Serve Frontend natively
app.mount("/", StaticFiles(directory="frontend",html=True), name="frontend")

if __name__ =="__main__":
    print("Starting backend server (FastAPI)....")
    uvicorn.run(app,host="0.0.0.0", port=8000)