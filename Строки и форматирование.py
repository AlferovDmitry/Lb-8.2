def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        return 'У тебя {} друзей'.format(len(DATABASE))
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'

print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))
