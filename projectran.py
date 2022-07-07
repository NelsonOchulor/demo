from enum import unique
import random

for x in range(1):
    payment_tax_id = str(random.randint(400000, 500000))

for x in range(1):
    randBits = bool(random.getrandbits(1))

payment_txn_success = randBits

if randBits == True:
    payment_txn_success = "Successful"
    failure_reason = ' '
    print(',' + payment_tax_id + ',' +
          payment_txn_success + failure_reason)

else:
    payment_txn_success = "Failed"
    failure_reason = "CVV Error"
    print(',' + payment_tax_id + ',' +
          payment_txn_success + ',' + failure_reason)
