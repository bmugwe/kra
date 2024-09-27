
import requests
import time
import pandas as pd


url = "https://etims.kra.go.ke/main/signup/getItaxData"
custome_headers = ['ebmTyCd', 'modrId', 'modrNm', 'modDt', 'tin', 'taxpr_nm', 'in_itax', 'taxpr_stts_cd', 'taxpr_ty_cd', 'bsns_actv', 'prvnc_no', 'dstrt_no', 'sctr_no', 'loc_desc', 'tel_no', 'email', 'sync_dt', 'vat_ty_cd', 'nid', 'taxpr_no', 'bsns_yn', 'remarks', 'regr_id', 'regr_nm', 'reg_dt', 'tso_id', 'ismri']




read_data = pd.read_csv('input/kra.csv', )

read_data


def getKRA(tinID):
    payload = f"tin={tinID}"
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,en-GB;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie': 'BIGipServer~k8sprd~ingress_etims-prod_etims-portal=2449595402.36895.0000; JSESSIONID=49F1B18CE4190E06E2F45BA0C7B053A5',
    'DNT': '1',
    'Origin': 'https://etims.kra.go.ke',
    'Referer': 'https://etims.kra.go.ke/main/signup/indexTinUser',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
    except Exception as e:
        print(f"Error fetching KRA : {e}")

def createArray(face):
    pd_base = []
    pd_headers = []
    if(face.get("base",'')):
        base = face['base']
        for i in base:
            pd_base.append(base[i])
            pd_headers.append(i)
    
            
    print(pd_headers)
    return pd_base

All_data = []



for pin in read_data['PIN_NUMBER']:
    print(pin)
    face = getKRA(pin)
    array_data = createArray(face)
    All_data.append(array_data)   
    
    # break
pd.DataFrame(All_data).to_csv("kra/output/kra.csv", header=custom_headers)


