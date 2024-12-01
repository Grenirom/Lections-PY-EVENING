SQL - (Structured Query Language/Структурированный язык запросов) - Язык запросов, который позволяет обращаться и работать с БД (Создание/Чтение/изменение/удаление)

БД (База данных) - хранилище, в котором хранятся данные

СУБД (Система управления базой данных) - Система которая позволяет полноценно работать с базой данных при помощи SQL (только в SQl-СУБД), существует 2 вида СУБД:
    1) Реляционные(relational) - Реляционная СУБД позволяет связывать таблицы между собой
    2) Не реляционные(non relational) - БД которая не имеет связей, зачастую данные хранятся в паре {ключ: значение}

PostgreSQL - Реляционная СУБД при помощи который мы будем работать с базами данных
(PostgreSQL, SQLite, MySQL, и тд) - реляционные
(MongoDB, redis) - нереляционные

Основные команды PostgreSQL:

-- psql - команда, для того, чтобы войти в оболочку Postgres

-- \q  - команда для выхода из оболочки postgresql

-- \c <db_name> - команда для подключения к БД

-- \с - если не указывать название БД, то выведет сообщение в котором покажет к какой бд мы сейчас подключены, и под каким юзером

-- \l - команда, которая показывает весь список баз данных

-- \du - команда, которая показывает список всех пользователей и их прав

-- \dt - команда которая показывает все таблицы в текущей БД

-- \d+ - команда которая показывает более подробную информацию о таблицах


-----------------------------------ТИПЫ ДАННЫХ POSTGRESQL-----------------------------
ЧИСЛОВЫЕ ТИПЫ ДАННЫХ:
    1) smallint - хранит маленькие числа в диапозоне от -32767 до +32767, в памяти занимает 2 байта
    2) integer - хранит числа в более широком диапозоне, занимает 4 байта в памяти
    3) bigint - огромные числа в диапозоне -9223372036854775808 до +9223372036854775808, занимает 8 байт
    4) serial - числовой тип данных, у которого есть автоинкремент

СТРОКОВЫЕ ТИПЫ ДАННЫХ:
    1) char(character(n)) - строковый тип данных, который имеет фиксированную длину, указанную в скобках (указывать ограничение ОБЯЗАТЕЛЬНО) name CHAR(100)
    nikita    -- имя занимает 6 символов, оставшиеся 94 символа будут заполнены пробелами

    2) character varying(n) VARCHAR(100) - строковый тип данных который имеет переменную длину
    nikita - не заполняет оставшиеся 94 символа пробелами, просто срезает длину строки с 100 символов до 6

    3) text - строковый тип данных у которого произвольная длина

ТИПЫ ДАННЫХ ДЛЯ ДАТ И ВРЕМЕНИ:
    1) date - тип данных для хранения дат, занимает 4 байта в памяти
    2) time - тип данных для хранения времени, от 00.00.00 до 24.00.00, занимет 8 байта

БУЛЕВЫЕ ТИПЫ ДАННЫХ:
    1) true - истина, вместо этого значения, допускаются: "t", TRUE, "y", "yes", "1"
    2) false - ложь, вместо этого значения, допускаются: "f", FALSE, "0", "no"
    ... is_active boolean

JSON - тип данных для хранения данных в json формате

КОМАНДА ДЛЯ СОЗДАНИЯ БАЗЫ ДАННЫХ:
    CREATE DATABASE <db_name>;

КОМАНДА ДЛЯ УДАЛЕНИЯ БАЗЫ ДАННЫХ:
    DROP DATABASE <db_name>;


КОМАНДА ДЛЯ СОЗДАНИЯ ТАБЛИЦЫ:
    1) CREATE TABLE <name_of_table> (
        <column_name> <column_type>,
    );


КОМАНДА ДЛЯ УДАЛЕНИЯ ТАБЛИЦЫ:
    1) DROP TABLE <table_name>;

КОМАНДА ДЛЯ ЗАПОЛНЕНИЯ ТАБЛИЦ:
    1) INSERT INTO <table_name> (<column1>, <column2>, ...) VALUES (<value1>, <value2>, ...);

КОМАНДА ДЛЯ ВЫВОДА ЗАПИСЕЙ ИЗ ТАБЛИЦЫ:
    1) SELECT * FROM <name_of_table>;

КОМАНДА ДЛЯ УДАЛЕНИЯ ВСЕХ ЗАПИСЕЙ ИЗ ТАБЛИЦЫ:
    1) DELETE FROM <table_name>;

КОМАНДА ДЛЯ ОБНОВЛЕНИЯ ВСЕХ ЗАПИСЕЙ В ТАБЛИЦЕ:
    1) UPDATE <table_name> SET <column> = <new_value>;

