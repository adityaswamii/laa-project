imgdata = {
    'A': '',
}

data = {

    -2: {
        'text': 'ok :( bye',
        'choices': {' ': -2},
    },
    -1: {
        'text': 'Game Over. Try again?',
        'choices': {'YES': 0, 'NO': -2},
    },
    0: {
        'text': 'Do you want to go back in time?',
        'choices': {'YES': 1, 'NO': -1},
    },
    1: {
        'text': 'How far back in time do you want to go?',
        'choices': {'THIS MORNING': 2, 'EVEN FURTHER BACK': 8},
    },
    2: {
        'text': 'You wake up in your bed at the start of the day. Later today, the bullies are going to force you to steal exam papers from the principal\'s office. Do you decide to go to school today?',
        'choices': {'YES': 3, 'NO': 7},
    },
    3: {
        'text': 'You go to school. As expected, during lunch break you find yourself surrounded by your bullies in the corridor behind the principal\'s office. What do you do?',
        'choices': {'RUN AWAY': 4, 'TRY TO REASON WITH THEM': 5},
    },
    4: {
        'text': 'You muster up all your courage and push back one of the bullies and sprint down the corridor behind him. You hear footsteps giving chase behind you but you\'re able to hide in a washroom stall for the rest of the break. However, one of them steals the exam papers on their own and hides it in your bag without you knowing.',
        'choices': {'': 6},
    },
    5: {
        'text': 'You try to stand up for yourself and reason your way out of this predicament. However, with yesterday\'s memory still fresh in your brain, you freeze up and eventually get pressured into stealing the exam papers from the principal\'s office again. Just like yesterday, they copy all the exam questions and force you to hide the papers in your bag once class starts.',
        'choices': {'': 6},
    },
    6: {
        'text': 'The principal walks into the classroom in the middle of your last class and everyone\'s bags are checked. You are caught red-handed with the exam papers in your bag and get suspended for a week. At home, you are scolded by your parents again. Despite going back in time, you have failed to change the outcome of the day.',
        'choices': {'': -1},
    },
    7: {
        'text': 'You decide to stay home for the day. After much arguing with your parents you are able to convince them to let you skip school. Thanks to the extended argument, however, they are now late for work. As a result, they end up speeding on their way to the office when the car\'s brake gets jammed. Their car crashes into an oncoming truck at full speed and they die on the spot.',
        'choices': {'': -1},
    },
    8: {
        'text': 'You have gone back 5 years. You can restart and pick an entirely new high school trajectory for yourself. Which high school do you pick?',
        'choices': {'GREENWOOD HIGH': 9, 'MAGNOLIA HIGH': 15},
    },
    9: {
        'text': 'During your time here at Greenwood High you are given 2 choices. Focus entirely on your academic grades, or enroll in the Greenwood High\'s partnered therapy program : MyDost.',
        'choices': {'MYDOST': 10, 'ACADEMICS': 13},
    },
    10: {
        'text': 'You learn to be more assertive and confident in your interactions with others. You develop a positive sense of self-worth and a better understanding of how to deal with difficult situations.',
        'choices': {'': 11},
    },
    11: {
        'text': 'You encounter one of your bullies again in 5 years. This time, you talk it out with them calmly and assertively. using your newfound confidence and assertiveness developed from therapy.',
        'choices': {'': 12},
    },
    12: {
        'text': 'Long-term, you  look back on your experience with the bully and are proud of how you handled the situation.',
        'choices': {'': -1},
    },
    13: {
        'text': 'If you choose to focus solely on your grades, you work hard and become a top scholar. You end up making good friends who support and encourage you. You continue to excel in school and feel fulfilled by your academic achievements.',
        'choices': {'': 14},
    },
    14: {
        'text': 'In the next 5 years you never run into a bully again, instead surrounded by like-minded individuals focused on bettering themselves and on the path to success.',
        'choices': {'': -1},
    },
    15: {
        'text': 'During your time here at Magnolia High you are given 2 choices. Focus entirely on your academic grades, or enroll in Magnolia High\'s exclusive martial arts program.',
        'choices': {'MARTIAL ARTS': 16, 'ACADEMICS': 13},
    },
    16: {
        'text': 'You start to train in Magnolia High\'s reputed martial arts program. As you become more proficient in self-defense in the form of Brazilian jiu-jitsu, you naturally build healthy trust and confidence in your own body.',
        'choices': {'': 17},
    },
    17: {
        'text': 'You encounter one of your bullies again in 5 years and must decide how to handle the situation. This time, you are capable of teaching them a lesson with your newfound proficiency on martial arts.',
        'choices': {'TALK IT OUT': 18, 'TAKE HIM DOWN': 20},
    },
    18: {
        'text': 'You talk it out with them calmly and assertively. using your newfound confidence developed from martial arts.',
        'choices': {'': 19},
    },
    19: {
        'text': 'In the future, you will be able to look back on your experience with the bully be proud of how you handled the situation and how it shaped you as a person.',
        'choices': {'': -1},
    },
    20: {
        'text': 'You use your martial arts training to brutally take down the former bully. You show no mercy or consideration for disciplinary action and continue beating them up until third-party intervention.',
        'choices': {'': 21},
    },
    21: {
        'text': 'Your bully is hospitalized with several broken bones and internal damage. Your actions lead to you being rusticated from Magnolia High and its martial arts academy. Worth it?',
        'choices': {'': -1},
    },

}


def runChoice(n):
    print('\n', data[n]['text'])
    userInput = " "
    while userInput not in data[n]['choices']:
        if '' in data[n]['choices']:
            print('PRESS ENTER')
        else:
            print('Options: ', list(data[n]['choices'].keys()))
        userInput = input().upper()
        if userInput in data[n]['choices']:
            runChoice(data[n]['choices'][userInput])
        elif userInput == "EXIT":
            break
        else:
            print('Please enter a valid option')


runChoice(0)