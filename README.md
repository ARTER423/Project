# Project
pythonProject22/  # (или CrazyPanda, если хотите назвать репозиторий также)
├── static/                 # Статические файлы (CSS, JavaScript, изображения)
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   └── images/             # (Рекомендуется для упорядочивания изображений)
│       ├── panda_logo.png
│       └── background.jpg
├── templates/              # Шаблоны Jinja2
│   └── index.html
├── deployment/           # Всё для развертывания
│   ├── environments/          # Конфигурации для разных сред
│   │   ├── dev/             # Конфигурация для dev
│   │   │   └── .env          # Конфигурационный файл (пример)
│   │   ├── staging/         # Конфигурация для staging
│   │   │   └── .env
│   │   └── prod/            # Конфигурация для production
│   │       └── .env
│   ├── scripts/             # Скрипты автоматизации развертывания
│   │   ├── install.sh       # Общий скрипт установки всего необходимого
│   │   ├── configure.sh     # Скрипт настройки приложения
│   │   ├── start.sh         # Скрипт запуска приложения
│   │   ├── stop.sh          # Скрипт остановки приложения
│   │   └── database/
│   │       └── migrate_db.py  # Скрипт миграции базы данных (если используется Alembic)
│   ├── ci_cd/              # Конфигурация CI/CD
│   │   └── .gitlab-ci.yml   # (или Jenkinsfile, GitHub Actions YML)
│   └── README.md            # Информация по деплою
├── docs/                   # Документация
│   ├── deployment.md      # Документация по развертыванию
│   └── operations.md      # Документация по эксплуатации
├── database.py           # Работа с БД (SqlAlchemy)
├── main.py               # FastAPI
├── models.py             # Модели SqlAlchemy
├── requirements.txt      # Зависимости
├── README.md             # Описание проекта
└── crazy_panda.db        # Database (не обязательно в репозиторий, можно исключить через .gitignore)
