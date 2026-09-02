FROM node:22-alpine

WORKDIR /user/src/app

COPY package.json package-lock.json* .

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node","app.js"]