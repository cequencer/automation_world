import json
import string
import random
import pandas as pd

nations = pd.read_csv('data/src/nations.csv')
nation_adjs = []
for i, r in nations.iterrows():
    nation = r['Country name']
    adj = r['Adjectivals'].split(', ')[-1]
    adj = adj.split(' or ')[0]
    nation_adjs.append(adj)

def make_news(skill):
    nation = random.choice(nation_adjs)
    headline = '{nation} {researchers} {action}'.format(
        nation=nation,
        researchers=random.choice([
            'researchers',
            'scientists',
            'engineers'
        ]),
        action=random.choice([
            'pioneered a new technique in {skill} today.',
            'unveiled an algorithm capable of {skill}.',
            'performs {skill} like a human.'
        ]).format(skill=skill.lower())
        # action=random.choice([
        #     'make breakthrough',
        #     'make advancement',
        #     'make discovery',
        #     'advance robotics',
        #     'develop new tech'
        # ])
    )
    body = random.choice([
        'Robotics researchers at the {nation} Institute of Technology pioneered a new technique in {skill} today.',
        'The {nation} Institute of Technology unveiled an algorithm capable of {skill}.',
        'The {nation} Institute of Technology showcased a system competitive with humans at {skill}.',
        'A new algorithm from The {nation} Institute of Technology performs {skill} like a human.'
    ])
    body = body.format(nation=nation, skill=skill.lower())

    return {
        'headline': headline,
        'body': body
    }


def bot_name():
    return '{}{}-{}'.format(
        random.choice(string.ascii_uppercase),
        random.choice('aeiouy'),
        ''.join(random.choice(string.digits) for _ in range(4)))

automation_schedule = pd.read_csv('data/src/orderedOnetSkillsByComputerization.csv')
automation_schedule = automation_schedule.iloc[::-1]

# Limit skills we automate to only those w/ positive correlation
automation_schedule = automation_schedule[automation_schedule.correlation > 0]

skill_edits = pd.read_csv('data/src/Clean Skills - orderedOnetSkillsByComputerization.csv')
omitted_skills = skill_edits[skill_edits['Omit?'] == 1.0]['Skill'].tolist()
renamed_skills = skill_edits[skill_edits['Omit?'] != 1.0][['Skill', 'Short name']].dropna()
renamed_skills = dict(zip(renamed_skills['Skill'], renamed_skills['Short name']))

skills = json.load(open('data/skills.json'))
skills_idx = {s['name']: s['id'] for s in skills.values()}

game_months = (65-18)*12
start_month = 10
n_scenarios = 2
scenarios = []
print('n skills', len(automation_schedule))
for i in range(n_scenarios):
    schedule = []
    month = start_month
    for j, row in automation_schedule.iterrows():
        skill = row.Skill
        if skill in omitted_skills: continue
        skill = renamed_skills.get(skill, skill)
        month += random.randint(4,8)
        schedule.append({
            'id': j,
            'months': month,
            'name': bot_name(),
            'skills': [skills_idx[skill]],
            'deepeningCountdown': random.randint(2*12, 25*12),
            'efficiency': random.random(),
            'news': make_news(skill)
        })

    scenario = {
        'name': 'Scenario {}'.format(i),
        'schedule': schedule
    }
    scenarios.append(scenario)

    # Check that there's enough game time
    # to release all robots
    print('End month:', month)
    print('Game months:', game_months)
    print('Schedule:', len(schedule))

with open('data/src/scenarios.json', 'w') as f:
    json.dump(scenarios, f, sort_keys=True, indent=2)
with open('data/scenarios.json', 'w') as f:
    json.dump(scenarios, f, sort_keys=True, indent=2)
