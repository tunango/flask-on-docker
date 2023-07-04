FROM python:3.9.10


WORKDIR /app

COPY ./app .
COPY requirements.txt .
# ./app . ./app /app は同意。内容をコピー

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "index.py"]

