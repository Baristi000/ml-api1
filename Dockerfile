FROM python:3.7.3
ADD ./api ./api
ADD ./core ./core
ADD ./functions ./functions
ADD ./main.py ./main.py
ADD ./packages.txt ./packages.txt
RUN pip install -r packages.txt && gdown https://drive.google.com/uc?id=11mujzVaFqa7R1_lB7q0kVPW22Ol51MPg && pip install tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl
CMD [ "python","main.py"]