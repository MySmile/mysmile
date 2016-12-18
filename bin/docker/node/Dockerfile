FROM node:0.12

# bower
RUN npm install -g bower

# install bower
RUN mkdir -p /mysmile/mysmile/static/vendor
WORKDIR /mysmile

ADD ./bower.json /mysmile/bower.json
ADD ./.bowerrc /mysmile/.bowerrc

RUN bower install --allow-root