УСЛОВИЯ:
    1) WHERE
        DELETE FROM <table_name> WHERE id=2;
        DELETE FROM <table_name> WHERE email='grebnev@gmail.com';

    2) like - Выбирает все записи, у которых в столбце name присутствует 'apple' (like ЧУВСТВИТЕЛЕН К РЕГИСТРУ, 'Apple' не найдет такую запись)
        ПРИМЕР: SELECT * FROM <table_name> WHERE name like '%apple%';

        ilike - Выбирает все записи, у которых в столбце name присутствует 'apple' (ilike НЕ ЧУВСТВИТЕЛЕН К РЕГИСТРУ, если вы введете 'Apple', то он найдет все записи, по этому условию, вне зависимости от того, какой регистр)

        ПРИМЕР: SELECT * FROM <table_name> WHERE name ilike '%apple%';

    3) ORDER BY - Условие, для сортировки по определенному полю, по дефолту ORDER BY сортирует по возрастанию (ASC)
    Пример: SELECT * FROM <table_name> ORDER BY <column>;
        -- В данном примере отсортирует по возрастанию все записи в таблице <table_name> по полю <column>
    
    4) ORDER BY - Условие, для сортировки по определенному полю, по дефолту ORDER BY сортирует по возрастанию (DESC)
    Пример: SELECT * FROM <table_name> ORDER BY <column> DESC;
        -- В данном примере отсортирует по убыванию все записи в таблице <table_name> по полю <column>
    (ASC - ascending/возрастание, DESC - descending/убывание)

    5) LIMIT - Условие, которое позволяет ограничивать выводимое количество ЗАПИСЕЙ
        ПРИМЕР: SELECT name FROM test_table LIMIT 3; -- выведет только 3 записи, но только поле name у этих записей
    6) OFFSET - Условие, которое позволяет пропустить какое то количество записей
        ПРИМЕР: SELECT * FROM test_table OFFSET 3; -- сначала пропустит первые 3 записи, а затем выведет все оставшиеся

        КОМБИНАЦИЯ LIMIT/OFFSET:
            SELECT * FROM test_table LIMIT 2 OFFSET 4; 

СВЯЗИ/PRIMARY KEY и FOREIGN KEY:
    1) PRIMARY KEY (Первичный ключ) (pk) - ключ, ограничение которое накладывается на поле, которое будет использовано в связях (это уникальный идентификационный ключ, зачастую применяется для ID, и на это уникальное поле будут ссылаться другие таблицы, для установления связи между ними)

    2) FOREIGN KEY (Внешний ключ) (fk) - ключ, ограничение которое накладывается на поле, которое ссылается на pk (PRIMARY KEY) в другой таблице (НАПРИМЕР: есть 2 таблицы, таблица passport, и таблица person, и в таблице passport будет поле 'person_id', это будет поле, которое ссылается на поле 'id' в таблице 'person')

    ПРИМЕР С ТАБЛИЦАМИ AUTHOR И BOOK:
        1) CREATE TABLE author (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_name VARCHAR(50)
        );

        2) CREATE TABLE book (
            id SERIAL PRIMARY KEY,
            title VARCHAR(50),
            author_id INT,

            CONSTRAINT fk_book_author FOREIGN KEY (author_id) REFERENCES author (id)
        );


ВИДЫ СВЯЗЕЙ МЕЖДУ ТАБЛИЦАМИ:
    1) One-to-One - один к одному, 1) один человек - один паспорт id 2) один автор - одна автобиография
    2) One-to-Many - один ко многим, 1) одна категория - много товаров
    3) Many-to-Many - многие ко многим, 1) один учитель - много учеников, один ученик - много учителей (много учителей - много учеников) 2) один разработчик - много проектов, один проект - много разработчиков (много разработчиков - много проектов)

    ПРИМЕРЫ СВЯЗЕЙ:
        1) one to one
            1) CREATE TABLE author (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50)
            );

            2) CREATE TABLE authobiography (
                id SERIAL PRIMARY KEY,
                body TEXT,
                author_id INT UNIQUE,

                CONSTRAINT fk_bio_author FOREIGN KEY (author_id) REFERENCES author (id)
            );
        2) One-to-Many
            1) CREATE TABLE author (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_name VARCHAR(50)
        );

            2) CREATE TABLE book (
            id SERIAL PRIMARY KEY,
            title VARCHAR(50),
            author_id INT,

            CONSTRAINT fk_book_author FOREIGN KEY (author_id) REFERENCES author (id)
        );

    3) Many to Many

        1) CREATE TABLE developer (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            language VARCHAR(50)
        );
        
        2) CREATE TABLE project (
            id SERIAL PRIMARY KEY,
            title VARCHAR(50),
            tz TEXT
        );
        
        3) CREATE TABLE dev_proj (
            id SERIAL PRIMARY KEY,
            developer_id INT,
            project_id INT,

            CONSTRAINT fk_develop FOREIGN KEY (developer_id) REFERENCES developer (id),
            CONSTRAINT fk_project FOREIGN KEY (project_id) REFERENCES project (id)
        );

