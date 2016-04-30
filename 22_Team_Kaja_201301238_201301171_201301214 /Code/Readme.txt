Step1:
	First we have to extract data from twitter
	Code : Code_to_get_data.py
	To Run:
		python Code_to_get_data.py > tofind.txt

Step2:
	Finding Stop words from training Twitter Data
	Code: for_finding_stopwords.py
	To Run:
		python for_finding_stopwords.py < inputfile(containg training twitterdata)	
		Input : twitter_data_file for trainings purpose
		Output: data with all stoppng words

Step3:
	Analyze Data to find trending Topic
	Code : Analysing_Data.py
	To Run:
		python Analysing_Data.py < inputfile(containg twitterdata)
		Input : twitter_data_file obtained in first step
		Output: Tweet data with all stop words are removed and words are stemmed

Step4:
	Finding trending Topic
	Code : final.py
	To Run:
		python final.py < inputfile(file obtained from above step3)
		Input: file obtained from above step3
		Output: result_output which containes  time wise trending topics with all other details
