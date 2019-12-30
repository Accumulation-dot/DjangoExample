1. 创建schemas
``` mysql
create schema `schema_name` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2.数据库命令
```python
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
```