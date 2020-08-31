import requests
import urllib3
from time import sleep
import xml.etree.ElementTree as ET

def getReferenceCode(token,id):

  referenceParams = {'t': token, 'q': id, 'v': '3'}
  referenceEndpoint = 'https://gdcdyn.interactivebrokers.com/Universal/servlet/FlexStatementService.SendRequest'

  try:
    referenceReq = requests.get(referenceEndpoint, params=referenceParams,timeout=5)
  except requests.exceptions.ConnectTimeout as timeoutExc:
    print(timeoutExc)
    return
  except Exception:
    return

  if referenceReq.status_code == 200:
    referenceTree = ET.fromstring(referenceReq.text)
    referenceCode = referenceTree.findtext('ReferenceCode')
    if referenceTree.findtext('Status') != "Success":
        return
    else:
        return referenceCode
  else:
      return

def getQueryResult(token,code):

  flexParams = {'t': token, 'q': code, 'v': '3'}
  flexEndpoint = 'https://gdcdyn.interactivebrokers.com/Universal/servlet/FlexStatementService.GetStatement'

  retry = 4
  xml_status = ""

  try:
    flexReq = requests.get(flexEndpoint, params=flexParams,timeout=5)
  except requests.exceptions.ConnectTimeout as timeoutExc:
    print(timeoutExc)
    return
  except Exception:
      return

  if flexReq.status_code == 200:
    # Check if response has XML format
    try:
      flexTree = ET.fromstring(flexReq.text)
      xml_status = referenceTree.findtext('Status')

      while retry > 0 and xml_status != "Success":
        flexReq = requests.get(flexEndpoint, params=flexParams,timeout=5)
        flexTree = ET.fromstring(flexReq.text)
        xml_status = referenceTree.findtext('Status')
        retry = retry - 1

      if xml_status != "Success":
        print("Got [%s] result from request [%s]: %s after %d retries",flexTree.findtext('Status'),flexTree.findtext('ErrorCode'),flexTree.findtext('ErrorMessage'),retry)
      return

    except:
        pass

    return flexReq.text

  else:
    return
