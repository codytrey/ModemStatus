FROM centos:7
LABEL maintainers="cody.t.belcher@gmail.com"

RUN yum -y update \
    && yum -y install centos-release-scl \
    && yum -y install git \
    && yum -y install rh-python36

ARG PERIOD
ENV PERIOD ${PERIOD:-300}

ARG TZ
ENV TZ ${TZ:-America/Chicago}

RUN mkdir /tmp/modemstatus

RUN chmod 777 /tmp/modemstatus

COPY run_script.sh /tmp

RUN chmod +x /tmp/run_script.sh

#COPY create_virt_env.sh /tmp

ADD https://github.com/codytrey/ModemStatus/archive/0.0.02.tar.gz /ModemStatus-0.0.02.tar.gz

ADD https://raw.githubusercontent.com/codytrey/ModemStatus/master/Examples/Graph_Stats/graph_stats.py /tmp/graph_stats.py

ADD https://raw.githubusercontent.com/codytrey/ModemStatus/master/Examples/Update_All/update_all.py /tmp/update_all.py

ADD requirements.txt /tmp

RUN tar xvf ModemStatus-0.0.02.tar.gz && \
    mv ModemStatus-0.0.02 ModemStatus

RUN ["scl", "enable", "rh-python36", "python", "-m", "venv", "virtenv"]

RUN source virtenv/bin/activate && \
    pip install --upgrade pip && \
    pip install /ModemStatus && \
    pip install -r /tmp/requirements.txt

#RUN chmod +x /tmp/create_virt_env.sh

#RUN ["scl", "enable", "rh-python36", "/tmp/create_virt_env.sh"]

CMD ["/tmp/run_script.sh"]