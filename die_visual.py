from die import Die
import pygal
die = Die()

# Моделирование серии бросков с сохранением результатов в списке
results = [die.roll() for _ in range(1000)]

# Анализ результатов
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

# Визуализация результатов.
hist = pygal.Bar()

hist.title = 'Результат за 1000 бросков D6'
hist.x_labels = [str(e) for e in range(1, 7)]
hist.x_title = "Result"
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')