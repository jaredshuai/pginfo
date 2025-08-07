# 设备信息管理系统 / Device Information Management System

这是一个设备信息管理系统，包含两个版本的后端实现：
- **Django REST Framework** 版本（原始实现）
- **FastAPI** 版本（新的现代化实现）

This is a device information management system with two backend implementations:
- **Django REST Framework** version (original implementation)  
- **FastAPI** version (new modern implementation)

## 功能特点

### 1. 设备信息管理
- 基本信息：名称、品牌、型号
- 设备照片上传和管理
- 产品说明书文档管理

### 2. 网络配置管理
- IP地址管理
- 子网掩码配置
- 网关设置

### 3. 地理位置管理
- 经度信息
- 纬度信息
- 支持地图定位

### 4. 远程控制配置
- 远程控制码
- 远程访问密码（安全存储）

## 技术栈 / Technology Stack

### Django 版本 / Django Version
- Python 3.8+
- Django 4.2.0+
- Django REST framework 3.14.0+
- Pillow 10.1.0+（图片处理）
- SQLite3（数据库）

### FastAPI 版本 / FastAPI Version
- Python 3.8+
- FastAPI
- SQLModel (ORM + Validation)
- Alembic (Database migrations)
- Uvicorn (ASGI server)
- PostgreSQL (推荐) / PostgreSQL (recommended)
- psycopg2-binary (PostgreSQL driver)

## 安装部署 / Installation & Deployment

### FastAPI 版本设置 / FastAPI Version Setup

#### 1. 克隆项目 / Clone the project
```bash
git clone [项目地址]
cd pginfo
```

#### 2. 创建虚拟环境（推荐）/ Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

#### 3. 安装依赖 / Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. 环境变量配置 / Environment Variables Setup
创建 `.env` 文件并配置数据库连接：
Create a `.env` file and configure database connection:

```bash
# PostgreSQL 数据库连接 / PostgreSQL Database Connection
DATABASE_URL=postgresql://username:password@localhost:5432/database_name

# 示例 / Example:
# DATABASE_URL=postgresql://pginfo_user:your_password@localhost:5432/pginfo_db
```

#### 5. 数据库迁移 / Database Migration
```bash
# 运行 Alembic 迁移创建数据库表 / Run Alembic migration to create database tables
alembic upgrade head
```

#### 6. 启动 FastAPI 服务器 / Start FastAPI Server
```bash
# 开发环境 / Development
uvicorn fastapi_app.main:app --reload --host 0.0.0.0 --port 8000

# 生产环境 / Production
uvicorn fastapi_app.main:app --host 0.0.0.0 --port 8000
```

#### 7. 访问 API 文档 / Access API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Django 版本设置 / Django Version Setup

#### 1. 安装依赖 / Install dependencies
```bash
pip install -r requirements.txt
```

#### 2. 数据库迁移 / Database Migration
```bash
python manage.py migrate
```

#### 3. 创建超级用户（可选）/ Create superuser (optional)
```bash
python manage.py createsuperuser
```

#### 4. 启动开发服务器 / Start development server
```bash
python manage.py runserver
```

## API 接口 / API Endpoints

### FastAPI 版本 / FastAPI Version

所有 API 响应都包装在统一格式中：`{"code": 0, "msg": "success", "data": {...}}`
All API responses are wrapped in a consistent format: `{"code": 0, "msg": "success", "data": {...}}`

#### 项目管理接口 / Project Management
- `GET /api/projects/` - 获取项目列表 / Get project list
  - 查询参数 / Query params: `name` (过滤 / filter)
- `POST /api/projects/` - 创建新项目 / Create new project
- `GET /api/projects/{id}/` - 获取项目详情（包含设备列表）/ Get project details (with device list)
- `PUT /api/projects/{id}/` - 更新项目信息 / Update project info
- `DELETE /api/projects/{id}/` - 删除项目 / Delete project
- `GET /api/projects/{id}/devices/` - 获取项目关联的设备列表 / Get devices for project

#### 设备管理接口 / Device Management
- `GET /api/devices/` - 获取设备列表 / Get device list
  - 查询参数 / Query params: `project_id`, `name`, `ip_address` (过滤和搜索 / filter and search)
- `POST /api/devices/` - 创建新设备 / Create new device
- `GET /api/devices/{id}/` - 获取设备详情 / Get device details
- `PUT /api/devices/{id}/` - 更新设备信息 / Update device info
- `DELETE /api/devices/{id}/` - 删除设备 / Delete device

### Django 版本 / Django Version

#### 设备管理接口 / Device Management
- `GET /api/devices/` - 获取设备列表
- `POST /api/devices/` - 创建新设备
- `GET /api/devices/{id}/` - 获取设备详情
- `PUT /api/devices/{id}/` - 更新设备信息
- `DELETE /api/devices/{id}/` - 删除设备

