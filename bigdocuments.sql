.output bigdocuments.txt

select count(*)
from
(select docid
from frequency
WHERE term = 'transactions' or term = 'world'
GROUP BY docid);
