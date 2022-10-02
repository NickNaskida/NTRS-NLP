# pull official base image
FROM python:3.9.13-alpine

MAINTAINER Nikoloz Naskidashvili <nikoloz2005@gmail.com>

# environment variables
ENV FLASK_ENV=development \
    FLASK_APP=manage

# set work directory
WORKDIR .

# update
RUN apk update

COPY ./requirements.txt ./requirements.txt
COPY ./requirements ./requirements

RUN apk add build-base   # install the GCC, libc-dev and binutils packages (greenlet error)
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# NLTK word lists download
RUN [ "python3", "-c", "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')" ]

# copy project
COPY . .

RUN ./scripts/linux/init.sh

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
