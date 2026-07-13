

-- =========================================
-- SQL Analytics Layer for First 10 Years
-- Purpose: Enable reproducible, scalable analysis for BI tools
-- Dataset limited to first 10 years of data
-- =========================================

/* select * from calgary_energy_preprocessed;*/


/* select count(*) 
from calgary_energy_preprocessed;*/

/*SELECT 
    COUNT(*) AS total_records,
    SUM(energy_kwh) AS total_sum,
    MIN(energy_kwh) AS min_value,
    MAX(energy_kwh) AS max_value,
    AVG(energy_kwh) AS avg_value
FROM calgary_energy_preprocessed;*/


-- 1. Total energy produced per site
/* SELECT 
    name,
    SUM(energy_kwh) AS total_energy_kwh,
    AVG(energy_kwh) AS average_energy_kwh
FROM calgary_energy_preprocessed
GROUP BY name;*/


 /* SELECT name,
    SUM(energy_kwh) AS total_energy_kwh,
    AVG(energy_kwh) AS avg_energy_kwh
FROM calgary_energy_preprocessed
GROUP BY name
ORDER BY total_energy_kwh DESC;  -- Sort by highest total*/


-- 2. Average energy per hour of day
/* SELECT 
    HOUR(datetime) AS hour_of_day,
    AVG(energy_kwh) AS avg_energy_kwh
FROM calgary_energy_preprocessed
GROUP BY HOUR(datetime)
ORDER BY hour_of_day;*/

-- 3 Maximum Energy per Day
/*SELECT DATE(datetime) AS day, 
       MAX(energy_kwh) AS max_energy
FROM calgary_energy_preprocessed
GROUP BY day
ORDER BY day;*/

-- 4 Number of Records per Month
/*SELECT 
    YEAR(datetime) AS year,
    MONTH(datetime) AS month,
    COUNT(*) AS record_count
FROM calgary_energy_preprocessed
GROUP BY YEAR(datetime), MONTH(datetime)
ORDER BY year, month;*/


-- 5 Monthly Total Energy
/*SELECT YEAR(datetime) AS year,
       MONTH(datetime) AS month,
       SUM(energy_kwh) AS monthly_energy
FROM calgary_energy_preprocessed
GROUP BY YEAR(datetime),MONTH(datetime)
ORDER BY year, month;*/


-- 6 Average Energy per Season

/*select season , avg(energy_kwh) as avg_energy
from calgary_energy_preprocessed
group by season;*/

-- 6.1. Create a new permanent table
/*CREATE TABLE season_energy_avg AS
SELECT season,
       AVG(energy_kwh) AS avg_energy_kwh,
       COUNT(*) AS record_count,
       SUM(energy_kwh) AS total_energy_kwh
FROM calgary_energy_preprocessed
GROUP BY season
ORDER BY avg_energy_kwh DESC;*/

/*SELECT * FROM season_energy_avg;*/

-- 7 Records Where Energy > 5 kWh
/*select * from calgary_energy_preprocessed
where energy_kwh > 5 */

-- 8 peak Energy per Site
/* create view  peak_nergy as
SELECT name, 
       MAX(energy_kwh) AS peak_energy
FROM calgary_energy_preprocessed
GROUP BY name
ORDER BY peak_energy DESC;*/

/*SELECT * FROM peak_nergy*/


 -- 9. Records higher than daily average
/* WITH daily_avg AS (
    SELECT DATE(datetime) AS day,
           AVG(energy_kwh) AS avg_energy
    FROM calgary_energy_preprocessed
    GROUP BY day
)
SELECT c.*
FROM calgary_energy_preprocessed c
JOIN daily_avg d ON DATE(c.datetime) = d.day
WHERE c.energy_kwh > d.avg_energy
ORDER BY datetime;*/
 
 
 -- 10. Top 5 peak hours per site
/*SELECT 
    name, 
    SUM(energy_kwh) AS total_energy_kwh, 
    AVG(energy_kwh) AS average_energy_kwh
FROM calgary_energy_preprocessed 
GROUP BY name 
ORDER BY average_energy_kwh DESC 
LIMIT 5;*/
 
 
 -- 11. Total energy per installation date
 /*SELECT installationdate, 
       SUM(energy_kwh) AS total_energy
FROM calgary_energy_preprocessed
GROUP BY installationdate*/
 
 
 -- 12. Average energy per day of year
SELECT DAYOFYEAR(datetime) AS day_of_year,
       AVG(energy_kwh) AS avg_energy
FROM calgary_energy_preprocessed
GROUP BY DAYOFYEAR(datetime)
ORDER BY day_of_year
LIMIT 1000;

 
 
 
 







