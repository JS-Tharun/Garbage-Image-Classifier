FROM python:3.10.20

WORKDIR /app

COPY ./model_requirements.txt /app/model_requirements.txt
COPY ./app_requirements.txt /app/app_requirements.txt
COPY ./force_requirements.txt /app/force_requirements.txt




RUN pip install --no-cache-dir -r /app/model_requirements.txt
RUN pip install --no-cache-dir -r /app/app_requirements.txt
RUN pip install --no-cache-dir -r /app/force_requirements.txt

COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "Introduction.py", "--server.address=0.0.0.0"]