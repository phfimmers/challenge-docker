# based on official docker image with debian buster and python v3.7
FROM python:3.7
# folder stucture creation
RUN mkdir /app
RUN mkdir /pipeline
# Copy the App
COPY pipeline /app/pipeline
# set working directory
WORKDIR /app
# run command
CMD ["python", "pipeline/model/model.py"]