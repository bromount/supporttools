with open('shzr_xheaders.html', 'r') as file_open:
	content=file_open.readlines()
	
	#print content
	for line in content:
		if "name=\"DC.Coverage\"" in line:
			coverage=line.split("content")[1].strip("=").strip('"').strip('>').split("\"")[0]
			#print line.strip('"/>')
			print coverage

		if "name=\"keywords\"" in line:
			keywd=line.split("content")[1].strip("=").strip('"').split("\"")[0]
			print keywd

                if "name=\"prodname\"" in line:
                        prodname=line.split("content")[1].strip("=").strip('"').split("\"")[0]
                        print prodname

                if "name=\"version\"" in line:
#			print line
                        version=line.split("content")[1].strip("=").strip('"').split("\"")[0]
                        print version

			

