FROM python:3.9.13-slim-buster

WORKDIR /opt/src

RUN pip3 install torch torchvision --extra-index-url https://download.pytorch.org/whl/cpu

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "inference.py" ]
