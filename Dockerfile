FROM python:3.7.6
WORKDIR assignment_fetch_rewards_mle
COPY . .
RUN pip install -r requirements.txt
EXPOSE 4500
CMD [ "flask", "run","--host","0.0.0.0","--port","4500"]