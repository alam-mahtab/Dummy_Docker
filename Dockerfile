FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

RUN pip install -r requirements.txt

EXPOSE 15400


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15400"]