import glob

input_files = glob.glob("/home/shubhi/Downloads/*.json")


# def slice(s):
#     return s.strip()[1:-1]


def main():
	
	with file("finalOutput.json", "w") as outputFile:
	        firstFile = True
	        for inputFileName in reversed(input_files):
	            with file(inputFileName) as inputFile:
	                if firstFile:
	                    outputFile.write('[')
	                    firstFile = False
	                else:
	                    outputFile.write(',')
	                #outfile.write(slice(infile.read()))
	                outputFile.write(inputFile.read())
	        outputFile.write(']')


if __name__ == '__main__':
	main()