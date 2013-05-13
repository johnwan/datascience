.output twowords.txt

select count(*)
from
(select docid
from frequency
WHERE term = 'transactions'
GROUP BY docid
HAVING docid IN
(SELECT docid FROM frequency
 WHERE term = 'world'));
