from the_bank import Account, Bank

def banking_2():
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))
    # William's account is corrupted because there is an even number of attributes
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    ))
    # The first transfer fails because William's account is corrupted
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
        bank.fix_account('William John')
        bank.fix_account('Smith Jane')
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
    else:
        print('Success')
