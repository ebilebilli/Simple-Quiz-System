def quiz_data_writer(name, point_name):
    with open('quiz_data.txt', 'a+') as file:
        file.write(f'User name: {name}, User point: {point_name}\n')