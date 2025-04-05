# Schritt 1: Frontend builden
FROM node:18 AS frontend-builder

WORKDIR /app/frontend
COPY frontend/frontend/package*.json ./
RUN npm install
COPY frontend/frontend .
RUN npm run build

# Schritt 2: Backend + Build zusammenführen
FROM python:3.13.2

WORKDIR /usr/src/app

# Backend
COPY backend/app.py backend/app.py

# Kopiere das gebaute Frontend aus dem vorherigen Image
COPY --from=frontend-builder /app/frontend/build frontend/build

# Requirements & Flask Start
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

ENV FLASK_APP=/usr/src/app/backend/app.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]