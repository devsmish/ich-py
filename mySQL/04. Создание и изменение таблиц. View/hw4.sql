-- 1 Подключитесь к своей базе данных созданной на уроке
use 101025__group;

-- 2 Создайте таблицу, которая отражает погоду в Вашем городе за последние 5 дней и включает следующее столбцы
-- Id - первичный ключ, заполняется автоматически
-- Дата - не может быть пропуском
-- Дневная температура - целое число, принимает значения от -30 до 30
-- Ночная температура - целое число, принимает значения от -30 до 30
-- Скорость ветра - подумайте какой тип данных и ограничения необходимы для этого столбца
create table weather (
    id int primary key auto_increment,
    `date` date not null,
    day_temp int check (day_temp between -30 and 30),
    night_temp int check (night_temp between -30 and 30),
    wind_speed decimal(4, 2) check (wind_speed >= 0)
);

CREATE TABLE weather (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date_d DATE NOT NULL,
    d_temperature TINYINT CHECK (-30 <= d_temperature <= 30),
    n_temperature TINYINT CHECK (-30 <= n_temperature <= 30),
    wind_speed_ms TINYINT CHECK (0 <= wind_speed_ms <= 100)
);

-- 3 Заполните таблицу 5 строками - за последние 5 дней 
insert into weather 
	(`date`, day_temp, night_temp, wind_speed)
VALUES 
	(date_sub(current_date, interval 4 day), 16, 6, 3.25),
	(date_sub(current_date, interval 3 day), 18, 9, 2.5),
	(date_sub(current_date, interval 2 day), 20, 12, 4),
	(date_sub(current_date, interval 1 day), 19, 11, 21.7),
	(current_date, -13, -17, 3.5);

insert into weather 
	(`date`, day_temp, night_temp, wind_speed)
VALUES
	('2025-05-24', 18, 5, 2),
	('2025-05-25', 16, 10, 8),
	('2025-05-26', 20, 9, 4),
	('2025-05-27', 17, 8, 9),
	('2025-05-28', 16, 6, 5);

-- 4 Увеличьте значения ночной температуры на градус если скорость ветра не превышала 3 м/с
set sql_safe_updates = 0;

update weather
set night_temp = night_temp + 1
where wind_speed <= 3;


-- 5 На основе полученной таблицы создайте представление в своей базе данных 
-- включите все строки Вашей таблицы и дополнительно рассчитанные столбцы
-- Средняя суточная температура - среднее арифметическое между ночной и дневной температурами
-- Столбец на основе скорости ветра - если скорость ветра не превышала 2 м/с то значение ‘штиль’, 
-- от 2 до 5 включительно - ‘умеренный ветер’, в остальных случаях - 
-- ‘сильный ветер’
create or REPLACE view view_weather as
select *,
round((day_temp + night_temp) / 2, 2) as average_temperature,
case
	when wind_speed <= 2 then "штиль"
	when wind_speed > 2 and wind_speed <= 5 then "умеренный ветер"
	-- when wind_speed BETWEEN 2 AND 5 then "умеренный ветер"
	when wind_speed > 5 then "сильный ветер"
	else "нет данных"
end as wind_type
from weather;


SELECT * FROM weather;
