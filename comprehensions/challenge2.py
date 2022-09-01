inch_measurement = (3, 8, 20)

cm_measurements = [2.54*x for x in inch_measurement]
print(cm_measurements)

cm_measurements = tuple([inch*2.54 for inch in inch_measurement])
print(cm_measurements)