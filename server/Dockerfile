FROM python:3.6
MAINTAINER Dan Porter <dan.porter@farsetlabs.org.uk>

WORKDIR /server
# Get application requirements
ADD requirements ./requirements
RUN pip install -r requirements/test.txt
ADD Makefile ./Makefile

# Application content (mounted at runtime)
#ADD src ./src

EXPOSE 8000
