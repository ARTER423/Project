# Project
pythonProject22/

├── static/              
│   ├── css/
│   │   └── styles.css

│   ├── js/
│   │   └── script.js

│   └── images/           
│       ├── panda_logo.png
│       └── background.jpg

├── templates/              
│   └── index.html

├── deployment/          
│   ├── environments/        
│   │   ├── dev/            
│   │   │   └── .env          
│   │   ├── staging/        
│   │   │   └── .env
│   │   └── prod/         
│   │       └── .env
│   ├── scripts/             
│   │   ├── install.sh       
│   │   ├── configure.sh     
│   │   ├── start.sh         
│   │   ├── stop.sh         
│   │   └── database/
│   │       └── migrate_db.py  
│   ├── ci_cd/              
│   │   └── .gitlab-ci.yml   
│   └── README.md           
├── docs/                  
│   ├── deployment.md      
│   └── operations.md     
├── database.py           
├── main.py              
├── models.py            
├── requirements.txt      
├── README.md            
└── crazy_panda.db
