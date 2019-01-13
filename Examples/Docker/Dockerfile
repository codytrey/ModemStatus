FROM centos:7
LABEL maintainers="cody.t.belcher@gmail.com"

RUN yum -y update \
    && yum -y install centos-release-scl
    && yum -y install git \
    && yum -y install rh-python36

ARG PERIOD
ENV PERIOD ${PERIOD:-300}

COPY run_script.sh /tmp

RUN chmod +x /tmp/run_script.sh

RUN scl enable rh-python36 /tmp/create_virt_env.sh

CMD ["scl enable rh-python36 /tmp/run_script.sh"]