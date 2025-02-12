FROM php:fpm-alpine

WORKDIR /app

RUN apk add --no-cache gcc libc-dev

COPY ./src/start.sh .
RUN chmod +x ./start.sh

COPY ./flag.txt .
RUN mv ./flag.txt /root/flag.txt
RUN chmod 400 /root/flag.txt
COPY ./readflag.c /readflag.c
RUN gcc -o /readflag /readflag.c
RUN rm /readflag.c
RUN chmod u+s /readflag

EXPOSE 9000

CMD [ "./start.sh" ]
