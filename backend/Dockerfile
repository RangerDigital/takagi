FROM python:3.8.2

# Copy requirements.
ADD requirements.txt /requirements.txt

# Install requirements.
RUN pip3 install -r requirements.txt

# Copy files.
ADD / /

EXPOSE 8000

# Run app server.
CMD gunicorn -b 0.0.0.0:8000 main:app
