# Flask-Smart-Farm-API
Flask Smart Farm API

Code Structure
```
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```

# Deployment using docker-compose
```
docker build -t flask-smart-farm-api_app .
docker-compose up -d
```
Access using http://ip:5000

# Deployment using Kubernetes
```
docker build -t flask-smart-farm-api_app .
cd k8s
kubectl create -f smartfarmapp-deployment.yaml
kubectl create -f smartfarmapp-service.yaml
kubectl create -f smartfarmapp-service-nodeport.yaml
kubectl get deployment,pod,svc
```
Access using NodePort http://ip:nodeport

# Swaager API
![](/docs/img/screenshot.png)