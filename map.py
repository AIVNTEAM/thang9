income = [10, 20, 30]
def doubleincome(money):
	return money * 2

new_incom = list(map(doubleincome, income))
print(income)
print(new_incom)