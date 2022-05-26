FROM python:3
ENV CONFIG_FILE=/config.yaml

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN rm /requirements.txt

COPY src/ /usr/local/share/makedeb-matrix/

ENTRYPOINT ["/usr/local/share/makedeb-matrix/main.py"]
