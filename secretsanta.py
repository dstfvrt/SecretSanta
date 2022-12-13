def memberList():
    return ['Ben Favorite',   
            'Cass Favorite',  
            'Jauss Favorite', 
            'Dusty Favorite', 
            'Ben Hornsby',    
            'Kate Velazquez']

def emails():
    return { 'Ben Favorite'   : 'bnfvrt@gmail.com',
             'Cass Favorite'  : 'Cassfavorite@gmail.com',
             'Jauss Favorite' : 'joshfavorite03@gmail.com',
             'Dusty Favorite' : 'dstfvrt@gmail.com',
             'Ben Hornsby'    : 'Bhornsby48@gmail.com',
             'Kate Velazquez' : 'kkatevelazquez@gmail.com' }

def badPairs():
    return [('Kate Velazquez', 'Dusty Favorite'),
            ('Ben Hornsby', 'Cass Favorite')]

from random import sample
def createPartners():
    partners = list()
    senders, receivers = memberList(), memberList()

    for sender in senders:
        receiver = sample(receivers, 1)[0]
        receivers.remove(receiver)
        partners.append((sender, receiver))

    badPartners  = [ badPartner in partners or badPartner[::-1] in partners for badPartner in badPairs() ]
    samePartners = [ partner[0] == partner[1] for partner in partners ]

    if any(badPartners) or any(samePartners):
        return createPartners()
    else:
        return partners

import smtplib, ssl
def sendEmail(partners):
    port = 465
    password = input('Password: ')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login('dstfvrt@gmail.com', password)

        for partner in partners:
            message =(f'Merry Christmas, {partner[0]}!\n\n'                       +
                      f'This year your Secret Santa partner is {partner[1]}.\n\n' +
                       '                                            Sincerely,\n' +
                       '                                           Santa Claus\n' +
                       'You can find the code that produced this message here:\n' +
                       'https://github.com/dstfvrt/SecretSanta'                    )
            server.sendmail('dstfvrt@gmail.com', emails()[partner[0]], message)

def secretSanta():
    partners = createPartners()
    sendEmail(partners)

if __name__ == '__main__':
    secretSanta()

