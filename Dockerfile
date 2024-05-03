FROM python:3

ENV UNBUFFER=1

WORKDIR /code

COPY reuirement.txt



RUN pip install -requirement.txt

EXPOSE 8000

CMD [ "python","manage.py","runserver" ]
