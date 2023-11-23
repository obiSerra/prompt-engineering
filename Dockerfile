FROM python:3.10

COPY ./working-dir /home/working-dir

WORKDIR /home/working-dir

# -- Install dependencies

# RUN pip install ...
RUN pip install pydantic Jinja2 jupyterlab
RUN pip install openai
RUN pip install beautifulsoup4

#RUN mkdir /home/working-dir

RUN pip install -e /home/working-dir


# -- Run any setup scripts