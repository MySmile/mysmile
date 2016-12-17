FROM python:3.5
ARG python='python3.5'

ENV PYTHONUNBUFFERED 1

RUN apt-get update

# upgrade
RUN pip install --upgrade pip

# requirements
RUN mkdir -p /mysmile/config/requirements
WORKDIR /mysmile

ADD ./config/requirements/local.txt /mysmile/config/requirements
RUN pip install -r /mysmile/config/requirements/local.txt

# ssh, source https://docs.docker.com/engine/examples/running_ssh_service/ with correction https://github.com/docker/docker/issues/23621#issuecomment-226575258
RUN apt-get -y install openssh-server

RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# supervisor
RUN apt-get install -y supervisor
RUN mkdir -p  /var/log/supervisor
ADD ./bin/docker/web/config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# expose ports
EXPOSE 22 8002
CMD ["supervisord", "--configuration", "/etc/supervisor/conf.d/supervisord.conf", "--logfile", "/var/log/supervisor/supervisord.log", "--logfile_maxbytes", "5000000", "--logfile_backups", "5", "--pidfile", "/var/tmp/supervisord.pid"]
