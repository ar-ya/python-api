FROM python:3.7.11-alpine
WORKDIR  /python-api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

# CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["python","app.py","--host=0.0.0.0"]
