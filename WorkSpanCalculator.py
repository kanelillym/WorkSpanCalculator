import datetime
import sys

START_DAY = datetime.datetime(2021, 10, 30)
WORK_SPAN_LENGTH = 4
DAYS_OFF_PER_SPAN = 1

def main() -> None:
	# read sys args
	if len(sys.argv) > 1:
		if sys.argv[1] == "-h":
			print("===Work Span Calculator===\nDetermines whether a given day is a work or rest day for a given work rhythm.\n"+\
			"Default values: 4 day cycles with 1 rest day per cycle, starting on 2021-10-30.\nRest days are consecutive at the start of each cycle.\n\nSYNTAX:\n"+\
			"python WorkSpanCalculator.py [cycle length] [rest days] [start date]")
		else:
			startDate = START_DAY
			span = WORK_SPAN_LENGTH
			rest = DAYS_OFF_PER_SPAN
			
			span = int(sys.argv[1])
			if len(sys.argv) > 2:
				rest = int(sys.argv[2])
				if len(sys.argv) > 3:
					startDate = datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d")
			result = isBreakDay(datetime.datetime.now(), startDate, span, rest)
			printResults(result)
	else:
		result = isBreakDay(datetime.datetime.now())
		printResults(result)

def printResults(result: bool) -> None:
	if result:
		print("Today is a break day.")
	else:
		print("Today is a work day.")

def getDaysSinceStart(targetDate: datetime, startDate: datetime = START_DAY) -> int:
	return (targetDate.date() - startDate.date()).days

def isBreakDay(targetDate: datetime, startDate: datetime = START_DAY, spanLength: int = WORK_SPAN_LENGTH, restDayCount: int = DAYS_OFF_PER_SPAN) -> bool:
	return getDaysSinceStart(targetDate, startDate) % spanLength < restDayCount

if __name__ == "__main__":
	main()