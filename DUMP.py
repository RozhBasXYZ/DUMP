import requests as ses
import re,os,sys,time,bs4
from bs4 import BeautifulSoup as parser

##-----FITUR GLOBAL---###
id,namafile = [],[]
try:pm = open(".pemisah.txt","r").read()
except:pm = "|"

##-----WARNA PRINT----##
J = '\x1b[38;5;208m'
P = '\033[m'
K = '\033[93m'

##-----FITUR AUTO PRINT---##
def simpan():
	print("\n")
	file = namafile[0]
	print("\rtotal akun sebanyak  : %s\npemisah file memakai : %s\nfile tersimpan di    : %s.json"%(len(id),pm,file))
	exit()


##----FITUR CLEAR / REST SYS ----##
def bersih():
	os.system("clear")


##----FITUR LOGIN----###
def login():
	print(f"""        ___                        
       / _ \__ ____ _  ___    
      / // / // /  ' \/ _ \      ┌──────────────────────────────┐
     /____/\_,_/_/_/_/ .__/      │  {J}Script By RochmatBasukiXD {P}  │       
            ___ _/ //_/_ _____   │    {J}Github.com/RozhBasXYZ   {P}  │
           / _ `/  '_/ // / _ \  └──────────────────────────────┘
           \_,_/_/\_/\\_,_/_//_/\n\n\n""")
	print("\033[93m•\033[91m•\033[92m•\33[m anda harus login terlebih dahulu \033[92m•\033[91m•\033[93m•\33[m\n")
	cookie = input(f"cookie : ")
	try:
		babas = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
		data = ses.get("https://business.facebook.com/business_locations",headers=babas,cookies={"cookie":cookie})
		token = re.search('(EAAG\w+)',str(data.text)).group(1)
		open(".token.txt", "w").write(token)
		open(".cookie.txt", "w").write(cookie)
		menu()
	except Exception as e:
		try:
			os.remove(".token.txt")
			os.remove(".cookie.txt")
		except:pass
		exit("cookie invalid")
		
		

##----MENU UTAMA---##
def menu():
	bersih()
	try:t = open(".token.txt", "r").read();c = {"cookie":open(".cookie.txt","r").read()};nama = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={t}",cookies=c).json()["name"]
	except:print("cookie invalid");time.sleep(2);os.system('clear');login()	
	print(f"""        ___                        
       / _ \__ ____ _  ___    
      / // / // /  ' \/ _ \      ┌──────────────────────────────┐
     /____/\_,_/_/_/_/ .__/      │  {J}Script By RochmatBasukiXD {P}  │       
            ___ _/ //_/_ _____   │    {J}Github.com/RozhBasXYZ   {P}  │
           / _ `/  '_/ // / _ \  └──────────────────────────────┘
           \_,_/_/\_/\\_,_/_//_/    selamat datang{K} {nama} {P}""")
	print(f"\n\n\n1. dump publik\n2. dump masal\n3. dump followers\n4. dump group publik\n5. setting pemisah file")
	bas = input("menu : ")
	if bas in ["1"]:
		publik(t,c)
	elif bas in ["2"]:
		masal(t,c)
	elif bas in ["3"]:
		follow(t,c)
	elif bas in ["4"]:
		group(t,c)
	elif bas in ["5"]:
		print("\ncontoh pemisah file yang umum di pakai\ncontoh = | / • / = / <=> / <> / + ")
		pms = input("pemisah baru : ")
		open(".pemisah.txt","w").write(pms)
		exit("pemisah baru berhasil di setting")
	else:
		exit("isi yang benar")
	 


##----DUMP PUBLIK----##
def publik(t,c):
	pil = input("id akun : ")
	nam = input("nama file : ")
	file = (nam+".json")
	xx = open(file,"w")
	namafile.append(nam)
	try:
		bas = ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()
		for pi in bas['friends']['data']:
			try:
				id.append(pi['id']+pm+pi['name'])
				xx.write(pi["id"]+pm+pi["name"]+"\n")
				print('\rsedang dump %s id'%(len(id)),end=" ")
				sys.stdout.flush()
			except:continue
		simpan()
	except (KeyError,IOError):
		exit("akun tidak publik")



