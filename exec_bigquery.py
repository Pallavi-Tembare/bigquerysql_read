from google.cloud import bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'data/ServiceKey_GoogleCloud.json'


class Exec_Bigquery:
    def __init__(self, data):
        client = bigquery.Client()
        for qry in data:
            print("\nQUERY: {}".format(qry))
            query_job = client.query(qry)
            try:
                results = query_job.result()
                print("Result:")
                for row in results:
                    print("{} : {} ".format(row.FIRST_NAME, row.HIRE_DATE))

            except Exception as e:
                for e in query_job.errors:
                    print('ERROR: {}'.format(e['message']))