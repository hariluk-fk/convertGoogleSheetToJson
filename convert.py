import requests, csv, json, os

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

def CSVToJson(csvFile):
    # Open the CSV
    f = open( csvFile, 'r' )

    reader = csv.DictReader( f, fieldnames = ( "DocTaxNo","TaxDate","TaxRate","TransNo", "CreditTerm", 
            "TaxNo", "CompanyName", "Branch", "Address1", "Address2", "Address3", "DeliveryName", "DeliveryAddress1", "DeliveryAddress2", "DeliveryAddress3",
            "PackingNo", "PackingType", "PackingPackage", "DeliveryNo", "DeliverySeq", "InvoiceNo", "InvoiceSeq", "DeliveryQty", "PurchaseNo", "PurchaseType",
                    "PartNo", "PartType", "PartName", "Retail", "Price", "Discount"
       ))
    framenames = []
    storeHeader = []

    # header frame names in a list
    for row in reader:
        header= {"docTaxNo":row["DocTaxNo"], 
        "taxDate": row["TaxDate"],
        "taxRate": row["TaxRate"],
        "transNo": row["TransNo"],
        "creditTerm": row["CreditTerm"],
        "customer":{
                        "taxNo":            row["TaxNo"],
                        "companyName":      row["CompanyName"],
                        "branch":           row["Branch"],
                        "address1":         row["Address1"],
                        "address2":         row["Address2"],
                        "address3":         row["Address3"],
                        "deliveryName":     row["DeliveryName"],
                        "deliveryAddress1": row["DeliveryAddress1"],
                        "deliveryAddress2": row["DeliveryAddress2"],
                        "deliveryAddress3": row["DeliveryAddress3"]
                        },
        "invoiceDetail":[]}
        if row["DocTaxNo"] not in framenames:
            framenames.append(row["DocTaxNo"])
            storeHeader.append(header)

    # Create Objects for Header, customer, Detial and article
    customer = {"taxNo":""}
    invoiceDetail = {"PackingNo": ""}
    for header in storeHeader:
        f = open( csvFile, 'r' )
        reader = csv.DictReader( f, fieldnames = ("DocTaxNo","TaxDate","TaxRate","TransNo", "CreditTerm", 
            "TaxNo", "CompanyName", "Branch", "Address1", "Address2", "Address3", "DeliveryName", "DeliveryAddress1", "DeliveryAddress2", "DeliveryAddress3",
            "PackingNo", "PackingType", "PackingPackage", "DeliveryNo", "DeliverySeq", "InvoiceNo", "InvoiceSeq", "DeliveryQty", "PurchaseNo", "PurchaseType",
                    "PartNo", "PartType", "PartName", "Retail", "Price", "Discount"))
        for row in reader:
            if header["docTaxNo"] == row["DocTaxNo"]:
                # if header["invoiceDetail"] == row["PackingNo"]:
                    invoiceDetail = {
                        "packingNo":                row["PackingNo"], 
                        "packingType":              row["PackingType"],
                        "packingPackage":           row["PackingPackage"],
                        "deliveryNo":               row["DeliveryNo"],
                        "deliverySeq":              row["DeliverySeq"],
                        "invoiceNo":                row["InvoiceNo"],
                        "invoiceSeq":               row["InvoiceSeq"],
                        "deliveryQty":              row["DeliveryQty"],
                        "purchaseNo":               row["PurchaseNo"],
                        "purchaseType":             row["PurchaseType"],
                        "article":{
                            "partNo":               row["PartNo"],
                            "partType":             row["PartType"],
                            "partName":             row["PartName"],
                            "retail":               row["Retail"],
                            "price":                row["Price"],
                            "discount":             row["Discount"]
                            }
                        }
                    header["invoiceDetail"].append(invoiceDetail)
                     
            
    # Parse the CSV into JSON
    out = json.dumps(header, indent=4)
    # Save the JSON
    if os.path.exists('/Users/hariluk/Desktop/TaxReport/Complete/JSON/invoiceJson.json'):

        os.remove('/Users/hariluk/Desktop/TaxReport/Complete/JSON/invoiceJson.json')
        print('Remove Json file complete !!!!!!!')
    
    f = open( '/Users/hariluk/Desktop/TaxReport/Complete/JSON/invoiceJson.json', 'w')
    f.write(out)

    print('Json file complete !!!!!!!')

googleSheetToCSV()