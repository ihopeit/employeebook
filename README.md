
## ��������
����֮ǰ��½ docker hub
docker login
docker build  -t ihopeit/employeebook-base:0.8 .


��������: 
docker run -it --rm -p 8000:8000 --entrypoint /bin/sh ihopeit/employeebook-base:0.8

## ʹ�þ�����ٴ��������
����/���⣺
�����׶Σ�����Ƶ���Ķ���ÿ�θĶ����´���Ч�ʵͣ�ϣ������Ķ�����ֱ�������е����������ֳ�����

��������� ���������� ָ������Դ��Ŀ¼
docker run -it --rm -p 8000:8000 -v "$(pwd)":/data/employeebook ihopeit/employeebook-base:0.8

ָ������Դ�� && ���������� 
docker run --rm -p 8000:8000 -v "$(pwd)":/data/employeebook --env server_params="--settings=employeebook.localSettings" ihopeit/employeebook-base:0.8

