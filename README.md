# Elastic search for mobile search engine

## requirement

- Java
- elasticsearch 5.6
- Other Python library requirement is in requirement.txt already.
- ElasticSearch Head (Chrome Extension) (optional)

```bash
pip install -r /path/to/requirements.txt
```

- dataset เก็บเป็น json เพียวๆ ไว้ใน folder dataset

## Extra requirement (database)
กรณีเก็บผลลัพธ์ crawl ไว้ใน database
- mongodb
- pymongo

## init index สร้าง index
-  option มี 2 แบบ
   -  file คือดึงโดยตรงจากไฟล์
   -  db ดึงมาจาก db
      -  ใส่ไฟล์สงไปใน db
         ```bash
         bash put_docs_to_db.bash
            ```

- รันแค่ครั้งแรกที่ทำบนเครื่อง
- ใช้เวลารันประมาณ 9-10 นาทีทั้งสองแบบ

```python
from index import my_elasticSearch
els_obj = my_elasticSearch(option = 'db')
```

## search
- รับ query มาและพ่นผลลัพธ์ออกไป

```python
from search import searcher
result = search(self,query, sum_op = 'url', SENTENCES_COUNT=2)
```

- sum_op option ที่ใช้ทำสรุปจาก sumy เผื่อเอาไปโชว์หน้าเว็บ
 - url ใช้ url เป็น input ของตัว sumy อันนี้ผลสรุปโอเค แต่ช้า
 - text ใช้ text เราเป็น input ของตัว sumy สรุปไว ผลไม่โอเค (parser เรา parse ไม่ดีเอง)
 - no ไม่ทำสรุป

- SENTENCES_COUNT จำนวนประโยคที่ให้ sumy สรุปมาให้

- output list ของไฟล์ json เหมือนที่เราเก็บมา
 - ตัด remove_stopword_text ทิ้ง
 - เพิ่ม result['score'] เป็นคะแนนจาก elasticSearch
 - เพิ่ม result['summary'] สรุปหน้าเว็บในกรณี sum_op != no
