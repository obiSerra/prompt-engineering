FROM python:3.10

COPY ./working-dir /home/working-dir

WORKDIR /home/working-dir

# -- Install dependencies

# RUN pip install ...
RUN echo "Installing requirements..."
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#RUN mkdir /home/working-dir

RUN pip install -e /home/working-dir

# -- Run any setup scripts