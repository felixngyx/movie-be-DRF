# Django Backend Project

## Mô tả

Django Backend Project là một ứng dụng API được xây dựng bằng Django 5.1.2 và Django REST Framework. Dự án này cung cấp một nền tảng cho việc phát triển ứng dụng web hoặc di động, hỗ trợ xác thực JWT và các chức năng quản lý người dùng.

## Yêu cầu

Trước khi bắt đầu, hãy đảm bảo rằng bạn đã cài đặt các yêu cầu sau:

- Python 3.8 hoặc phiên bản cao hơn
- pip (trình quản lý gói Python)
- Django 5.1.2
- Django REST Framework

## Cài đặt

1. **Clone repository:**

   ```bash
   git clone https://github.com/felixngyx/movie-be-DRF.git
   cd movie-be-DRF
2. **Run Project**
    
    2.1 . Setup env
    ```bash
    python -m venv venv
    source venv/bin/activate  # MacOs / Linux
    venv\Scripts\activate     # Windows
    ```
    2.2 Run requirements.txt
    ```bash
    pip install -r requirements.txt
    ```

    2.3 . Migrate
    ```bash
    python manage.py migrate
    ```
    2.4 . Create superadmin account
    ```bash
    python manage.py createsuperuser
    ```

3. Run server
   ```
   python manage.py runserver
   ```


