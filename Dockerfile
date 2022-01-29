FROM python:3
ENV CONFIG_FILE=/config.yaml

COPY src/ /usr/local/share/makedeb-matrix/

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN rm /requirements.txt

ENTRYPOINT ["/usr/local/share/makedeb-matrix/main.py"]
