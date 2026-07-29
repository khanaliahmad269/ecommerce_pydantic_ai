# Build the Application

FROM python:3.11-slim
WORKDIR /app 


#install backend dependencies

COPY requirements.txt .
RUN pip install --no-chache-dir -r requirements.txt 

#Copy Source cpde (Backend + Frontend natively)]
COPY . .

#Environment Variables
ENV PYTHONUNBUFFERED=1


#EXPOSE THE APPLICATION PORT

EXPOSE 8000

#START THE APPLICATION

CMD ["uvicorn","main:app","--host",'0.0.0.0',"--port","8000"]
