from cashRegister import CashRegister

cash = CashRegister()

print( cash.getTotal())
print( cash.getCount())

cash.addItem(99)

print( cash.getTotal())
print( cash.getCount())

print( "your change is = ", cash.giveChange(120))

cash.clear()

print(" cash class variable values after clearing: ")
print( cash.getTotal())
print( cash.getCount())
