# start by pulling the python image
FROM python:3.8-alpine

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# install the dependencies and packages in the requirements file
RUN apk --no-cache add musl-dev linux-headers g++

# https://codehunter.cc/a/docker/install-numpy-requirement-in-a-dockerfile-results-in-error
# RUN apk add --no-cache py3-numpy
RUN pip3 install numpy
RUN pip3 install -r requirements.txt
RUN apk update
RUN apk --no-cache add curl

# copy every content from the local file to the image
COPY . /app

EXPOSE 8083

# configure the container to run in an executed manner
#ENTRYPOINT [ "python" ]

CMD ["python", "-u", "main.py"]
