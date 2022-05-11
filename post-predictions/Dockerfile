FROM python:3.8

WORKDIR /root

ENV TRANSITION_ID not_provided
ENV EXECUTION_ID not_provided

COPY requirements.txt .
COPY main.py .

RUN pip install -r requirements.txt


# input to this function will be provided through the command line arguments
ENTRYPOINT ["python", "main.py"]
