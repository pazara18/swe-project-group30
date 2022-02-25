# Instructions
# First build the app using: docker build -t docker_image_name work_dir_path
# Then run by: docker run -p port_num:port_num docker_image_name
#
#
# After successfully executing the commands above the docker container should 
# show up in the Docker Desktop application and using the IP given there the 
# web app can be accessed.

FROM python:3.9.7

WORKDIR /group30

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY ./src ./app

COPY ./utils ./app

CMD ["python", "./app/app.py"]