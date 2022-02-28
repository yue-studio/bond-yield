!pip install xmltodict

import xmltodict

url ='https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData'
page = requests.get(url=url)
doc = ' '

try:
  doc = xmltodict.parse(page.content)
except:
  doc['feed']['entry'] = ' '  

data = []
cols = ['Date', '1 year', '10years', '20 years','30 years']

#
# Sometimes their format gets messed up, this is a simple way to work around that
# 
for entry in doc['feed']['entry']:
  date = (entry['content']['m:properties']['d:NEW_DATE']['#text'].split("T"))[0]
  try:
    OneYr = (entry['content']['m:properties']['d:BC_1YEAR']['#text'])
  except:
     OneYr = 0
  try:
    TenYr = entry['content']['m:properties']['d:BC_10YEAR']['#text']
  except:
     TenYr = 0
  try:
     TwentyYr = entry['content']['m:properties']['d:BC_20YEAR']['#text']
  except:
     TwentyYr = 1
  try:
     ThirtyYr = entry['content']['m:properties']['d:BC_30YEAR']['#text']
  except:
     ThirtyYr = 1
 
  data.append([date, OneYr, TenYr, TwentyYr, ThirtyYr])

Bonddf = pd.DataFrame(data)  # Write in DF
Bonddf.columns = cols  # Update column names
print(Bonddf.tail(3))
