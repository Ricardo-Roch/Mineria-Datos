import requests  # hace solicitudes HTTP
from bs4 import BeautifulSoup  # analiza el contenido HTML
import re  # pa trabaja con expresiones regulares
import urllib.request  # descargar la cosa
url = "https://datos.cdmx.gob.mx/tl/dataset/nacimientos-registrados-en-la-ciudad-de-mexico"


#        |Analiza la cosa|PeticionGet|                                  |Busca que termine en .csv|                |Obtiene el link wiiii
csv_link = BeautifulSoup(requests.get(url).text, 'html.parser').find('a', href=re.compile(r'\.csv$')).get('href')

#         Se descarga y ya
urllib.request.urlretrieve(csv_link, "Nacimientos2020-2023.csv")

#Ricardo Rocha Mo
#2076182