#### 项目管理接口 / Project Management
- `GET /api/projects/` - 获取项目列表
- `POST /api/projects/` - 创建新项目
- `GET /api/projects/{id}/` - 获取项目详情
- `PUT /api/projects/{id}/` - 更新项目信息
- `DELETE /api/projects/{id}/` - 删除项目

## 文件存储

- 设备照片存储路径：`media/devices/photos/`
- 产品说明书存储路径：`media/devices/manuals/`

## 开发说明 / Development Guide

### FastAPI 项目结构 / FastAPI Project Structure
```
pginfo/
├── fastapi_app/          # FastAPI 应用目录 / FastAPI application directory
│   ├── main.py          # 主应用文件 / Main application file
│   ├── models.py        # SQLModel 数据模型 / SQLModel data models
│   ├── database.py      # 数据库连接配置 / Database connection setup
│   ├── response.py      # 统一响应格式 / Unified response format
│   └── routers/         # API 路由 / API routers
│       ├── projects.py  # 项目管理路由 / Project management routes
│       └── devices.py   # 设备管理路由 / Device management routes
├── alembic/             # 数据库迁移 / Database migrations
│   ├── versions/        # 迁移版本文件 / Migration version files
│   └── env.py          # Alembic 环境配置 / Alembic environment config
├── alembic.ini          # Alembic 配置文件 / Alembic configuration
└── requirements.txt     # 项目依赖 / Project dependencies
```

### Django 项目结构 / Django Project Structure
```
pginfo/
├── apps/
│   ├── devices/          # 设备管理应用
│   │   ├── models.py     # 设备数据模型
│   │   ├── serializers.py# 序列化器
│   │   ├── views.py      # 视图逻辑
│   │   └── urls.py       # URL配置
│   └── projects/         # 项目管理应用
├── pginfobackend/        # Django 项目配置
├── media/                # 媒体文件目录
├── static/               # 静态文件目录
├── templates/            # 模板目录
└── manage.py            # Django管理脚本
```

### 数据模型 / Data Models

#### FastAPI 版本 (SQLModel) / FastAPI Version (SQLModel)

**Project 模型 / Project Model:**
- `id`: Integer (主键 / Primary Key)
- `name`: String (项目名称 / Project Name)
- `description`: String (可选，项目描述 / Optional, Project Description)
- `created_at`: DateTime (创建时间 / Creation Time)
- `updated_at`: DateTime (更新时间 / Update Time)

**Device 模型 / Device Model:**
- `id`: Integer (主键 / Primary Key)
- `name`: String (设备名称 / Device Name)
- `brand`: String (可选，品牌 / Optional, Brand)
- `model`: String (可选，型号 / Optional, Model)
- `ip_address`: String (可选，IP地址 / Optional, IP Address)
- `subnet_mask`: String (可选，子网掩码 / Optional, Subnet Mask)
- `gateway`: String (可选，网关 / Optional, Gateway)
- `location`: String (可选，位置 / Optional, Location)
- `longitude`: Float (可选，经度 / Optional, Longitude)
- `latitude`: Float (可选，纬度 / Optional, Latitude)
- `status`: Enum (状态：ONLINE/OFFLINE/ERROR / Status: ONLINE/OFFLINE/ERROR)
- `photo`: String (可选，照片路径 / Optional, Photo Path)
- `product_manual`: String (可选，说明书路径 / Optional, Manual Path)
- `remote_code`: String (可选，远程控制码 / Optional, Remote Code)
- `remote_password`: String (可选，远程密码 / Optional, Remote Password)
- `project_id`: Integer (外键，关联项目 / Foreign Key, Related Project)
- `created_at`: DateTime (创建时间 / Creation Time)
- `updated_at`: DateTime (更新时间 / Update Time)

#### Django 版本 / Django Version
设备模型包含以下主要字段：
- 基本信息：`name`, `brand`, `model`
- 网络信息：`ip_address`, `subnet_mask`, `gateway`
- 位置信息：`longitude`, `latitude`
- 文件字段：`photo`, `product_manual`
- 控制信息：`remote_code`, `remote_password`

## 注意事项

1. 生产环境部署时请修改 `settings.py` 中的以下配置：
   - `DEBUG = False`
   - `SECRET_KEY`
   - `ALLOWED_HOSTS`

2. 文件上传
   - 支持的图片格式：JPG, PNG, GIF
   - 支持的文档格式：PDF, DOC, DOCX

3. 安全性
   - 远程控制密码在API响应中不可见
   - 建议使用HTTPS进行传输
   - 建议配置跨域保护

## 许可证

[许可证类型] 





