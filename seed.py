import json, sys
from psycopg2 import connect, Error
from psycopg2.extras import Json
from psycopg2.extras import json as psycop_json

if len(sys.argv) > 1:
    table_name = '_'.join(sys.argv[1:])
else:
    # ..otherwise revert to a default table name
    table_name = "fishing_backend_fish"

# print ("\ntable name for JSON data:", table_name)



with open('data.json') as json_data:
    record_list = json.load(json_data)

# print ("\nrecords:", record_list)
# print ("\nJSON records object type:", type(record_list))

sql_string = 'INSERT INTO {} '.format( table_name )

if type(record_list) == list:
    first_record = record_list[0]
    columns = list(first_record.keys())
    # print ("\ncolumn names:", columns)
else:
    print ("Needs to be an array of JSON objects")
    sys.exit()

sql_string += "(" + ', '.join(columns) + ")\nVALUES "

# table_name = "fish"

for i, record_dict in enumerate(record_list):
    values = []
    for col_names, val in record_dict.items():
        if type(val) == str:
            val = val.replace("'", "''")
            val = "'" + val + "'"

        values += [ str(val) ]
    sql_string += "(" + ', '.join(values) + "),\n"




sql_string = sql_string[:-2] + ";"

# print ("\nSQL string:")
# print (sql_string)


# table_name = "fish"
# sql_string = "INSERT INTO %s (%s)\nVALUES %s" % (
#     table_name,
#     ', '.join(columns),
#     sql_string
# )


try:
    # declare a new PostgreSQL connection object
    conn = connect(
        dbname = "fish",
        user = "fishuser",
        host = "localhost",
        password = "fish",
        # attempt to connect for 3 seconds then raise exception
        connect_timeout = 3
    )

    cur = conn.cursor()
    print ("\ncreated cursor object:", cur)

except (Exception, Error) as err:
    print ("\npsycopg2 connect error:", err)
    conn = None
    cur = None

# # print(sql_string)

if cur != None:

    try:
        cur.execute( sql_string )
        conn.commit()

        print ('\nfinished INSERT INTO execution')

    except (Exception, Error) as error:
        print("\nexecute_sql() error:", error)
        conn.rollback()

    # close the cursor and connection
    cur.close()
    conn.close()
