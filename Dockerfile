FROM python:3
COPY requirements.txt /usr/src/brain_storm/requirements.txt
RUN pip install -r /usr/src/brain_storm/requirements.txt