FROM  python
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY .. /app
EXPOSE 5001
ENV FLASK_RUN_HOST 0.0.0.0

CMD [ "python3","-m","flask","--app","src/app","run" ]