from urllib import request

Msoft_url='http://real-chart.finance.yahoo.com/table.csv?s=MSFT&d=8&e=15&f=2015&g=d&a=2&b=13&c=1986&ignore=.csv'

def downloadFile(link):
	response=request.urlopen(link)
	File=response.read()
	File_str=str(File)
	lines=File_str.split("\\n")
	save_url=r'Microsoft.csv'
	fx=open(save_url,"w")
	for a in lines:
		fx.write(a +"\n")
	fx.close()

downloadFile(Msoft_url)