JOIN - инструкция, которая позволяет в запросах SELECT выбирать данные из нескольких таблиц сразу
    ВИДЫ JOIN:
        INNER JOIN (JOIN) - достаются только те записи, у которых есть пара (у которых есть связь)
        FULL JOIN - достает все записи из обеих таблиц (вне зависимости от того, есть ли пара или нет)
        LEFT JOIN - достает все записи из левой таблицы, и из правой, если есть связь (пара)
        RIGHT JOIN - достает все записи из правой таблицы, и из левой, если есть связь (пара)

    * Где 'левая' таблица - та, которая пишется до JOIN, 'правая' - та которая пишется после JOIN

ПРИМЕР 1:

1) CREATE TABLE blogger (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

2) CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(20),
    body TEXT,
    blogger_id INT,
    created_at DATE,
    
    CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);


ПРИМЕР 2:

1) CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

2) CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    title VARCHAR(20),
    price DECIMAL
);

3) CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,

    CONSTRAINT fk_cart_customer FOREIGN KEY (customer_id) REFERENCES customer (id),
    CONSTRAINT fk_cart_product FOREIGN KEY (product_id) REFERENCES product (id)
);


АГРЕГАТНЫЕ ФУНКЦИИ:
    Агрегатные функции - это функции, которые помогают считать, складывать, находить минимум/максимум и другие вычисления для групп данных

    **ДЛЯ РАБОТЫ МНОГИХ АГРЕГАТНЫХ ФУНКЦИЙ ТРЕБУЕТСЯ ГРУППИРОВКА ЧЕРЕЗ ФУНКЦИЮ GROUP BY**

    COUNT - считает количество записей в сгруппированном поле

    ПРИМЕР ДЛЯ ФУНКЦИИ COUNT:
        --пример из blog 

        1) SELECT blogger.name, COUNT(post.id) AS posts_count FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY (blogger.name);

    ARRAY_AGG - объединяет записи сгруппированного поля в массив
        -- пример из blog

        1) SELECT blogger.name, ARRAY_AGG(post.title) AS post_titles FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY (blogger.name);

    
    SUM - Функция, которая находит сумму всех записей в сгруппированном виде
        -- пример из shop

        1) SELECT customer.name, SUM(product.price) AS total_price FROM product JOIN cart ON product.id = cart.product_id JOIN customer ON customer.id = cart.customer_id GROUP BY (customer.name);

    MIN, MAX - функции, которые находят минимальное и максимальное значения среди записей в сгруппированном виде
        -- пример из blog

        1) SELECT blogger.name, MIN(post.created_at) AS first_post, MAX(post.created_at) AS last_post FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY (blogger.name);


КОМАНДЫ ДЛЯ ИЗМЕНЕНИЯ ТАБЛИЦ:
    -- команда для добавления нового столбца(новой колонки)
        1) ALTER TABLE <table_name> ADD COLUMN <column_name> <data_type> <constraint>;

    -- команда для удаления столбца из таблицы
        1) ALTER TALBRE <table_name> DROP COLUMN <column_name>;

    -- команда для добавления ограничения на поле (столбец)
        1) ALTER TABLE <table_name> ADD CONSTRAINT <constraint_name> constraint;

        2) ALTER TABLE test ADD CONSTRAINT col_unq UNIQUE (col);
            -- test - название таблицы
            -- col_unq - название ограничения
            -- col - столбец

        ПРИМЕР:

        1) ALTER TABLE blogger ADD COLUMN email VARCHAR(20);

        2) ALTER TABLE blogger ADD CONSTRAINT email_unq UNIQUE (email);

        3) INSERT INTO blogger (email) VALUES ('n@gmail.com'), ('n@gmail.com');

    
    -- команда для того, чтобы переименовать название столбца
    ALTER TABLE <table_name> RENAME COLUMN <old_name> TO <new_name>;

IMPORT/EXPORT Базы данных

--IMPORT--
    1) psql <db_name> < file.sql

--EXPORT--
    1) pg_dump <db_name> > file.sql