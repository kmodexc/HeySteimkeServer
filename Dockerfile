FROM python

WORKDIR /work

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY interface.proto . 
COPY HeySteimkeServer.py .
RUN python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. .\interface.proto

ENTRYPOINT ["python" , "/work/HeySteimkeServer.py"]