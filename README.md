# test_task-1

# Как запустить проект с помощью Docker:
- Соберите Docker-образ, используя команду docker build. Для этого откройте терминал, перейдите в директорию с вашим Dockerfile, и выполните следующую команду:
```
docker build -t my_server .
```
где my_server - это имя вашего образа (вы можете выбрать любое другое имя).

- После успешного завершения сборки образа, вы можете запустить контейнер на основе этого образа с помощью команды docker run. Например:
```
docker run -p 8080:8080 my_server
```
где -p 8080:8080 маппит порт 8080 вашего контейнера на порт 8080 вашей машины.

- После запуска контейнера вы сможете отправить запросы на ваш сервер, используя порт, на который он привязан (например, http://127.0.0.1:8080). Используйте Postman или браузер для отправки запросов и проверки работоспособности вашего сервера.

### Запуск тестов:

- Для запуска тестов необходимо воспользоваться командой `pytest`.
*Убедитесь, что у вас установлены все зависимости проекта, так как aiohttp требует специальные пакеты для настройки фикстур*.