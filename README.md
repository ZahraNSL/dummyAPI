# 🚀 API Testing with Docker & Pytest

This project contains an **API** built with Flask and tested using **Pytest** inside **Docker containers**. It includes **Docker networking** to run the API and test containers separately.

---

## 📌 **How to Run the API (Without Docker)**
If you want to run the API **without Docker**, follow these steps:

### ** Install dependencies**
```sh
pip install -r requirement.txt
```
### ** Run the API**
```sh
python API.py
```
### ** Test the API Manually**
```sh
curl -X POST http://127.0.0.1:5000/transform -H "Content-Type: application/json" -d '{"text": "hello"}'
```
## 📌 **How to Run the API with Docker**
If you prefer running the API **inside Docker**, follow these steps:

### **  Build the Docker Image**
```sh
docker build -t my-api .
```

### **  Create a Docker Network**
```sh
docker network create test-network || true
```

### ** Run the API Container**
```sh
docker run -d --name api-container --network test-network -p 5001:5000 my-api
```

### ** Test API**
```sh
curl -X POST http://127.0.0.1:5001/transform -H "Content-Type: application/json" -d '{"text": "hello"}'
```

## 📌 **How to Run tests in Docker**
to run tests **inside Docker**, use:

### **  Build the Test Image**
```sh
docker build -t my-api-test -f Dockerfiletest .
```

### ** Run Tests in a Separate Container**
```sh
docker run --rm --network test-network my-api-test
```

## 📌 **Using docker-compose**
Instead of running everything manually, you can use **docker-compose.yml**.

### **Start API & Tests**
```sh
docker-compose up --build
```