import gspread, datetime
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("copy_of_plany_dyzurowe")

now = datetime.datetime.now()
polishMonths = ["", "STYCZEN", "LUTY", "MARZEC", "KWIECIEN", "CZERWIEC", "LIPIEC", "SIERPIEN", "WRZESIEN", "PAZDZIERNIK", "LISTOPAD", "GRUDZIEN"]
sheetName = "%s %s" %(polishMonths[now.month], now.year)
worksheet = sheet.worksheet(sheetName)

startCell = worksheet.find("PLAN")
print("Found something at R%sC%s" % (startCell.row, startCell.col))
startRow = startCell.row + 5
startCol = startCell.col + 1
shifts = [None] * 32
for j in range(3):
	for i in range(32):
		if j == 0 and worksheet.cell(startRow + i, startCol + j).value == "AR":
			shifts[i+1] = 1
			print(str(i + 1) + ": \t 1")
		if j == 1 and worksheet.cell(startRow + i, startCol + j).value == "AR":
			shifts[i+1] = 2
			print(str(i + 1) + ": \t 2")
		if j == 2 and worksheet.cell(startRow + i, startCol + j).value == "AR":
			shifts[i+1] = 3
			print(str(i + 1) + ": \t 3")	



print(shifts)

val = worksheet.cell(startRow, startCol).value
print(val)
