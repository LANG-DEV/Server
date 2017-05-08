aws ecr get-login --region us-west-2
docker build -t lang:latest .
docker tag lang:latest 766193532162.dkr.ecr.us-west-2.amazonaws.com/lang:latest
docker push 766193532162.dkr.ecr.us-west-2.amazonaws.com/lang:latest