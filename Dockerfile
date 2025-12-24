# Start from python base image
FROM python:3.11-slim
RUN pip install --no-cache-dir torch==2.3.0 --index-url https://download.pytorch.org/whl/cpu

# Change working directory
WORKDIR /code

# Add requirements file to image
COPY ./requirements.txt /code/requirements.txt

# Install python libraries
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./Unittesting /code/Unittesting 

# Expose port 80 if running on that
EXPOSE 80

# Specify default command to run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
