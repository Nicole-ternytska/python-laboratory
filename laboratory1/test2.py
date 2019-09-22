x_A = int(input('Введіть координату Х точки А: '))
y_A = int(input('Введіть координату Y точки А: '))
x_B = int(input('Введіть координату Х точки B: '))
y_B = int(input('Введіть координату Y точки B: '))
x_C = int(input('Введіть координату Х точки C: '))
y_C = int(input('Введіть координату Y точки C: '))
x_D = int(input('Введіть координату Х точки D: '))
y_D = int(input('Введіть координату Y точки D: '))
averageX1 = (x_A + x_C) / 2
averageY1 = (y_A + y_C) / 2
averageX2 = (x_B + x_D) / 2
averageY2 = (y_B + y_D) / 2
if averageX1 == averageX2 and averageY2 == averageY1:
    print('Точки є вершинами паралелограму')
else:
    print('Точки не є вершинами паралелограма')