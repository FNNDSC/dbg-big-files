FROM docker.io/python:3.10.2-alpine

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="dbg-bigfiles" \
      org.opencontainers.image.description="A ChRIS fs plugin that creates files of random data."

WORKDIR /usr/local/src/dbg-bigfiles

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

CMD ["bigfiles", "--help"]
