def new_func():
    telebeler = [
    {
        'ad':'Iman',
        'staj_il':45
    },
    {
        'ad':'Tural',
        'staj_il':5
    },
    {
        'ad':'Zair',
        'staj_il':13
    },
    {
        'ad':'Miri',
        'staj_il':4
    }
]
    tecrube=[]
    for age in telebeler:
        tecrube.append(age['staj_il'])
    print(max(tecrube))

new_func()

