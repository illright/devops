FROM node:16-alpine AS builder

RUN mkdir -p /app
WORKDIR /app

RUN npm install -g pnpm

COPY .eslintrc.js package.json pnpm-lock.yaml rollup.config.js /app/
RUN pnpm install

COPY src /app/src
COPY public /app/public

RUN pnpm build



FROM node:16-alpine

RUN mkdir -p /app
WORKDIR /app

COPY --from=builder /app/public public
COPY --from=builder /app/package.json .

RUN npm install --omit dev

EXPOSE 3000

CMD ["npm", "start", "--", "--port", "3000", "--host", "0.0.0.0"]
