import requests, os

def googleSheetToCSV():
    response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSJOjQcVmvnLJj13_fi0J6uJibHkJIu0mbhxioQPWBx6IPk0aBc1KJImR1xCQBVhAtrFP5L6a1s0zFy/pub?output=csv')
    assert response.status_code == 200, 'Wrong status code'

    f = open('/Users/hariluk/Desktop/TaxReport/Template/JSON/csvTmp.csv', 'r')

    if os.path.exists('/Users/hariluk/Desktop/TaxReport/Template/JSON/invoiceCSVTmp.csv'):
    
        os.remove('/Users/hariluk/Desktop/TaxReport/Template/JSON/invoiceCSVTmp.csv')
        print('Remove CSV file complete !!!!!!!')

    f = open( '/Users/hariluk/Desktop/TaxReport/Template/JSON/invoiceCSVTmp.csv', 'w')

    out = response.text
    f.write(out)

    if os.path.exists('/Users/hariluk/Desktop/TaxReport/Template/JSON/invoiceCSVTmp1.csv'):
        print('CSV file template complete, going to Json !!!!!')
        CSVToJson('/Users/hariluk/Desktop/TaxReport/Template/JSON/invoiceCSVTmp1.csv')
    else:
        print('CSV file template invalid!')

googleSheetToCSV()