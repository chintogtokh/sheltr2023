FROM node:14-alpine3.15
WORKDIR /app
COPY . .
# RUN apk add --no-cache python2 make g++
RUN npm install --legacy-peer-deps
RUN npm run build
# ENV NODE_ENV production
EXPOSE 4000
CMD [ "node", "dist" ]