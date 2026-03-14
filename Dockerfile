# Starting with a lightweight Python 3.11 image
FROM python:3.11-slim

# Seting /app as the main working directory inside the container
WORKDIR /app

# Copying the requirements file first
COPY requirements.txt .

# Installing all the Python libraries needed for the project
RUN pip install -r requirements.txt

# Copying the rest of the application files into the container
COPY . .

# Exposing port 5000 so the Flask app can be accessed from outside
EXPOSE 5000

# For Starting the Flask application and allow connections from any host
CMD ["python", "app.py", "--host=0.0.0.0"]
