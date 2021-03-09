# bte_regression_test

## Usage

### Clone the repo

`
git clone https://github.com/kevinxin90/bte_regression_test & cd bte_regression_test
`

### Install Dependencies

`
pip install -r requirements.txt
`

### Configure server url

Server url can be set at /src/config.py file. It's recommended to run a local copy of BTE TRAPI interface using documentation provided [here](https://github.com/biothings/BioThings_Explorer_TRAPI).

If you use local copy, set SERVER_URL to be "http://localhost:3000". If you want to use the production server, set SERVER_URL to be "https://api.bte.ncats.io" or development server, set SERVER_URL to be "https://dev.api.bte.ncats.io".

### Run queries

`
python3 src/query.py {output_file_path} {query_template}
`

replace {output_file_path} with file path you want to output the results.
replace {query_template} witth file path you store the query template. Example query templates are stored in /src/query_templates folder.