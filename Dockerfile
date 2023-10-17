FROM python:3.11.4

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requiremts.txt

EXPOSE 8501

COPY ./Home_Page.py
COPY ./pages
COPY ./assets

ENTRYPOINT ["streamlit", "run"]

CMD ["Home_Page.py"]