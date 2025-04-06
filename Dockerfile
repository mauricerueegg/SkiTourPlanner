# -------- Stage 1: Build frontend --------
    FROM node:18 AS frontend-builder

    WORKDIR /app/frontend
    COPY frontend/package*.json ./
    RUN npm install
    COPY frontend/ ./
    RUN npm run build
    
    # -------- Stage 2: Backend + Copy build --------
    FROM python:3.13.2
    
    WORKDIR /usr/src/app
    
    # Copy backend + requirements
    COPY backend/ ./backend
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    
    # ✅ Copy built frontend from Stage 1
    COPY --from=frontend-builder /app/frontend/build ./frontend/build
    
    # Expose port
    EXPOSE 80
    
    # ✅ Optional: set env variable for Flask
    ENV FLASK_APP=backend/app.py
    
    # Start Flask
    CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]