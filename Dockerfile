FROM bitnami/python
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tornado
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple redis
COPY websocketo.py /project/
WORKDIR /project
ENTRYPOINT ["python","websocketo.py"]