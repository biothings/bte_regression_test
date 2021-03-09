from config import SERVER_URL, TIMEOUT

import requests
from urllib.parse import urljoin
import csv
import time
import os
import sys
import json

def make_request(gard_id, template):
    template['message']['query_graph']['nodes']['n0']['id'] = "GARD:" + gard_id
    try:
        doc = requests.post(urljoin(SERVER_URL, "/v1/query"), json=template, timeout=TIMEOUT)
        if doc.status_code == 200:
            data = doc.json()
            return data
        else:
            print("Call to gard_id {0} failed with status code: {1}".format(gard_id, doc.status_code))
            print(doc.content)
    except:
        print("Call to gard_id {0} failed.".format(gard_id))

def check_if_response_contain_unii(response, unii):
    for rec in response['message']['knowledge_graph']['nodes'].values():
        if 'UNII:' + unii in rec['attributes'][0]['value']:
            return True
    return False

def query(output_file, template_path):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, 'data/OOPD-22-02-21.csv'), newline='', encoding='utf-8') as csvfile:
        with open(output_file, 'w', newline='') as outputfile:
            with open(template_path) as f:
                template_file = json.load(f)
                fieldnames = ['gard id', 'unii id', 'has hit']
                writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
                writer.writeheader()
                data = csv.reader(csvfile, delimiter=',')
                next(data)
                for row in data:
                    print(row[21])
                    if row[21] and row[22]:
                        api_res = make_request(row[21], template_file)
                    else:
                        api_res = None
                    if api_res:
                        writer.writerow({'gard id': row[21], 'unii id': row[22], 'has hit': check_if_response_contain_unii(api_res, row[22])})
                        time.sleep(1)
                    else:
                        writer.writerow({'gard id': row[21], 'unii id': row[22], 'has hit':  "failed"})



if __name__ == "__main__":
    print(sys.argv[1], sys.argv[2]   )
    query(sys.argv[1], sys.argv[2])