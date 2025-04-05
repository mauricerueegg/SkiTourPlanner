FROM python:3.13.2

WORKDIR /usr/src/app

# Backend
COPY backend/app.py backend/app.py

# Frontend (aus lokalem Build)
COPY frontend/frontend/build frontend/build

# Requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80
ENV FLASK_APP=/usr/src/app/backend/app.py
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]