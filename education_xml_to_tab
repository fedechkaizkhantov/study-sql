select
    value,
    regexp_substr(value, '\d+') as id,
    regexp_substr(substr(value, instr(value, '<h1>')+4), '[^:|</]{0,100}') as category,
    regexp_substr(substr(value, instr(value, '<p class="title">')+17), '[^:|</]{0,100}') as name,
    regexp_substr(substr(regexp_replace(value, ' Ý', 'Ý'), instr(regexp_replace(value, ' Ý', 'Ý'), '<p class="author">')+18), '[^:|</]{0,100}') as author,
    regexp_substr(substr(value, instr(value, '<p class="price">')+17), '(\d+){0,5}') as price
from data
