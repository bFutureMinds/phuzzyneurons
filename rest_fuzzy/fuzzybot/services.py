from chatterbot import ChatBot
from chatterbot.training.trainers import ListTrainer


def getBot():

    chatterbot= ChatBot(
        "Example ChatterBot",
        database='chatterbot-database',
        logic_adapters=[
        "chatterbot.adapters.logic.ClosestMatchAdapter",
        ],
        read_only=True,
    )
    chatterbot.set_trainer(ListTrainer)

    dataList = [
        ["Hi",
         "Hello",
         "Hello",
         "Hello",
         "Hello",
         "hi",
         "How are you?",
         "I am good.",
         "That is good to hear.",
         "Thank you",
         "You are welcome.",
         ], [
            'The credit limit was exceeded',
            'Your Credit limit has exceeded. Kindly make the payment for your card befor initiation any more transaction on the same card.'
        ], [
            'Card limit has exceeded',
            'Your Credit limit has exceeded. Kindly make the payment for your card befor initiation any more transaction on the same card.'
        ], [
            'This transaction cannot be processsedas you creadit card limit was exceeded',
            'Your Credit limit has exceeded. Kindly make the payment for your card befor initiation any more transaction on the same card.'
        ], [
            'Payment Failure. Credit limit exhausted',
            'Your Credit limit has exceeded. Kindly make the payment for your card befor initiation any more transaction on the same card.'
        ], [
            'I get a Messgae my credit limit has exceeded. What Shoud I do?',
            'Your Credit limit has exceeded. Kindly make the payment for your card befor initiation any more transaction on the same card.'
        ], [
            'While trying to make a payment I see a message my Credit limit has exhusted',
            'Your Credit limit has exceeded. Kindly make the payment for your card befor initiation any more transaction on the same card.'
        ], [
            'I cannot complete my transaction. My credit limit has exceeded.Please help',
            'Your Credit limit has exceeded. Kindly make the payment for your card befor initiation any more transaction on the same card.'
        ], [
            'Transaction is failing with message my credit limit exceeded',
            'Your Credit limit has exceeded. Kindly make the payment for your card befor initiation any more transaction on the same card.'
        ], [
            'The card had expired',
            'Your card has expired.You need to renew your card details.Please follow the below link for renewal process:www.barclayscardus.com'
        ], [
            'My card has expired.Please suggest',
            'Your card has expired.You need to renew your card details.Please follow the below link for renewal process:www.barclayscardus.com'
        ], [
            'Cannot make payment with my card. Its expired.',
            'Your card has expired.You need to renew your card details.Please follow the below link for renewal process:www.barclayscardus.com'
        ], [
            'Card expired!',
            'Your card has expired.You need to renew your card details.Please follow the below link for renewal process:www.barclayscardus.com'
        ], [
            'I cannot carry out any transaction.My card has expired',
            'Your card has expired.You need to renew your card details.Please follow the below link for renewal process:www.barclayscardus.com'
        ], [
            'I am getting  messagemy card has expired',
            'Your card has expired.You need to renew your card details.Please follow the below link for renewal process:www.barclayscardus.com'
        ], [
            'Transaction is failing with messagemy credit has expired.',
            'Your card has expired.You need to renew your card details.Please follow the below link for renewal process:www.barclayscardus.com'
        ], [
            'Credit card expired.How can i renew it?',
            'Your card has expired.You need to renew your card details.Please follow the below link for renewal process:www.barclayscardus.com'
        ], [
            'How can I pay my bills online?',
            'To pay your credit card bill online log in to your account and select MAKE A PAYMENT. You may choose to make a single payment or sign up for automatic repeat monthly payments.'
        ], [
            'Is there a way I can make online billl payment for my card',
            'To pay your credit card bill online log in to your account and select MAKE A PAYMENT. You may choose to make a single payment or sign up for automatic repeat monthly payments.'
        ], [
            'Bill payment Issue. Procedure to pay bills online?',
            'To pay your credit card bill online log in to your account and select MAKE A PAYMENT. You may choose to make a single payment or sign up for automatic repeat monthly payments.'
        ], [
            'Can I make online payments of my bill?',
            'To pay your credit card bill online log in to your account and select MAKE A PAYMENT. You may choose to make a single payment or sign up for automatic repeat monthly payments.'
        ], [
            'How can i pay my card bills through website',
            'To pay your credit card bill online log in to your account and select MAKE A PAYMENT. You may choose to make a single payment or sign up for automatic repeat monthly payments.'
        ], [
            'Is there a online way to make my card bill payment?',
            'To pay your credit card bill online log in to your account and select MAKE A PAYMENT. You may choose to make a single payment or sign up for automatic repeat monthly payments.'
        ], [
            'I want to make a online payment of my bills. Where can i do that?',
            'To pay your credit card bill online log in to your account and select MAKE A PAYMENT. You may choose to make a single payment or sign up for automatic repeat monthly payments.'
        ], [
            'I want to make a online payment of my bills. How can i do that?',
            'To pay your credit card bill online log in to your account and select MAKE A PAYMENT. You may choose to make a single payment or sign up for automatic repeat monthly payments.'
        ], [
            'What variety of options do I have to make a payment?',
            'You can make a payment online through the Barclaycard Mobile App by phone at 302-622-8990  or by mail to either of the following address: Card Services P.O. Box 13337 Philadelphia PA...'
        ], [
            'Ways to make my card payments',
            'You can make a payment online through the Barclaycard Mobile App by phone at 302-622-8990  or by mail to either of the following address: Card Services P.O. Box 13337 Philadelphia PA...'
        ], [
            'Payment Options for bill payment',
            'You can make a payment online  through the Barclaycard Mobile App by phone at 302-622-8990  or by mail to either of the following address: Card Services P.O. Box 13337 Philadelphia PA...'
        ], [
            'What are the available options for bill payment?',
            'You can make a payment online  through the Barclaycard Mobile App by phone at 302-622-8990  or by mail to either of the following address: Card Services P.O. Box 13337 Philadelphia PA...'
        ], [
            'How to make my cards bill payment?',
            'You can make a payment online  through the Barclaycard Mobile App by phone at 302-622-8990  or by mail to either of the following address: Card Services P.O. Box 13337 Philadelphia PA...'
        ], [
            'Can you help me with the my cards bill payment?',
            'You can make a payment online  through the Barclaycard Mobile App by phone at 302-622-8990  or by mail to either of the following address: Card Services P.O. Box 13337 Philadelphia PA...'
        ], [
            'Options to make credit card bill payment',
            'You can make a payment online  through the Barclaycard Mobile App by phone at 302-622-8990  or by mail to either of the following address: Card Services P.O. Box 13337 Philadelphia PA...'
        ], [
            'How can i pay my credit cards bill?',
            'You can make a payment online  through the Barclaycard Mobile App by phone at 302-622-8990  or by mail to either of the following address: Card Services P.O. Box 13337 Philadelphia PA...'
        ], [
            'How long does it take to process an online payment?',
            'Want to know when your online mobile or phone payment will be processed and when your available credit will be updated? Find out fast with this handy link.'
        ], [
            'Online payment processing time ?',
            'Want to know when your online mobile or phone payment will be processed and when your available credit will be updated? Find out fast with this handy link.'
        ], [
            'What is the time taken to process an online payment?',
            'Want to know when your online mobile or phone payment will be processed and when your available credit will be updated? Find out fast with this handy link.'
        ], [
            'How long will I have to wait to see online payment status ?',
            'Want to know when your online mobile or phone payment will be processed and when your available credit will be updated? Find out fast with this handy link.'
        ], [
            'Time it takes for process a online payment?',
            'Want to know when your online mobile or phone payment will be processed and when your available credit will be updated? Find out fast with this handy link.'
        ], [
            'Processsing time for a bill payment made online?',
            'Want to know when your online mobile or phone payment will be processed and when your available credit will be updated? Find out fast with this handy link.'
        ], [
            'Can you tell me how long it take to process a online payment?',
            'Want to know when your online mobile or phone payment will be processed and when your available credit will be updated? Find out fast with this handy link.'
        ], [
            'Time require to process a online bill payment?',
            'Want to know when your online mobile or phone payment will be processed and when your available credit will be updated? Find out fast with this handy link.'
        ], [
            'What is my minimum payment amount?',
            'Your minimum payment is the payment thats required each billing period to keep your Credit Card account in good standing. Your monthly billing statement will tell you the minimum payment amount...'
        ], [
            'What is the minimum amount for my card pyment',
            'Your minimum payment is the payment thats required each billing period to keep your Credit Card account in good standing. Your monthly billing statement will tell you the minimum payment amount...'
        ], [
            'The minimum amount that needs to be paid by me for this card',
            'Your minimum payment is the payment thats required each billing period to keep your Credit Card account in good standing. Your monthly billing statement will tell you the minimum payment amount...'
        ], [
            'Minimum transaction value for my card payment',
            'Your minimum payment is the payment thats required each billing period to keep your Credit Card account in good standing. Your monthly billing statement will tell you the minimum payment amount...'
        ], [
            'What is the minimum payment amount I can pay for my card bill?',
            'Your minimum payment is the payment thats required each billing period to keep your Credit Card account in good standing. Your monthly billing statement will tell you the minimum payment amount...'
        ], [
            'Tell mewhat is the minimum payment amount for my card?',
            'Your minimum payment is the payment thats required each billing period to keep your Credit Card account in good standing. Your monthly billing statement will tell you the minimum payment amount...'
        ], [
            'What is the Minimum transaction value for my cards bill payment?',
            'Your minimum payment is the payment thats required each billing period to keep your Credit Card account in good standing. Your monthly billing statement will tell you the minimum payment amount...'
        ], [
            'What is the lower limit for paying my cards bill payment?',
            'Your minimum payment is the payment thats required each billing period to keep your Credit Card account in good standing. Your monthly billing statement will tell you the minimum payment amount...'
        ], [
            'How often can I change my due date?',
            'You can change your payment due date once every 120 days.'
        ], [
            'Can I change my due date for payment',
            'You can change your payment due date once every 120 days.'
        ], [
            'Is there any limitation on number of times I can change my payment due date?',
            'You can change your payment due date once every 120 days.'
        ], [
            'Maximum times I can change my due dates for payment',
            'You can change your payment due date once every 120 days.'
        ], [
            'How many times I can change my due date for bill payment?',
            'You can change your payment due date once every 120 days.'
        ], [
            'I want to change my payment due date?How many times I am allowed to do this?',
            'You can change your payment due date once every 120 days.'
        ], [
            'Is there a limit to number of times i Can change my payment due date?',
            'You can change your payment due date once every 120 days.'
        ], [
            'Can you tell me how many times is it allowed to change the payment due date?',
            'You can change your payment due date once every 120 days.'
        ], [
            'How can I change my payment due date?',
            'You can change your payment due date by clicking on Change Payment Due Date under Account Settings. Note: Changing your payment due date will not affect any payments currently due. Please continue to'
        ], [
            'I want to change my payment due date?Can you help?',
            'You can change your payment due date by clicking on Change Payment Due Date under Account Settings. Note: Changing your payment due date will not affect any payments currently due. Please continue to'
        ], [
            'Whats the procedure to change the payment due date?',
            'You can change your payment due date by clicking on Change Payment Due Date under Account Settings. Note: Changing your payment due date will not affect any payments currently due. Please continue to'
        ], [
            'Way to change payment due date?',
            'You can change your payment due date by clicking on Change Payment Due Date under Account Settings. Note: Changing your payment due date will not affect any payments currently due. Please continue to'
        ], [
            'I want to change my payment due date? How can i do this?',
            'You can change your payment due date by clicking on Change Payment Due Date under Account Settings. Note: Changing your payment due date will not affect any payments currently due. Please continue to'
        ], [
            'Is there a way I can change my payment due date?',
            'You can change your payment due date by clicking on Change Payment Due Date under Account Settings. Note: Changing your payment due date will not affect any payments currently due. Please continue to'
        ], [
            'Help with the process of changing the payment due date',
            'You can change your payment due date by clicking on Change Payment Due Date under Account Settings. Note: Changing your payment due date will not affect any payments currently due. Please continue to'
        ], [
            'Guide me through the process of changing the payment due date?',
            'You can change your payment due date by clicking on Change Payment Due Date under Account Settings. Note: Changing your payment due date will not affect any payments currently due. Please continue to'
        ], [
            'What if I need to make a payment and the website is down or unavailable?',
            'If you need to make a payment during a time when our website and/or Barclaycard Mobile App are down please call 302-622-8990 to make a payment.'
        ], [
            'I want to make a payment but seems website is not working?',
            'If you need to make a payment during a time when our website and/or Barclaycard Mobile App are down please call 302-622-8990 to make a payment.'
        ], [
            'Website is down I need to make a payment please help?',
            'If you need to make a payment during a time when our website and/or Barclaycard Mobile App are down please call 302-622-8990 to make a payment.'
        ], [
            'Is there a way I a can make payment if website is not unavailable or down?',
            'If you need to make a payment during a time when our website and/or Barclaycard Mobile App are down please call 302-622-8990 to make a payment.'
        ], [
            'I am trying to make my cards paymentbut i can see the website is down. Please help',
            'If you need to make a payment during a time when our website and/or Barclaycard Mobile App are down please call 302-622-8990 to make a payment.'
        ], [
            'I am unable to make my bill payment.Site is not working.',
            'If you need to make a payment during a time when our website and/or Barclaycard Mobile App are down please call 302-622-8990 to make a payment.'
        ], [
            'I am not able to make  payments for my bill. Site is unavailable?',
            'If you need to make a payment during a time when our website and/or Barclaycard Mobile App are down please call 302-622-8990 to make a payment.'
        ], [
            'Your site is not working. How can I pay my bills?',
            'If you need to make a payment during a time when our website and/or Barclaycard Mobile App are down please call 302-622-8990 to make a payment.'
        ], [
            'Can I use multiple bank accounts to make payments?',
            'Yes. You can add multiple bank accounts to use to make payments on your account.'
        ], [
            'Can I make paymens using multiple bank account?',
            'Yes. You can add multiple bank accounts to use to make payments on your account.'
        ], [
            'Is it possible to make payment using different bank accounts',
            'Yes. You can add multiple bank accounts to use to make payments on your account.'
        ], [
            'How can I use multiple bank accounts to make payments?',
            'Yes. You can add multiple bank accounts to use to make payments on your account.'
        ], [
            'I want to pay my bills using my two different bank acounts. Is there a way to do it?',
            'Yes. You can add multiple bank accounts to use to make payments on your account.'
        ], [
            'Can i use my different bank accounts to pay bill for my card?',
            'Yes. You can add multiple bank accounts to use to make payments on your account.'
        ], [
            'Is it permissible to pay bills using multiple bank accounts?',
            'Yes. You can add multiple bank accounts to use to make payments on your account.'
        ], [
            'Is it possible to make payment using different bank accounts on your site?',
            'Yes. You can add multiple bank accounts to use to make payments on your account.'
        ],
        [
            'What is my balance',
            'Your balance is {balance}',
        ]
        ,
        [
            'Can you tell me my balance',
            'Your balance is {balance}',
        ]
        ,
        [
            'Please tell me my account balance',
            'Your balance is {balance}',
        ]
        ,
        [
            'What is my account balance',
            'Your balance is {balance}',
        ],
        [
            'What is my account balance',
            'Your balance is {balance}',
        ],
        [
            'What is my balance',
            'Your balance is {balance}',
        ],
        [
            'Tell me my balance',
            'Your balance is {balance}',
        ]
    ]

    for data in dataList:
        chatterbot.train(data)
    return chatterbot
