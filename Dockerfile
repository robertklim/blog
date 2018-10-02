FROM python:3.7.0-slim-stretch
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/blog/src
ADD src/requirements.txt /usr/src/blog/src/
RUN pip install -r requirements.txt
ADD src/nltk_download.py /usr/src/blog/src/
RUN python nltk_download.py