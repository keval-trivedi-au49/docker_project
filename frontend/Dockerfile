FROM node:22-alpine

WORKDIR /user/src/app

COPY package.json package-lock.json* .

RUN npm ci --omit=dev

COPY . .

EXPOSE 3000

CMD ["node","app.js"]