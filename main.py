import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# graphic config
fig, ax = plt.subplots()
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_title('Uso de CPU e memória')
ax.set_ylabel('Uso (*)')
ax.set_xlabel('Tempo')
cpu_line, = ax.plot([], [], label='CPU', color='#FF0000')
mem_line, = ax.plot([], [], label='Memória', color='#00FF00')
ax.legend()

# Add text to values
cpu_text = ax.text(0.77, 0.7, '', transform=ax.transAxes)
mem_text = ax.text(0.77, 0.6, '', transform=ax.transAxes)


def update_chart(frame):
    cpu_percent = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    mem_percent = mem.percent

    cpu_line.set_data(list(range(frame)), [cpu_percent] * frame)
    mem_line.set_data(list(range(frame)), [mem_percent] * frame)

    cpu_text.set_text(f'CPU: {cpu_percent:.1f}%')
    mem_text.set_text(f'Memória: {mem_percent:.1f}%')

    return cpu_line, mem_line, cpu_text, mem_text


animation = FuncAnimation(fig, update_chart, frames=100, interval=1000, blit=True)

for line in [cpu_line, mem_line]:
    line.set_linewidth(2)
    line.set_marker('o')
    line.set_markersize(5)

ax.set_facecolor('#F5F5F5')

plt.show()
