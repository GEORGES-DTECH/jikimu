import requests
from datetime import datetime
import base64
from requests.auth import HTTPBasicAuth


#=========================MPESA INTEGRATION==================================
#====================PARAMETERS=====================
business_short_code = "174379"
c2b_short_code = "600426"
consumer_key = "uGG7CxH42KeQPBaAcQAUOihH09lhjWog"
consumer_secret = "mY5AXoObwRmsyX77"
phone_number = "254727574812"
pass_key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

#==================FORMATING TIME================
unformatted_time = datetime.now()
formated_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#===================ENCODING PASSWORD===============
data_to_encode = business_short_code + pass_key + formated_time
encoded_string = base64.b64encode(data_to_encode.encode())
decoded_password = encoded_string.decode('utf-8')

#===================GENERATING ACCESS TOKEN===================

api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
result = requests.get(api_url,auth=HTTPBasicAuth(consumer_key,consumer_secret))
json_response = result.json()
my_access_token = json_response["access_token"]



# lipa_na_mpesa()  

def register_url():
    
    api_url= 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
    headers ={"Authorization":"Bearer %s"% my_access_token }
    
    request={
            "ShortCode": 600426,
            "ResponseType": "Completed",
            "ConfirmationURL": "https://www.providaafrica.com/payments/confirmation/",
            "ValidationURL": "https://www.providaafrica.com/payments/validation/"
        
        }
    
    try:
       response = requests.post(api_url,json=request,headers=headers)
    except:
       response = requests.post(api_url,json=request,headers=headers,verify=False)


    print(response.text)  
      
# register_url()        


def c2b_payment():
   
    api_url= "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers ={"Authorization":"Bearer %s"%  my_access_token }
    
    request={
            "ShortCode": c2b_short_code,
            "CommandID":"CustomerPayBillOnline",
             "Amount":"5000",
            "Msisdn": "254708374149",
            "BillRefNumber": "29388001",
        }

    
    try:
       response = requests.post(api_url,json=request,headers=headers)
    except:
       response = requests.post(api_url,json=request,headers=headers,verify=False)
 
   

    print(response.text)    
c2b_payment()    