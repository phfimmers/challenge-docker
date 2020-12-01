# based on official docker image with debian buster and python v3.7
FROM python:3.7
# install nano text editor and numpy
RUN pip install numpy \
	&& apt-get update \
	&& apt-get install nano \
	&& rm -rf /var/lib/apt/lists/*
# folder stucture creation
RUN mkdir /app
RUN mkdir /app/pipeline
RUN mkdir /app/docker
# Copy the App
COPY docker /app/docker
COPY pipeline /app/pipeline
# set working directory
WORKDIR /app
# run command
CMD ["python", "pipeline/pipeline.py"]