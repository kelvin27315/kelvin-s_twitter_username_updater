FROM python:3.9.13-slim

RUN apt update; \
    apt install -y git
RUN pip install "pysen[lint]==0.10.2"

ENTRYPOINT ["pysen", "run"]