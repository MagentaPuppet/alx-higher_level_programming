-- displays the average temperatures (Fahrenheit) by city ordered by temperature (decending)
SELECT `city`, AVG(`value`) 'avg_temp' FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC
