import mysql.connector
from mysql.connector import Error
import random
import string

class DataGenerator:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost', database='ebanking', user='root')
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
        except Error as e:
            print("Error while connecting to MySQL", e)

        self.female_names = ['تارا','باران','یاسمن','بیتا','سمانه' ,'سارا','سحر', 'شادی','زویا','فاطمه','نازنین','نیلوفر','لیلی','سروین','پارمیدا','مریم','دریا','سمیرا','ترانه','کیمیا','کیانا','دیبا','کتایون','لاله','آریانا']
        self.male_names = ['کوروش','هیربد','باربد','داراب','دانیال' ,'پارسا','شهرام', 'شهریار','محمدجواد','رامین','هادی','آرمین','امیرپاشا','سورنا','محمود','علی','بردیا','کامران','آرش','امید','پدرام','فرهاد','حمیدرضا','امیر',]
        self.family_names = ['صبا', 'علوی','رضوی','تهرانی','طالبی','طیبی','موتمن','کامرانی','ستوده','میرعباسی','هروی','نعمتی','نعیمی','کاووسی','میر','بابایی نژاد','خالو','فرزان','مرعشی','عقیلی','ادیبی','مهرانفر','کرابی','تبریزی','کرمانی','فرزانه پور','فدایی','اربابی','آریایی','ملایری','فولادی',]
        self.cities = ['تهران','کیش','مشهد','قشم','تبریز' ,'مشهد','ساری', 'سمنان','اردبیل','ارومیه','اصفهان','یزد','شیراز','همدان','هرمزگان','ایلام','اراک','شوش','ملایر','خوانسار','کاشان','قم','بوشهر','بیرجند','بجنورد','خرم آباد','کرمانشاه','کرمان','قزوین']
        self.branch_names = ['کامرانیه','ظفر','ولیعصر','پاسداران','زعفرانیه','سعادت آباد','کیش','مشهد','قشم','تبریز' ,'مشهد','ساری', 'سمنان','اردبیل','ارومیه','اصفهان','یزد','شیراز','همدان','هرمزگان','ایلام','اراک','شوش','ملایر','خوانسار','کاشان','قم','بوشهر','بیرجند','بجنورد','خرم آباد','کرمانشاه','کرمان','قزوین']

    def create_tables(self):
        tables = ["LoanTypes", "AccountTypes", "Guarantors", "Branches", "Admins", "Customers", "BankTellers","BranchManagers","Accounts","Cards","Loans","InternetBanks","Transactions","AccountOwnerships"]

        for table in tables:
            f = open(table+".sql", 'r')

            print(f.name)
            self.cursor.execute(f.read())

    def populate_loan_and_account_types(self):
        account_types = [
            ("قرض الحسنه جاری",0,True,False,True) ,
            ("قرض الحسنه پس‌انداز",0,True,False,False),
            ("سپرده بلند مدت",18,False, True,False),
            ("سپرده کوتاه مدت",10, True, False, True)]

        loan_types = [
            ('مسکن',18,7500000000,60,40),
            ('ازدواج',4,1000000000,120,120),
            ('تعمیر',18,2000000000,60,60),
            ('خودرو',18,1000000000,36,36)]

        insert_account_types_query = """
        INSERT INTO AccountTypes
        (name,interest, can_withdraw, can_borrow_loan, can_get_card)
        VALUES ( %s, %s, %s, %s, %s)
        """
        insert_loan_types_query = """
                INSERT INTO LoanTypes
                (name,interest, amount, period, number_of_payments)
                VALUES (%s, %s, %s, %s, %s)
                """
        self.cursor.executemany(insert_account_types_query, account_types)
        self.cursor.executemany(insert_loan_types_query, loan_types)
        self.connection.commit()

    def populate_people(self):
        insert_customers = """
               INSERT INTO Customers
               (first_name,last_name, father_name, date_of_birth, place_of_birth, phone_number, national_code, identification_number, address, postal_code)
               VALUES ( %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s)
               """
        insert_tellers = """
                      INSERT INTO BankTellers
                      (first_name,last_name, father_name, date_of_birth, place_of_birth, phone_number, national_code, identification_number, address, postal_code, salary, branch)
                      VALUES ( %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s)
                      """
        insert_managers = """
                              INSERT INTO BranchManagers
                              (first_name,last_name, father_name, date_of_birth, place_of_birth, phone_number, national_code, identification_number, address, postal_code, salary, branch)
                              VALUES ( %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s)
                              """
        insert_admins = """
                              INSERT INTO Admins
                              (first_name,last_name, father_name, date_of_birth, place_of_birth, phone_number, national_code, identification_number, address, postal_code, salary, rating)
                              VALUES ( %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s)
                              """
        insert_guarantors = """
                                      INSERT INTO Guarantors
                                      (first_name,last_name, national_code, payslip_code)
                                      VALUES ( %s, %s, %s, %s)
                                      """
        customers = []
        tellers = []
        managers = []
        admins = []
        guarantors = []
        teller_salary = [50000000, 60000000, 65000000]
        managers_salary = [100000000, 150000000, 200000000, 250000000]
        admins_salary = [20000000, 30000000, 40000000]
        counter = 0
        branch_nums = random.sample(range(1,111), 110)
        while counter < 110:
            mf = random.randint(0,1)
            if mf == 1:
                names = self.female_names
            else:
                names = self.male_names

            managers.append((random.choice(names), random.choice(self.family_names), random.choice(self.male_names),
                            str(random.randint(1310, 1401)) + '-' + str(random.randint(1, 12)) + '-' + str(
                                random.randint(1, 28)), random.choice(self.cities),
                            str(random.randint(12345678911, 99999999999)),
                            str(random.randint(1000000000, 9999999999)),
                            str(random.randint(1, 9999999999)),
                            random.choice(self.cities) + "، خیابان " + random.choice(self.cities) + "، پلاک " + str(
                                random.randint(1, 150)) + "، طبقه" + str(random.randint(1, 20)) + "، واحد" + str(
                                random.randint(1, 4)), str(random.randint(1000000000, 9999999999)),
                            random.choice(managers_salary), branch_nums[counter]))

            admins.append((random.choice(names), random.choice(self.family_names), random.choice(self.male_names),
                             str(random.randint(1310, 1401)) + '-' + str(random.randint(1, 12)) + '-' + str(
                                 random.randint(1, 28)), random.choice(self.cities),
                             str(random.randint(12345678911, 99999999999)),
                             str(random.randint(1000000000, 9999999999)),
                             str(random.randint(1, 9999999999)),
                             random.choice(self.cities) + "، خیابان " + random.choice(self.cities) + "، پلاک " + str(
                                 random.randint(1, 150)) + "، طبقه" + str(random.randint(1, 20)) + "، واحد" + str(
                                 random.randint(1, 4)), str(random.randint(1000000000, 9999999999)),
                             random.choice(admins_salary), round(random.random()*5,2)))

            guarantors.append((random.choice(names), random.choice(self.family_names),
                           str(random.randint(1000000000, 9999999999)),
                               str(random.randint(1000, 9999999999))
                           ))
            counter += 1

        counter = 0
        while counter < 250:
            mf = random.randint(0, 1)
            if mf == 1:
                names = self.female_names
            else:
                names = self.male_names
            customers.append((random.choice(names), random.choice(self.family_names), random.choice(self.male_names),
                              str(random.randint(1310, 1401)) + '-' + str(random.randint(1, 12)) + '-' + str(
                                  random.randint(1, 28)), random.choice(self.cities),
                              str(random.randint(12345678911, 99999999999)),
                              str(random.randint(1000000000, 9999999999)),
                              str(random.randint(1, 9999999999)),
                              random.choice(self.cities) + "، خیابان " + random.choice(self.cities) + "، پلاک " + str(
                                  random.randint(1, 150)) + "، طبقه" + str(random.randint(1, 20)) + "، واحد" + str(
                                  random.randint(1, 4)), str(random.randint(1000000000, 9999999999))))

            tellers.append((random.choice(names), random.choice(self.family_names), random.choice(self.male_names),
                            str(random.randint(1310, 1401)) + '-' + str(random.randint(1, 12)) + '-' + str(
                                random.randint(1, 28)), random.choice(self.cities),
                            str(random.randint(12345678911, 99999999999)),
                            str(random.randint(1000000000, 9999999999)),
                            str(random.randint(1, 9999999999)),
                            random.choice(self.cities) + "، خیابان " + random.choice(self.cities) + "، پلاک " + str(
                                random.randint(1, 150)) + "، طبقه" + str(random.randint(1, 20)) + "، واحد" + str(
                                random.randint(1, 4)), str(random.randint(1000000000, 9999999999)),
                            random.choice(teller_salary), random.randint(1, 110)))
            counter+=1
        self.cursor.executemany(insert_customers, customers)
        self.cursor.executemany(insert_tellers, tellers)
        self.cursor.executemany(insert_admins, admins)
        self.cursor.executemany(insert_managers, managers)
        self.cursor.executemany(insert_guarantors, guarantors)
        self.connection.commit()


    def populate_branches(self):
        insert_branches = """
                       INSERT INTO Branches
                       (branch_name,date_of_establishment, capital, phone_number, address)
                       VALUES ( %s, %s, %s, %s, %s)
                       """
        branches = []
        counter = 0
        while counter < 110:
            branches.append((random.choice(self.branch_names), str(random.randint(1340,1401))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28)), random.randint(50000000000,400000000000),str(random.randint(12345678911,99999999999)),random.choice(self.cities)+"، خیابان " + random.choice(self.cities)+ "، پلاک " + str(random.randint(1,150))) )
            counter+=1
        self.cursor.executemany(insert_branches, branches)
        self.connection.commit()

    def populate_accounts(self):
        insert_accounts = """
                               INSERT INTO Accounts
                               (sheba,open_date, close_date, status, balance, account_type, branch, opener, closer)
                               VALUES ( %s, %s, %s, %s, %s , %s, %s, %s, %s)
                               """
        accounts = []
        statuses = [True] * 80 + [False] * 1
        closed = [False] * 30 + [True] * 1
        counter = 0
        branch_nums = random.sample(range(1, 111), 110)
        while counter < 300:
            is_closed = random.choice(closed)
            if is_closed == False:
                accounts.append((str(random.randint(100000000000000000000000,999999999999999999999999)),
                                 str(random.randint(1340, 1401)) + '-' + str(random.randint(1, 12)) + '-' + str(
                                     random.randint(1, 28)),None,random.choice(statuses),random.randint(300000,300000000000), random.randint(1,4), random.randint(1,110),
                                 random.randint(1,250), None))
            else:
                open_year = random.randint(1340, 1398)
                accounts.append((str(random.randint(100000000000000000000000, 999999999999999999999999)),
                                 str(open_year) + '-' + str(random.randint(1, 12)) + '-' + str(
                                     random.randint(1, 28)), str(random.randint(open_year,1401)) + '-' + str(random.randint(1, 12)) + '-' + str(
                                     random.randint(1, 28)), True,
                                 0, random.randint(1, 4), random.randint(1, 110),
                                 random.randint(1, 250), random.randint(1, 250)))
            counter += 1
        self.cursor.executemany(insert_accounts, accounts)
        self.connection.commit()
    def populate_internet_banks(self):
        insert_internet_banks = """
                       INSERT INTO InternetBanks
                       (username,password, issue_date, customer, branch, issuer)
                       VALUES ( %s, %s, %s, %s, %s,%s)
                       """
        internet_banks = []
        counter = 0
        customers = random.sample(range(1, 251), 150)
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        all = lower + upper + num+lower + upper + num
        while counter < 150:
            temp = random.sample(all, 64)
            internet_banks.append((customers[counter],"".join(temp), str(random.randint(1392,1401))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28)), customers[counter],random.randint(1,110),random.randint(1,250)) )
            counter+=1
        self.cursor.executemany(insert_internet_banks, internet_banks)
        self.connection.commit()

    def populate_loans(self):
        insert_loans = """
                       INSERT INTO Loans
                       (start_date ,remainder, loan_type, branch, account, guarantor)
                       VALUES ( %s, %s, %s, %s, %s,%s)
                       """
        loans = []
        counter = 0
        self.cursor.execute(
            "SELECT id FROM `Accounts` WHERE account_type = 3")
        accounts = self.cursor.fetchall()
        loan_accounts = []
        guarantors = random.sample(range(1, 111), 110)
        for account in accounts:
            loan_accounts.append(account[0])
        while counter < 110:
            loans.append((str(random.randint(1360,1401))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28)), random.randint(1,10)*10000000,random.randint(1,4), random.randint(1,110),random.choice(loan_accounts),guarantors[counter]) )
            counter+=1
        self.cursor.executemany(insert_loans, loans)
        self.connection.commit()

    def populate_account_ownerships(self):
        insert_ownerships = """
                       INSERT INTO AccountOwnerships
                       (account_id, customer_id)
                       VALUES ( %s, %s)
                       """
        ownerships = []
        counter = 0
        accounts = random.sample(range(1, 301), 300)
        customers = random.sample(range(1, 251), 250)
        while counter < 350:
            if counter <250:
                ownerships.append((accounts[counter], customers[counter]))
                counter += 1
            elif counter<300:
                ownerships.append((accounts[counter], random.randint(1,250)))
                counter += 1
            else:
                new_owner = (random.randint(1,300), random.randint(1,250))
                if new_owner not in ownerships:
                    ownerships.append(new_owner)
                    counter+=1


        self.cursor.executemany(insert_ownerships, ownerships)
        self.connection.commit()

    def populate_cards(self):
        self.cursor.execute("SELECT customer_id, account_id FROM AccountOwnerships INNER JOIN Accounts ON AccountOwnerships.account_id = Accounts.id where Accounts.account_type = 1 or Accounts.account_type = 4")
        accounts_and_owners = self.cursor.fetchall()
        insert_cards = """
                              INSERT INTO Cards
                              (cvv2, issue_date, expiration_date, close_date, first_password, second_password, status, owner, branch, account, issuer, closer)
                              VALUES ( %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)
                              """
        cards = []
        counter = 0
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        all = lower + upper + num + lower + upper + num
        cvv2s = random.sample(range(100,1000), 110)
        closed = [False] * 40 + [True] * 1
        shuffle = random.sample(range(0,179), 110)
        while counter < 110:
            temp = random.sample(all, 4)
            temp2 = random.sample(all, 4)
            year = random.randint(1387,1400)
            month = random.randint(1,12)
            day = random.randint(1,28)
            is_closed = random.choice(closed)
            if not is_closed:
                cards.append((cvv2s[counter],str(year)+'-'+str(month)+'-'+str(day) ,str(year+5)+'-'+str(month)+'-'+str(day) ,None,"".join(temp),"".join(temp2) ,
                              not is_closed,accounts_and_owners[shuffle[counter]][0],random.randint(1,110),accounts_and_owners[shuffle[counter]][1], random.randint(1,250),None ) )
            else:
                cards.append((cvv2s[counter], str(year) + '-' + str(month) + '-' + str(day),
                              str(year + 5) + '-' + str(month) + '-' + str(day), str(year+1)+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28)) , "".join(temp), "".join(temp2),
                              not is_closed, accounts_and_owners[shuffle[counter]][0], random.randint(1, 110), accounts_and_owners[shuffle[counter]][1],
                              random.randint(1, 250), random.randint(1, 250)))
            counter+=1
        self.cursor.executemany(insert_cards, cards)
        self.connection.commit()

    def populate_transactions(self):
        insert_transactions = """
                       INSERT INTO Transactions
                       (transaction_id, account_id, amount, transaction_type, transaction_date, admin_id, teller_id, internet_bank_id)
                       VALUES ( %s, %s, %s, %s, %s,%s, %s, %s)
                       """
        transactions = []
        counter = 1
        self.cursor.execute(
            "SELECT id FROM `Accounts` WHERE account_type = 1 or account_type = 2 or account_type = 4")
        accounts = self.cursor.fetchall()
        withdraw_accounts = []
        for account in accounts:
            withdraw_accounts.append(account[0])
        internet_banks = [(18,7,69), (112, 27,136), (145,226,16), (92,89,71)]
        two_parts = [False] * 10 + [True] * 1
        while counter < 151:
          if counter%40 == 0:
              date = str(random.randint(1390, 1401)) + '-' + str(random.randint(1, 12)) + '-' + str(
                  random.randint(1, 28))
              transactions.append((counter, internet_banks[int(counter/40)][2], random.randint(1, 20) * 10000000,
                                   "واریز",
                                   date, None, None, internet_banks[int(counter/40)][0]))
              counter += 1
          else:
            is_two_parts = random.choice(two_parts)
            if not is_two_parts:
                is_deposit = random.choice([True, False])
                doer = random.choice([1,2])
                if not is_deposit:
                    if doer ==1:
                        transactions.append((counter,random.choice(withdraw_accounts),random.randint(1,20)*10000000,"برداشت",str(random.randint(1380,1401))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28)), random.randint(1,110),None,None ))
                    if doer ==2:
                        transactions.append((counter,random.choice(withdraw_accounts),random.randint(1,20)*10000000,"برداشت",str(random.randint(1380,1401))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28)), None,random.randint(1,250),None ))
                else:
                    if doer ==1:
                        transactions.append((counter,random.randint(1,300),random.randint(1,20)*10000000,"واریز",str(random.randint(1380,1401))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28)), random.randint(1,110),None,None ))
                    if doer ==2:
                        transactions.append((counter,random.randint(1,300),random.randint(1,20)*10000000,"واریز",str(random.randint(1380,1401))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28)), None,random.randint(1,250),None ))
                counter+=1
            else:
                doer = random.choice([1, 2])
                if doer == 1:
                    admin = random.randint(1, 110)
                    amount = random.randint(1, 20) * 10000000
                    date = str(random.randint(1380, 1401)) + '-' + str(random.randint(1, 12)) + '-' + str(
                                             random.randint(1, 28))
                    transactions.append((counter, random.choice(withdraw_accounts), amount,
                                         "برداشت",
                                         date, admin, None, None))
                    transactions.append((counter, random.randint(1,300), amount,
                                         "واریز",
                                         date, admin, None, None))
                if doer == 2:
                    teller = random.randint(1, 250)
                    amount = random.randint(1, 20) * 10000000
                    date = str(random.randint(1380, 1401)) + '-' + str(random.randint(1, 12)) + '-' + str(
                        random.randint(1, 28))
                    transactions.append((counter, random.choice(withdraw_accounts), amount,
                                         "برداشت",
                                         date, None, teller, None))
                    transactions.append((counter, random.randint(1,300), amount,
                                         "واریز",
                                         date, None, teller, None))

                counter += 1

        self.cursor.executemany(insert_transactions, transactions)
        self.connection.commit()

if __name__ == '__main__':
     dataGenerator = DataGenerator()
     # dataGenerator.create_tables()
     # dataGenerator.populate_loan_and_account_types()
     # dataGenerator.populate_branches()
     # dataGenerator.populate_people()
     #dataGenerator.populate_accounts()
     #dataGenerator.populate_internet_banks()
     #dataGenerator.populate_account_ownerships()
     #dataGenerator.populate_cards()
     #dataGenerator.populate_loans()
     dataGenerator.populate_transactions()




