# -*- coding: utf-8 -*-
# MIT License

# Copyright (c) 2020-present largecats

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import logging
from sparksqlformatter.src import api
from sparksqlformatter.src.formatter import Formatter
from sparksqlformatter.src.config import Config

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)


class Test:
    def __init__(self):
        pass


#     def test_create_table_using_data_source(self):
#         msg = 'Testing create table using data source'
#         testQuery = '''
# CREATE TABLE xxx
#     (time string, amount double, country string, date date)
#     USING org.apache.spark.sql.parquet
#     OPTIONS ('serialization.format'='1', 'path'='/user/xxx', 'mergeSchema'='true')
#     PARTITIONED BY (country, date)
#         '''
#         key = '''
# CREATE TABLE
#     xxx (time string, amount double, country string, date date)
#     USING org.apache.spark.sql.parquet
#     OPTIONS ('serialization.format' = '1', 'path' = '/user/xxx', 'mergeSchema' = 'true')
#     PARTITIONED BY (country, date)
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_insert_without_into(self):
#         msg = 'Testing INSERT without INTO'
#         testQuery = '''INSERT Customers (ID, MoneyBalance, Address, City) VALUES (12, -123.4, 'Skagen 2111','Stv')'''
#         key = '''
# INSERT
#     Customers (ID, MoneyBalance, Address, City)
# VALUES
#     (12, -123.4, 'Skagen 2111', 'Stv')
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_alter_table_modify(self):
#         msg = 'Testing ALTER TABLE ... MODIFY query'
#         testQuery = '''ALTER TABLE supplier MODIFY supplier_name STRING(100) NOT NULL'''
#         key = '''
# ALTER TABLE
#     supplier
# MODIFY
#     supplier_name STRING(100) NOT NULL
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_alter_table_alter_column(self):
#         msg = 'Testing ALTER TABLE ... ALTER COLUMN query'
#         testQuery = '''ALTER TABLE supplier ALTER COLUMN supplier_name STRING(100) NOT NULL'''
#         key = '''
# ALTER TABLE
#     supplier
# ALTER COLUMN
#     supplier_name STRING(100) NOT NULL
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_simple_select(self):
#         msg = 'Testing simple SELECT'
#         testQuery = '''SELECT c1, c2 FROM t0'''
#         key = '''
# SELECT
#     c1,
#     c2
# FROM
#     t0
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_select_with_left_join(self):
#         msg = 'Testing SELECT query with LEFT JOIN'
#         testQuery = '''SELECT a, b FROM t LEFT JOIN t2 ON t.id = t2.id_t'''
#         key = '''
# SELECT
#     a,
#     b
# FROM
#     t
# LEFT JOIN
#     t2
#     ON t.id = t2.id_t
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_select_with_function(self):
#         msg = 'Testing SELECT with udf'
#         testQuery = '''SELECT from_unixtime(time), c2 FROM t0'''
#         key = '''
# SELECT
#     from_unixtime(time),
#     c2
# FROM
#     t0
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_select_with_udf(self):
#         msg = 'Testing SELECT with udf'
#         testQuery = '''SELECT foo(c1), c2 FROM t0'''
#         key = '''
# SELECT
#     foo(c1),
#     c2
# FROM
#     t0
#         '''.strip()
#         return self.run(msg, testQuery, key, {'userDefinedFunctions': ['foo']})

