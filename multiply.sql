.output multiply.txt

select SUM(s)
FROM
(select (a.value * b.value) AS s
FROM a JOIN b ON a.col_num = b.row_num
WHERE a.row_num = 2 AND b.col_num = 3);