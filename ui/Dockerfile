FROM node:carbon
MAINTAINER Dan Porter <dan.porter@farsetlabs.org.uk>

WORKDIR /ui
# Get application requirements
ADD package.json ./package.json
RUN npm install

# Application content (mounted at runtime)
#ADD src ./
