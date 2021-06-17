
import os,sys,time,hashlib
file_list=[]
root_dir="root\\"
print("Starting Scanning. . .")
for subdir,dirs,files in os.walk(root_dir):
	for file in files:
		file_path=subdir + os.sep + file
		
		if(file_path.endswith(".exe") or file_path.endswith(".dll") or file_path.endswith(".com")):
			file_list.append(file_path)
			


def scan():
	infected_list=[]
	for f in file_list:
		virus_def=open("viruses.txt","r").read()
		file_not_read=False
		print("\nScaning... : {}".format(f))
		hasher=hashlib.md5()
		try:
			with open(f,"rb") as file:
				try:
					buf=file.read()
					file_not_read=True
					hasher.update(buf)
					file_hashed=hasher.hexdigest()
					for line in virus_def:
						if file_hashed == line:
							print("Malware Detected --> file name: {}".format(f))
							infected_list.append(f)
					print(f"file md5 Done: {file_hashed}")
				except Exception as e:
					print("Malware Detected --> file name: {}".format(f))
					infected_list.append(f)
		except:
			print("jyghgfbaduiobuhngvuyijg hnuicmxhn")
	print("Infected files found : {}".format(infected_list))
	deleteOrnot=str(input("Would you like to delete the infected files y=yes n=no (y/n)"))
	if deleteOrnot.upper()=="Y":
		for infected in infected_list:
			os.remove(infected)
			print("File removed : {}".format(infected))
	else:
		os.system("PAUSE")
				
					
scan()		
