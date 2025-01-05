# Практическая работа - RESTful веб-приложение на Spring Boot

Выполнил: студент ИВТ, 4 курс, группа 2, Родионов Родион
## Цель работы:
Создать RESTful веб-приложение “Task Management System” для управления задачами с использованием Spring Boot, применяя ключевые компоненты фреймворка, включая автоматическую конфигурацию, стартеры, работу с базой данных и безопасность.

## Реализация
Сгенерировал проект с помощью [Spring initializr](https://start.spring.io/)  
_[Ссылка на Spring initializr с добавленными зависимостями](https://start.spring.io/#!type=maven-project&language=java&platformVersion=3.4.1&packaging=jar&jvmVersion=17&groupId=com.example&artifactId=demo&name=demo&description=Demo%20project%20for%20Spring%20Boot&packageName=com.example.demo&dependencies=web,data-jpa,h2,security,lombok)_  

### Структура проекта
**src/main/java/com/example/taskmanagement/  
├── config**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Конфигурации приложения (например, Spring Security)_  
**│ └── SecurityConfig.java  
├── controller**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# _REST-контроллеры для обработки HTTP запросов_  
**│ └── TaskController.java  
├── model**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Классы моделей данных (Entity)_  
**│ └── Task.java  
├── repository**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Интерфейсы для взаимодействия с базой данных_  
**│ └── TaskRepository.java  
├── service**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Слой бизнес-логики_  
**│ └── TaskService.java  
└── TaskManagementApplication.java**  
### Запуск приложения
Чтобы установить зависимости из pom.xml  
❯ mvn clean install  
Запускал приложение в VS Code  
![Screenshot4](https://github.com/jack-lull/Herzen-University/blob/main/4term/prog7/RESTful_SpringBoot/assets/screenshot4.png)
## Тестирование проекта
С помощью Postman проверил работает ли приложение, смог создать задачу  
![Screenshot1](https://github.com/jack-lull/Herzen-University/blob/main/4term/prog7/RESTful_SpringBoot/assets/screenshot1.png)<br>
Далее проверил задачу в h2-console
Смог войти по заданным кредам  
![Screenshot3](https://github.com/jack-lull/Herzen-University/blob/main/4term/prog7/RESTful_SpringBoot/assets/screenshot3.png)<br>
Проверил наличие задачи  
![Screenshot2](https://github.com/jack-lull/Herzen-University/blob/main/4term/prog7/RESTful_SpringBoot/assets/screenshot2.png)
### Версионирование
OpenJDK 17.0.13  
Apache Maven 3.9.9  
Spring Boot 3.4.1  