#     def test_case_when(self):
#         msg = 'Testing CASE ... WHEN'
#         testQuery = '''SELECT c1, c2, CASE WHEN c3 = 'one' THEN 1 WHEN c3 = 'two' THEN 2 ELSE 3 END AS c4 FROM t0'''
#         key = '''
# SELECT
#     c1,
#     c2,
#     CASE
#         WHEN c3 = 'one'
#         THEN 1
#         WHEN c3 = 'two'
#         THEN 2
#         ELSE 3
#     END AS c4
# FROM
#     t0
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_case_when_with_expression(self):
#         msg = 'Testing CASE ... WHEN with expression'
#         testQuery = '''
# SELECT
# CASE WHEN toString(getNumber()) = 'one' THEN 1
# WHEN toString(getNumber()) = 'two' THEN 2 ELSE 3 END AS c1
# FROM t0
# '''
#         key = '''
# SELECT
#     CASE
#         WHEN toString(getNumber()) = 'one'
#         THEN 1
#         WHEN toString(getNumber()) = 'two'
#         THEN 2
#         ELSE 3
#     END AS c1
# FROM
#     t0
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_lowercase_case_when(self):
#         msg = 'Testing lower-case CASE ... WHEN'
#         testQuery = '''select case when c1 = 'foo' then 1 else 2 end from t0'''
#         key = '''
# SELECT
#     CASE
#         WHEN c1 = 'foo'
#         THEN 1
#         ELSE 2
#     END
# FROM
#     t0
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_ignore_case_when_in_other_string(self):
#         msg = 'Testing ignore CASE, WHEN in other strings'
#         testQuery = '''SELECT CASEDATE, ENDDATE FROM table1'''
#         key = '''
# SELECT
#     CASEDATE,
#     ENDDATE
# FROM
#     table1
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_nested_case_when(self):
#         msg = 'Testing nested CASE ... WHEN'
#         testQuery = '''
# select
#     case when a > 0 then
#         case when b > 0 then True
#         else False
#         end
#     end
#     from t0
#         '''
#         key = '''
# SELECT
#     CASE
#         WHEN a > 0
#         THEN CASE
#             WHEN b > 0
#             THEN TRUE
#             ELSE FALSE
#         END
#     END
# FROM
#     t0
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_operator_spacing(self):
#         msg = 'Testing operator spacing, e.g., -, &, {, }'
#         testQuery = '''
# select
#     *,
#     case when (a>0) and (cast(b as int) & {KEYWORD}=0)
#     then -c
#     else a-c end
#     from t0
#         '''
#         key = '''
# SELECT
#     *,
#     CASE
#         WHEN (a > 0) AND (CAST(b AS int) & {KEYWORD} = 0)
#         THEN -c
#         ELSE a - c
#     END
# FROM
#     t0
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_line_comment(self):
#         msg = 'Testing line comment'
#         testQuery = '''
# SELECT a,--comment, here
# b FROM t0--comment'''
#         key = '''
# SELECT
#     a, --comment, here
#     b
# FROM
#     t0 --comment
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_line_comment_followed_by_comma(self):
#         msg = 'Testing line comment followed by comma'
#         testQuery = '''
# SELECT a --comment
# , b
#         '''
#         key = '''
# SELECT
#     a --comment
# ,
#     b
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_line_comment_followed_by_close_paren(self):
#         msg = 'Testing line comment followed by closing parentheses'
#         testQuery = '''
# SELECT ( a --comment
#  )
#         '''
#         key = '''
# SELECT
#     (
#         a --comment
#     )
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_line_comment_followed_by_open_paren(self):
#         msg = 'Testing line comment followed by opening parentheses'
#         testQuery = '''
# SELECT a --comment
# ()
#         '''
#         key = '''
# SELECT
#     a --comment
#     ()
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_query_with_between_and(self):
#         msg = 'Testing query with BETWEEN ... AND'
#         testQuery = '''
# select c1, c2 from t0
# where c1 between '{date}' and add_months('{date}', 1)
# and c2 < 0
#         '''
#         key = '''
# SELECT
#     c1,
#     c2
# FROM
#     t0
# WHERE
#     c1 BETWEEN '{date}' AND add_months('{date}', 1)
#     AND c2 < 0
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_query_with_left_join_and(self):
#         msg = 'Testing query with LEFT JOIN ... AND'
#         testQuery = '''
# select c1, c2 from t0
# left join t1 on t0.c1 = t1.c1 and t0.c3 = t1.c3
#         '''
#         key = '''
# SELECT
#     c1,
#     c2
# FROM
#     t0
# LEFT JOIN
#     t1
#     ON t0.c1 = t1.c1
#     AND t0.c3 = t1.c3
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_query_with_nested_and_in_where(self):
#         msg = 'Testing query with nested AND in WHERE'
#         testQuery = '''
# SELECT c1, c2 FROM t0 WHERE type = 1 OR (c3 = 0 AND type = 2)
#         '''
#         key = '''
# SELECT
#     c1,
#     c2
# FROM
#     t0
# WHERE
#     type = 1
#     OR (
#         c3 = 0
#         AND type = 2
#     )
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_query_with_long_table_name(self):
#         msg = 'Testing query with long table name'
#         testQuery = '''
# select t0.a, t0.b, t1.x, t2.y,
#     t3.c, t3.d

# from t0_very_very_very_very_very_very_very_very_very_long_table_name t0
#     left join t1_very_very_very_very_very_very_very_very_very_long_table_name t1 on t0.a = t1.z
#     left join t2 on t0.a = t2.z

#     left join t3 on t3.c = t0.a

