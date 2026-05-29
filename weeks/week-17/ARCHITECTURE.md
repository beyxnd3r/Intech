
# Architecture (events-s06)

## 1. Общее описание

Проект `events-s06` — микросервисная система для управления событиями на основе варианта `variants/431/s06/week-17.json`.

Система состоит из 3 компонентов:

- `events-svc` — REST API на FastAPI для ресурсов `events`.
- `events-grpc-svc` — внутренний gRPC-сервис.
- `gateway` — Nginx gateway, который принимает внешние HTTP-запросы.

## 2. Состав и технология реализации

- Ресурс: `events`.
- Сущность: `event`.
- Дополнительное поле: `location: str`.
- REST-сервис: `events-svc`, внутренний порт `8257`, внешний порт в Docker Compose `8130`.
- Gateway route: `/api/events` -> `events-svc:8257`.
- Gateway: внутренний порт `8080`, внешний порт в Docker Compose `8085`.
- gRPC-сервис: `events-grpc-svc`, порт `8131`.
- Kubernetes app/container из варианта: `events-app` / `events-container`.
- Код проекта: `events-s06`.

## 3. Взаимодействие сервисов

```text
Client -> Gateway:8085 -> events-svc:8257
                 -> events-grpc-svc:8131
```

- Клиент отправляет HTTP-запрос на `http://localhost:8085/api/events`.
- Gateway проксирует запрос в `events-svc`.
- `events-svc` обрабатывает REST-запросы и хранит события в памяти (или в выбранном хранилище).
- `events-grpc-svc` запускает внутренний gRPC-сервер на порту `8131`.

## 4. REST API

- `GET /health` — healthcheck для Docker Compose.
- `GET /api/events` — список событий.
- `POST /api/events` — создание события.
- `PUT /api/events/{event_id}` — обновление события.
- `DELETE /api/events/{event_id}` — удаление события.

Swagger UI FastAPI доступен по адресу:

```text
http://localhost:8130/docs
```

## 5. Инфраструктура

### Docker Compose

Локальный запуск производится одной командой:

```bash
docker compose up --build
```

Сервисы работают в сети `events-network`.

### Helm

Helm chart находится в `weeks/week-17/helm/events-s06` и содержит манифесты для Kubernetes для всех трёх сервисов:

- Deployment/Service для `events-svc`.
- Deployment/Service для `events-grpc-svc`.
- Deployment/Service для `gateway`.

### CI/CD

GitHub Actions workflow `.github/workflows/ci.yml` выполняет:

- сборку и проверку зависимостей;
- тесты `make test WEEK=17`;
- сборку Docker-образов;
- `helm lint`;
- `helm template`;
- упаковку Helm chart как артефакт.
