# Use an official Python runtime as a parent image
FROM python:3.10.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./untitled0.py /app
COPY ./random_paragraphs.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org nltk

# Make port 80 available to the world outside this container
EXPOSE 80

# Run untitled0.py when the container launches
CMD ["python", "/app/untitled0.py"]
