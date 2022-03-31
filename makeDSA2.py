import tabula
import re



# PDFファイル
pdf_file = "10_DataIQ-DSA-2022-002_rev01" 

try:
    found = re.search('-(.+?)_', pdf_file).group(1)
    #print(found)
except AttributeError:
    pass

try:
    found2 = re.search('10_(.+?)_', pdf_file).group(1)
    #print(found)
except AttributeError:
    pass

# テキストテーブル取得
dummy = tabula.read_pdf(pdf_file+".pdf", lattice=True, pages='all')

y=dummy[3]

z=y[y['CVEs Addressed'].str.contains('CVE-',na=False)]

x=z['CVEs Addressed']

x.reset_index(drop=True, inplace=True)


#print(x)


for i in range(len(x.index)):
    a=x[i]
    #print(a)

with open('test.txt', mode='w') as f:
    f.write("以下の脆弱性についてDellEMC社からDSAが発表されております。 DSAとは、製品のセキュリティ上の脆弱性に対してDellEMC社から発表される情報となります。\n"+
    "\n"+
    "-DSA番号：\n"+
    found+"\n"+
    "\n"+
    "-該当共通脆弱性識別子：\n")

for i in range(len(x.index)):
    with open('test.txt', mode='a') as f:
        f.write(x[i]+"\n")

with open('test.txt', mode='a') as f:
    f.write("\n"+
    "-詳細情報\n"+
    "詳細につきましては、メーカー資料を[TIPS]からダウンロードし、ご参照ください。\n"+
    "\n"+
    "[TIPS(Techmatrix Information Protal Site)]\n"+
    "https://nws.techmatrix.co.jp/tips/\n"+
    "フォルダ：製品資料 > 10_脆弱性情報 > ファイル名：10_"+found2+"_revXX.pdf\n"+
    "\n"+
    "※ファイル名の末尾XXにリビジョン番号が入ります。ファイルの更新がある場合は、リビジョン番号も更新されます。\n")