# where t0.a between '{date}' and add_months('{date}', 1)
# and t2.y < 0
# order by 1,2,3
#         '''
#         key = '''
# SELECT
#     t0.a,
#     t0.b,
#     t1.x,
#     t2.y,
#     t3.c,
#     t3.d
# FROM
#     t0_very_very_very_very_very_very_very_very_very_long_table_name t0
# LEFT JOIN
#     t1_very_very_very_very_very_very_very_very_very_long_table_name t1
#     ON t0.a = t1.z
# LEFT JOIN
#     t2
#     ON t0.a = t2.z
# LEFT JOIN
#     t3
#     ON t3.c = t0.a
# WHERE
#     t0.a BETWEEN '{date}' AND add_months('{date}', 1)
#     AND t2.y < 0
# ORDER BY
#     1,
#     2,
#     3
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_query_with_unicode_char(self):
#         msg = 'Testing query with unicode character'
#         testQuery = '''
# select c1, c2 from t0
# where t1.c2 IN ('你好' 'ไหว้')
#         '''
#         key = '''
# SELECT
#     c1,
#     c2
# FROM
#     t0
# WHERE
#     t1.c2 IN ('你好' 'ไหว้')
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_query_with_string_formatting_with_keyword(self):
#         msg = 'Testing query with mutliple {} for Python string formatting that contain keywords in the query'
#         testQuery = '''
# select * from t0 where t0.id in ({CREATE}, {UPDATE}, {UPDATE}, {UPDATE}, {UPDATE}, {UPDATE}, {UPDATE}, {UPDATE}, {UPDATE}, {UPDATE}, {UPDATE}, {UPDATE}, {UPDATE}) --CREATE or UPDATE
#         '''
#         key = '''
# SELECT
#     *
# FROM
#     t0
# WHERE
#     t0.id IN (
#         {CREATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE},
#         {UPDATE}
#     ) --CREATE or UPDATE
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_query_with_subquery(self):
#         msg = 'Testing query with subquery'
#         testQuery = '''
# with t0 as (select c1, c2 from tab1),

# t1 as (select c1, c2 from tab2),

# t2 as (select c1, c2 from tab3)

# select * from t0 left join t1 on t0.c1 = t1.c1
# left join t2 on t0.c1 = t2.c1
#         '''
#         key = '''
# WITH t0 AS (
#     SELECT
#         c1,
#         c2
#     FROM
#         tab1
# ),

# t1 AS (
#     SELECT
#         c1,
#         c2
#     FROM
#         tab2
# ),

# t2 AS (
#     SELECT
#         c1,
#         c2
#     FROM
#         tab3
# )

# SELECT
#     *
# FROM
#     t0
# LEFT JOIN
#     t1
#     ON t0.c1 = t1.c1
# LEFT JOIN
#     t2
#     ON t0.c1 = t2.c1
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_query_with_nested_subquery(self):
#         msg = 'Testing query with nested subquery'
#         testQuery = '''
# select
#     *,
#     from_unixtime(ctime)
# from
#     (
#         select * from t1
#     )
#         '''
#         key = '''
# SELECT
#     *,
#     from_unixtime(ctime)
# FROM
#     (
#         SELECT
#             *
#         FROM
#             t1
#     )
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_query_with_lateral_view_explode(self):
#         msg = 'Testing query with LATERAL VIEW EXPLODE'
#         testQuery = '''
# select * from
#     t0
#     LATERAL VIEW EXPLODE(t0.groupA.list) t as groupA_list_explode
#         '''
#         key = '''
# SELECT
#     *
# FROM
#     t0
#     LATERAL VIEW EXPLODE(t0.groupA.list) t AS groupA_list_explode
#         '''.strip()
#         return self.run(msg, testQuery, key)

#     def test_reservedKeywordUppercase_config(self):
#         msg = 'Testing reservedKeywordUppercase config'
#         testQuery = '''select c1, c2 from t0'''
#         key = '''
# select
#     c1,
#     c2
# from
#     t0
#         '''.strip()
#         return self.run(msg, testQuery, key, {'reservedKeywordUppercase': False})

#     def test_linesBetweenQueries_config(self):
#         msg = 'Testing linesBetweenQueries config'
#         testQuery = '''
# with t0 as (select c1, c2 from tab1),

# t1 as (select c1, c2 from tab2),

# t2 as (select c1, c2 from tab3)

# select * from t0 left join t1 on t0.c1 = t1.c1
# left join t2 on t0.c1 = t2.c1
#         '''
#         key = '''
# WITH t0 AS (
#     SELECT
#         c1,
#         c2
#     FROM
#         tab1
# ),

# t1 AS (
#     SELECT
#         c1,
#         c2
#     FROM
#         tab2
# ),

