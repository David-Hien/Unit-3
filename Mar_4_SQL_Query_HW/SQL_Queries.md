## Code
``` sql
-- Nagisa: List of cites with the number of murders in descending order
SELECT city, count(city) as freq from crime_scene_report where type='murder' group by city order by freq desc;

-- Reiji: List of people who own a Mercedes-Benz
SELECT count(car_make) from drivers_license where car_make='Mercedes-Benz';

-- Bee: List of streets and number of people living in descending order
SELECT address_street_name, count(address_street_name) as freq from person group by address_street_name order by freq desc;

-- Elia: Number of theft report in SQL City
SELECT count(type) from crime_scene_report where city='SQL City' and type='theft';

-- Kojiro: Number of Facebook event in July 2017
SELECT count(event_name) from facebook_event_checkin where date like '201707%';

-- David: List of annual income of people with gold gym membership - using subquery and inner join
SELECT annual_income, ssn from income where ssn in (SELECT ssn from person where id in (SELECT person_id from get_fit_now_member where membership_status='gold'));
SELECT p.name, annual_income from income inner join person p on income.ssn = p.ssn inner join get_fit_now_member gfnm on p.id = gfnm.person_id where membership_status='gold';

-- Anju: Number of crimes at night - insufficient data

-- Michael: List of months with the number of crimes in descending order - biased because data include 12 months in 2017 and 5 months in 2018
SELECT substr(date, 5, 2), count(substr(date, 5, 2)) as freq from crime_scene_report group by substr(date, 5, 2) order by freq desc;

-- Aup: Number of crimes involved nudism
SELECT count(type) from crime_scene_report where description like 'nudism%';

```

## UML Diagram

![March_6th_UML](https://user-images.githubusercontent.com/89367058/158045611-028f2fdf-b498-4623-b9e5-25af0a37ab0b.png)

