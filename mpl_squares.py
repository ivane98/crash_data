import matplotlib.pyplot as plt

input_values = range(1, 5001)
squares = [x**3 for x in input_values]


plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(input_values, squares, c='red', cmap=plt.cm.Blues, s=10)

# ax.plot(input_values, squares, linewidth=3)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Numbers', fontsize=14)
ax.set_ylabel('Squares', fontsize=14)

ax.tick_params(labelsize=14)

# ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()

# plt.savefig('squares_plot.png', bbox_inches='tight')