# t2 AS (
#     SELECT
#         c1,
#         c2
#     FROM
#         tab3
# )

# SELECT
#     *
# FROM
#     t0
# LEFT JOIN
#     t1
#     ON t0.c1 = t1.c1
# LEFT JOIN
#     t2
#     ON t0.c1 = t2.c1
#         '''.strip()
#         return self.run(msg, testQuery, key, {'linesBetweenQueries': 2})

    def test_(self):
        msg = 'test'
        testQuery = '''
        with payment_audit_tab_edit as (
    select *
    from (select *, ROW_NUMBER() OVER(PARTITION BY payment_id ORDER BY ctime desc, id desc) as txn_desc
            from shopee_payment_module_audit_xx_db__payment_audit_tab
            where date(from_unixtime(case when '{region}' in ('TH','ID','VN') 
                then ctime - 3600 
                else ctime end)) <= date('{date}')
            )
    where txn_desc = 1
    )
    
    SELECT '{region}' as country,
            date(from_unixtime((case when '{region}' in ('TH','ID','VN') 
                    then pay_a.ctime - 3600 
                    else pay_a.ctime end))) as date_id,
            cast(get_json_object(trans.extra_data,'$.target_transaction_id') as bigint) as target_transaction_id,
            cast(get_json_object(trans.extra_data,'$.target_payment_id') as bigint) as target_payment_id,
            coalesce(get_json_object(pc.extra_data, '$.description'), pc.description) AS payment_type,
            from_unixtime(case when '{region}' in ('TH','ID','VN') 
                            then t_pay.mtime - 3600 
                            else t_pay.mtime end) as target_transaction_update_time,
    from 
        (
            select *
            from 
                (
                    select *, ROW_NUMBER() OVER(PARTITION BY payment_id ORDER BY ctime asc) as rank  --requested by LY, need to dedupe and choose the one with min(ctime)
                    from shopee_payment_module_audit_xx_db__payment_audit_tab
                    where  new_status in (20) --spm_constants.PaymentStatus.SUCCESS
                    and old_status not in (20) --spm_constants.PaymentStatus.SUCCESS
                )
            where rank = 1
        ) pay_a 
    left join shopee_payment_module_payment_xx_db__payment_tab t_pay 
        on cast(get_json_object(trans.extra_data,'$.target_transaction_id') as bigint) = t_pay.transaction_id
        and cast(get_json_object(trans.extra_data,'$.target_payment_id') as bigint) = t_pay.payment_id
    left join shopee_payment_module_xx_db__payment_channel_tab t_pay_c
        on t_pay.channel_id = t_pay_c.channel_id
    left join 
        (
            select t_prov.transaction_id, t_prov.entity_id
            from shopee_payment_module_provision_xx_db__provision_tab t_prov 
            join shopee_payment_module_xx_db__provision_channel_tab t_prov_c on t_prov.channel_id = t_prov_c.channel_id and t_prov_c.category not in (9,10,13) --filter away those fake checkouts, it's a bug in spm admin
        ) t_prov  on cast(get_json_object(trans.extra_data,'$.target_transaction_id') as bigint) = t_prov.transaction_id
    left join transaction_audit_tab_edit t_taudit
        on cast(get_json_object(trans.extra_data,'$.target_transaction_id') as bigint) = t_taudit.transaction_id
    left join payment_audit_tab_edit t_pay_a
        on cast(get_json_object(trans.extra_data,'$.target_transaction_id') as bigint) = t_pay_a.transaction_id
        and cast(get_json_object(trans.extra_data,'$.target_payment_id') as bigint) = t_pay_a.payment_id
        
    where prov_c.category = 22 -- AUTO_REFUND
    and date(from_unixtime((case when '{region}' in ('TH','ID','VN') 
            then pay_a.ctime - 3600 
            else pay_a.ctime end))) = date('{date}')
    and t_pay_c.description != 'JKO COD'
        '''
        key = 'key'
        return self.run(msg, testQuery, key)

    def run(self, msg, testQuery, key, config=Config()):
        logger.info(msg)
        logger.info('testQuery =')
        logger.info(testQuery)
        formattedQuery = api.format_query(testQuery, config)
        logger.info('formattedQuery =')
        logger.info(formattedQuery)
        logger.info(repr(formattedQuery))
        logger.info('key =')
        logger.info(key)
        logger.info(repr(key))
        assert formattedQuery == key
        return True

    def run_all(self):
        tests = list(filter(lambda m: m.startswith('test_'), dir(self)))
        for test in tests:
            getattr(self, test)()

if __name__ == "__main__":
    Test().run_all()
