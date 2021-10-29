import DateTime

def main():
	# Calculate four day spans from 2021-10-30 (the first break day)
	print(isBreakDay(0))
	print(isBreakDay(1))
	print(isBreakDay(2))
	print(isBreakDay(3))
	print(isBreakDay(4))
	
def getDaysCount():
	pass
	
def isBreakDay(dayNumber):
	return dayNumber % 4 == 0
	
if __name__ == "__main__":
	main()
