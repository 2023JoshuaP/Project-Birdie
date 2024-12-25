# Birdie  

**_A social networking application with Django and React._**  
Aplicación de red social funcional que permite a los usuarios publicar contenido, visualizar, dar "me gusta" y comentar publicaciones, así como seguir y dejar de seguir a otros usuarios. Soporta modos de tema claro y oscuro.  

---

## 📚 Índice  

1. [Equipo](#equipo)  
2. [Propósito del Proyecto](#propósito-del-proyecto)  
   - [Objetivo](#objetivo)  
   - [Arquitectura de Software](#arquitectura-de-software)  
   - [Funcionalidades principales](#funcionalidades-principales)  
3. [Tecnologías](#tecnologías)  
   - [Lenguajes de Programación](#lenguajes-de-programación)  
   - [Frameworks](#frameworks)  
   - [Bibliotecas](#bibliotecas)  
   - [Herramientas de Construcción y Pruebas](#herramientas-de-construcción-y-pruebas)  

---

## 🧑‍💻 Equipo  

**Nombre del equipo:** Roar Omega Roar  

**Integrantes:**  
- Phiclo - El Delegado  
- Jose Alejandro - El Político  
- Deza - La Mano Derecha  
- Huertas - El Técnico  

---

## 🎯 Propósito del Proyecto  

### Objetivo  

Diseñar y desarrollar una aplicación de red social que sea escalable, moderna y eficiente, utilizando tecnologías actuales como Django y React para proporcionar una experiencia de usuario fluida y accesible desde múltiples dispositivos.  

### Arquitectura de Software  

La arquitectura de la aplicación sigue un enfoque basado en **Frontend-Backend**, dividido en dos capas principales:  

1. **Backend (Django + Django REST Framework):**  
   - Manejo de autenticación, gestión de usuarios, y lógica de negocio.  
   - API REST para comunicación con el frontend.  

2. **Frontend (React):**  
   - Interfaz de usuario dinámica.  
   - Enrutamiento y vistas interactivas para manejar publicaciones y perfiles.  

### Funcionalidades principales  

- **Registro e inicio de sesión para usuarios:**  
  Permite a los usuarios crear cuentas y acceder a la plataforma con credenciales seguras.  
  ![Registro](https://github.com/user-attachments/assets/7122061f-2ed7-490b-a717-bdb753c49e5e)  

- **Publicación de contenido:**  
  Los usuarios pueden crear publicaciones personalizadas para compartir con otros.  
  ![Publicaciones](https://github.com/user-attachments/assets/7613637f-905a-48f9-98bd-6bc7af8df41c)  

- **Interacciones:**  
  Los usuarios pueden dar "me gusta" y comentar en publicaciones, así como seguir o dejar de seguir a otros usuarios.  
  ![Likes](https://github.com/user-attachments/assets/4b51d3e8-3707-4559-a359-27bc3db73fdd)  

- **Ver perfil de usuario:**  
  Cada usuario tiene un perfil donde puede ver y gestionar su contenido e interacciones.  
  ![Perfil](https://github.com/user-attachments/assets/e823899f-5a19-43a3-8e35-9ff22d86f81f)  


---

## 🛠️ Tecnologías  

### Lenguajes de Programación  
- Python  
- JavaScript  

### Frameworks  
- Django y Django REST Framework (Backend)  
- React (Frontend)  

### Bibliotecas  
- React Router  
- Tailwind CSS  
- Material UI y Material UI Icons  

### Herramientas de Construcción y Pruebas  
- Virtualenv (para entornos virtuales en Python)  
- npm (gestión de dependencias para React)  

---
 

## CI/CD Pipeline Configuration

The CI/CD pipeline for Birdie is implemented using Jenkins with the following stages:

```groovy
pipeline {
    agent any
    tools {
        jdk 'PATH'
    }
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        ZAP_HOME = 'C:\\Program Files\\ZAP\\Zed Attack Proxy\\ZAP.bat'
    }
    stages {
        stage('GitHub Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/2023JoshuaP/Project-Birdie.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                bat """
                python -m venv venv
                venv\\Scripts\\activate
                pip install --upgrade pip setuptools
                pip install selenium pytest pytest-html
                """
            }
        }
        stage('Verify Syntax') {
            steps {
                bat """
                venv\\Scripts\\activate
                python -m compileall .
                """
            }
        }
        stage('Installation of Dependencies') {
            steps {
                dir('backend') {
                    bat "pip install -r requirements.txt"
                }
            }
        }
        stage('Install Specific Dependencies') {
            steps {
                dir('backend') {
                    bat """
                    ..\\venv\\Scripts\\activate
                    pip install django-cleanup unittest-xml-reporting
                    """
                }
            }
        }
        stage('Backend Unit Testing') {
            steps {
                dir('backend') {
                    bat """
                    ..\\venv\\Scripts\\activate
                    python manage.py test --verbosity 2
                    """
                }
            }
        }
        stage('Run Functional Tests') {
            steps {
                dir('frontend/birdie') {
                    bat """
                    ..\\venv\\Scripts\\activate
                    pytest --html=report.html test/ || exit 0
                    """
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'frontend/birdie/report.html', fingerprint: true
                }
            }
        }
        stage('OWASP ZAP Security Scan') {
            steps {
                dir('frontend/birdie') {
                    script {
                        def zap_jar_path = '"C:/Program Files/ZAP/Zed Attack Proxy/zap-2.15.0.jar"'
                        def target_url = 'http://localhost:3000'
                        def report_path = 'zap-reports/zap-report.html'
                        bat 'if not exist zap-reports mkdir zap-reports'
                        bat "java -Xmx512m -jar ${zap_jar_path} -cmd -host localhost -port 8097 -quickurl ${target_url} -quickout ${report_path}"
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'frontend/birdie/zap-reports/zap-report.html', fingerprint: true
                }
            }
        }
    }
}
```

