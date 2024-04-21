from die import Die
import pygal
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке
results = []
for _ in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = 'Результат за 1000 бросков 2 кубиков D6'
hist.x_labels = [str(e) for e in range(2, 13)]
hist.x_title = "Result"
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')