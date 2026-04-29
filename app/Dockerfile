FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /code

EXPOSE 8501

CMD ['streamlit', 'run', 'Introduction.py', "--server.address=0.0.0.0"]