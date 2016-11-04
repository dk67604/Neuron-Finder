import glob
import sys

input_files = sorted(glob.glob(sys.argv[1]))

def main():
	
	with file("final_output.json", "w") as outputFile:
	        firstFile = True
	        for inputFileName in input_files:
	            with file(inputFileName) as inputFile:
	                if firstFile:
	                    outputFile.write('[')
	                    firstFile = False
	                else:
	                    outputFile.write(',')
	                outputFile.write(inputFile.read())
	        outputFile.write(']')

if __name__ == '__main__':
	main()
