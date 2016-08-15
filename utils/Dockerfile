FROM ubuntu
MAINTAINER Alex Georgescu <alexandru.c.georgescu@gmail.com>

# Installing pip, python, git
RUN apt-get update && apt-get install -y python python-pip git vim
RUN pip install --upgrade pip
RUN pip install tweepy nose ipython

# preparing git environment for running tests
RUN echo "colorscheme industry" > ~/.vimrc
RUN git config --global user.email "alexandru.c.georgescu@gmail.com"
RUN git config --global user.name "Alex Georgescu"

#testing with Volumes
#VOLUME /opt/test

RUN cd /opt &&  git clone https://github.com/sup3rfly/uv_twitter.git
RUN cd /opt/uv_twitter/ && git pull

# run the tests and store results in xml format file
WORKDIR /opt/uv_twitter/test

RUN nosetests  test_post.py test_get.py  -v --with-xunit --xunit-file=out.xml
