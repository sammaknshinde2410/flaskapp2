FROM python
RUN pip install flask
RUN mkdir /app/
COPY welcome.py /app/
EXPOSE 7000
CMD [ "python", "/app/welcome.py" ]
