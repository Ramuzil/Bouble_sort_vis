import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from matplotlib.widgets import Button, Slider

class BubbleSortVisualizer:
    def __init__(self, array_size=50):
        self.array_size = array_size
        self.arr = [random.randint(1, 100) for _ in range(array_size)]
        self.original_arr = self.arr.copy()
        
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        plt.subplots_adjust(bottom=0.35)
        
        self.bars = None
        self.paused = False
        self.speed = 1.0
        self.comparisons = 0
        self.swaps = 0
        self.sorted_indices = set()
        
        self.setup_ui()
        self.draw_bars()
        
    def setup_ui(self):
        """Setup pause button and speed slider"""
        # Pause button
        ax_pause = plt.axes([0.45, 0.05, 0.1, 0.075])
        self.btn_pause = Button(ax_pause, 'Pause/Resume')
        self.btn_pause.on_clicked(self.toggle_pause)
        
        # Reset button
        ax_reset = plt.axes([0.57, 0.05, 0.1, 0.075])
        self.btn_reset = Button(ax_reset, 'Reset')
        self.btn_reset.on_clicked(self.reset_sort)
        
        # Speed slider
        ax_speed = plt.axes([0.2, 0.15, 0.6, 0.03])
        self.slider_speed = Slider(ax_speed, 'Speed', 0.1, 5.0, valinit=1.0, step=0.1)
        self.slider_speed.on_changed(self.update_speed)
        
        self.ax.set_title('Bubble Sort Visualization', fontsize=14, fontweight='bold')
        
    def draw_bars(self):
        """Draw bars representing array elements"""
        self.ax.clear()
        colors = []
        for i in range(len(self.arr)):
            if i in self.sorted_indices:
                colors.append('green')
            else:
                colors.append('steelblue')
        
        self.bars = self.ax.bar(range(len(self.arr)), self.arr, color=colors)
        self.ax.set_ylim(0, 105)
        self.ax.set_xlim(-1, len(self.arr))
        self.ax.set_xlabel('Index', fontsize=10)
        self.ax.set_ylabel('Value', fontsize=10)
        
        info_text = f'Comparisons: {self.comparisons} | Swaps: {self.swaps} | Speed: {self.speed:.1f}x'
        self.ax.text(0.5, 1.08, info_text, transform=self.ax.transAxes, 
                     ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
    def update_bar_colors(self, comparing_indices=None, swapping_indices=None):
        """Update bar colors based on sort state"""
        colors = []
        for i in range(len(self.arr)):
            if i in self.sorted_indices:
                colors.append('green')
            elif comparing_indices and i in comparing_indices:
                colors.append('red')
            elif swapping_indices and i in swapping_indices:
                colors.append('orange')
            else:
                colors.append('steelblue')
        
        for bar, color, val in zip(self.bars, colors, self.arr):
            bar.set_color(color)
            bar.set_height(val)
    
    def toggle_pause(self, event):
        """Toggle pause state"""
        self.paused = not self.paused
        
    def update_speed(self, val):
        """Update animation speed"""
        self.speed = self.slider_speed.val
        
    def reset_sort(self, event):
        """Reset to original array"""
        self.arr = self.original_arr.copy()
        self.comparisons = 0
        self.swaps = 0
        self.sorted_indices = set()
        self.draw_bars()
        self.fig.canvas.draw_idle()
        
    def animate_sort(self):
        """Generator for bubble sort animation"""
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                # Wait if paused
                while self.paused:
                    yield
                
                # Highlight comparison
                self.comparisons += 1
                self.update_bar_colors(comparing_indices=[j, j + 1])
                self.draw_bars()
                self.fig.canvas.draw_idle()
                
                # Delay based on speed
                for _ in range(int(10 / self.speed)):
                    yield
                
                # Perform swap if needed
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    self.swaps += 1
                    
                    self.update_bar_colors(swapping_indices=[j, j + 1])
                    self.draw_bars()
                    self.fig.canvas.draw_idle()
                    
                    for _ in range(int(10 / self.speed)):
                        yield
            
            # Mark as sorted
            self.sorted_indices.add(n - i - 1)
            self.update_bar_colors()
            self.draw_bars()
            self.fig.canvas.draw_idle()
        
        # Mark last element as sorted
        self.sorted_indices.add(0)
        self.update_bar_colors()
        self.draw_bars()
        self.fig.canvas.draw_idle()
        
    def run(self):
        """Run the visualization"""
        self.anim = animation.FuncAnimation(
            self.fig, lambda frame: None, 
            frames=self.animate_sort(),
            blit=False, interval=50
        )
        plt.show()

if __name__ == "__main__":
    visualizer = BubbleSortVisualizer(array_size=50)
    visualizer.run()
