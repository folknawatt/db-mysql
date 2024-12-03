# MySQL Database Setup 🗄️

## 📋 Project Overview
This project provides a dockerized MySQL database setup with phpMyAdmin for easy database management and SQLAlchemy as the Object-Relational Mapping (ORM) tool.

## 🛠 Tools Stack
### Database and ORM
- **Database**: MySQL:lastest
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
  - Additional Thai Language Reference: [Phyblas Tutorial](https://phyblas.hinaboshi.com/20200529)

### Database Management
- **Admin Tool**: [phpMyAdmin](https://hub.docker.com/_/phpmyadmin)

## 🚀 Getting Started

### Prerequisites
- Docker
- Docker Compose
- Python 3.8+

### Installation Steps

 **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

 **Start Services**
   ```bash
   docker compose up -d --build
   ```

## 🔍 Service Access

### phpMyAdmin
- **URL**: http://localhost:8080

## 📌 References
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [การจัดการฐานข้อมูล sql ในแบบออบเจ็กต์ใน python ด้วย sqlalchemy](https://phyblas.hinaboshi.com/20200529) 
- [Docker MySQL Image](https://hub.docker.com/_/mysql)
- [phpMyAdmin Docker Image](https://hub.docker.com/_/phpmyadmin)
