FROM python:3.9
RUN mkdir /urlShot
WORKDIR /urlShot
RUN pip install --upgrade pip
COPY requirements.txt /urlShot/
RUN pip install -r requirements.txt
COPY . /urlShot/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]