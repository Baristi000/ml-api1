FROM python:3.8
ADD ./api ./api
ADD ./core ./core
ADD ./functions ./functions
ADD ./.gitignore ./.gitignore
ADD ./main.py ./main.py
ADD ./packages.txt ./packages.txt
RUN pip install -r packages.txt
CMD [ "python","main.py"]