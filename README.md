# Диплом по курсу «Django: создание функциональных веб-приложений»

## По  курсу Django - разработка функциональных веб-приложений

## Инструкция по установке

- Установите зависимости: python pip install -r requirements.txt

- Выполните миграции: python manage.py migrate

- Загрузите тестовые данные в базу: python manage.py loaddata fixtures.json

- Запустите тестовый сервер python manage.py runserver --settings=settings.local

- Тестовый суперпользователь: 
                              логин: admin@test.ru
                              пароль: admin
                              
                              
                              
                              
## Задание 

Разработать сайт интернет-магазина.
Должна быть реализована клиентская часть сервиса и интерфейс администрирования.


### Описание клиентской части

Просмотр товара и добавление в корзину (рядом с каждым товаром должна быть кнопка добавления в корзину).

* Главная страница со статьями о подборке товаров (отсортированы по дате создания статьи)
  и перечислением этих товаров.
* Страница категории товара со списком товаров с пагинацией.
* Страница товара с подробным описанием.
    
Меню:

* Ссылка на главную страницу.
* Ссылки на разделы (разделы могут иметь иерархию).
* Ссылка на корзину.
* Кнопка входа/выхода в зависимости от статуса авторизации.

Корзина со списком выбранных товаров, привязанных к пользователю.
Кнопка заказа должна создавать заказ и очищать корзину.

Для входа использовать аутентификацию по email'у.


### Интерфейс администратора

* Редактирование разделов.
* Редактирование товаров.
* Редактирование статей на главной странице и привязывание к ним товаров,
  которые должны отображаться после нее.
* Просмотр списка заказов пользователей, отсортированных по дате создания,
    с указанием пользователя и количества товаров.
* Страница детализации заказа с просмотром списка заказанных товаров.

### Дизайн

* [Главная страница](./resources/index.html).
* [Страница раздела](./resources/smartphones.html).
* [Страница незаполненного раздела](./resources/empty_section.html).
* [Страница товара](./resources/phone.html).
* [Страница корзины](./resources/cart.html).
* [Страница входа](./resources/login.html).

### Требования к организации системы

* Система должна быть реализована на Django версии 2.
* Интерфейс администратора должен быть создан стандартными средствами Django admin.
* В качестве СУБД использовать sqlite.
* Система при работе не должна вызывать исключений и ошибок.

### Что необходимо предоставить по проекту

* Миграции для создания базы данных.
* Инструкции по установке и первому запуску. Файл `README.md` в папке проекта.
* Дамп данных с тестовым наполнением `fixtures.json`,
  с тестовым суперпользователем с именем `admin` и паролем `admin` (команда `manage.py dumpdata` для создания дампа).

### Дополнительные задачи

* Реализовать механизм анонимных отзывов как показано на макете [Страница товара](./resources/phone.html).
* Реализовать возможность регистрации по почте (без подтверждения почты).