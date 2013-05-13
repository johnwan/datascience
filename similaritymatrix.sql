.output similaritymatrix.txt

select SUM(s)
FROM
(select (a.count * b.count) AS s
FROM (select * from Frequency WHERE docid = '10080_txt_crude')AS a JOIN 
     (select * from Frequency WHERE docid = '17035_txt_earn') AS b ON a.term = b.term);