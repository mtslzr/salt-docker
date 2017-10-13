FROM ubuntu:16.04
MAINTAINER Matthew Salazar

RUN apt-get update && apt-get install -y wget
RUN wget -O - https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub | apt-key add -
RUN echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main" >> /etc/apt/sources.list.d/saltstack.list
RUN apt-get update

RUN apt-get install -y salt-master salt-minion salt-ssh salt-syndic salt-cloud salt-api
EXPOSE 4505 4506

CMD ["/usr/bin/salt-master"]