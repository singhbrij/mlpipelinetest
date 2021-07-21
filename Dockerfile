#FROM continuumio/anaconda3:4.4.0
FROM python:3.6.8
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python swagger.py