##----DUMP MASAL----##
def masal(t,c):
    try:
        bz=0
        apa = int(input(f'jumblah target : '))
        nam = input("nama file : ")
        file = (nam+".json")
        xx = open(file,"w")
        namafile.append(nam)
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	pil = input(f'\rmasukan id akun ke {bz} : ')
    	try:
    		bas = ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()
    		for pi in bas['friends']['data']:
    		      id.append(pi['id']+pm+pi['name'])
    		      xx.write(pi["id"]+pm+pi["name"]+"\n")
    		      print('\rsedang dump %s id'%(len(id)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except KeyError:
    	      print(f'gagal dump akun mungkin tidak publik')
    	      continue		                       		
    simpan()
          
              

##----DUMP FOLLOWERS----##
def follow(t,c):
	pil = input("id akun : ")
	nam = input("nama file : ")
	file = (nam+".json")
	xx = open(file,"w")
	namafile.append(nam)	
	try:
		for pi in ses.get(f"https://graph.facebook.com/{pil}?fields=name,subscribers.fields(id,name).limit(5000)&access_token={t}",cookies=c).json()["subscribers"]["data"]:
			id.append(pi['id']+pm+pi['name'])
			xx.write(pi["id"]+pm+pi["name"]+"\n")
			print('\rsedang dump %s id'%(len(id)),end=" ")
			sys.stdout.flush()
			time.sleep(0.0002)
	except KeyError:
		exit("gagal dump akun mungkin tidak publik")
	simpan()
          


##----DUMP GROUP----##          
def group(t,c):
	print("pastikan id adalah group publik")
	idt = input("id group : ")
	nam = input("nama file : ")
	file = (nam+".json")
	xx = open(file,"w")
	namafile.append(nam)
	url = "https://mbasic.facebook.com/groups/"+idt
	data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
	try:nama = re.findall('<head><title>(.*?)</title>',str(data))[0]
	except:nama = ''
	print(f"{nama}")
	get_datagrup(nam,url)
	simgrub(nam)
	simpan()
def get_datagrup(nam,url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
		for cari in data.find_all('table'):
			liatnih = cari.text
			spl = liatnih.split(' ')
			if 'mengajukan' in spl:
				idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
				idyou =	idsiapa[0].replace('content_owner_id_new.','')
				namayou = liatnih.replace(' mengajukan pertanyaan .','')
				idku = idyou+pm+namayou
				if idku in id:continue
				else:
					id.append(idku)
					print('\rsedang dump %s id, ctrl+c untuk stop'%(len(id)),end=" ")
					sys.stdout.flush()
			elif '>' in spl:
				idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
				idyou =	idsiapa[0].replace('content_owner_id_new.','')
				namayou = liatnih.split(' > ')[0]
				idku = idyou+pm+namayou
				open(nam+".json","w").write(idku+"\n")
				if idku in id:
					continue
				else:
					id.append(idku)
					print('\rsedang dump %s id, ctrl+c untuk stop'%(len(id)),end=" ")
					sys.stdout.flush()
			else:
				continue
		for g in data.find_all('a'):
			css = str(g).split('>')
			if 'Lihat Postingan Lainnya</span' in css:
				bcj = str(g).replace('<a href="','').replace('amp;','')
				bcj2 = bcj.split(' ')[0].replace('"><img','')
				get_datagrup(nam,'https://mbasic.facebook.com'+bcj2)
	except KeyboardInterrupt:
		simgrub(nam)
		simpan()
	except Exception as e:
		simgrub(nam)
		simpan()



##----CONVERT APPEND TO FILE----###
def simgrub(nam):
	for x in id:
		akun,nama = x.split(pm)
		open(nam+".json",'a+').write('%s%s%s\n'%(akun,pm,nama))
                                
				
def main():
	try:os.system('git pull')
	except:pass
	try:os.system('clear')
	except:pass
	menu()								
if __name__=="__main__":
		main()		
		
		
		

		
		
