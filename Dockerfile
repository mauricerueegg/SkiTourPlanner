# --- Frontend bauen ---
    FROM node:18 AS frontend-builder

    WORKDIR /app/frontend
    COPY frontend/package*.json ./
    RUN npm install
    COPY frontend .
    RUN npm run build
    
    # --- Backend + gebaute Files zusammenführen ---
    FROM python:3.13.2
    
    WORKDIR /usr/src/app
    COPY backend/app.py backend/app.py
    COPY requirements.txt requirements.txt
    RUN pip install -r requirements.txt
    
    # Frontend aus vorherigem Stage
    COPY --from=frontend-builder /app/frontend/build frontend/build
    
    EXPOSE 80
    ENV FLASK_APP=/usr/src/app/backend/app.py
    CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]