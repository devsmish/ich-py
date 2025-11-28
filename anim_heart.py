import tkinter as tk
import time
import threading

B = chr(0x2588)

heart_big = [
    f'                  {B*5}         {B*5}',
    f'                {B*2}     {B*2}     {B*2}     {B*2}',
    f'               {B*2}        {B*2} {B*2}        {B*2}',
    f'               {B*2}         {B*3}         {B*2}',
    f'                 {B*2}                 {B*2}',
    f'                   {B*2}             {B*2}',
    f'                     {B*2}         {B*2}',
    f'                       {B*2}     {B*2}',
    f'                         {B*2} {B*2}',
    f'                          {B*3}',
]

heart_avg = [
    f'                      {B*3}     {B*3}',
    f'                    {B*2}   {B*2} {B*2}   {B*2}',
    f'                  {B*2}      {B*3}      {B*2}',
    f'                  {B*2}               {B*2}',
    f'                    {B*2}           {B*2}',
    f'                      {B*2}       {B*2}',
    f'                        {B*2}   {B*2}',
    f'                          {B*3}',
]

heart_small = [
    f'                      {B*3}     {B*3}',
    f'                    {B*2}   {B*2} {B*2}   {B*2}',
    f'                  {B*2}      {B*3}      {B*2}',
    f'                    {B*2}           {B*2}',
    f'                      {B*2}       {B*2}',
    f'                        {B*2}   {B*2}',
    f'                          {B*3}',
]

frames = [heart_small, heart_avg, heart_big, heart_avg]

# ----------- Неоновая пульсация цвета -----------
def neon_color(t):
    """
    Возвращает цвет RGB в зависимости от времени t.
    Создаёт мягкое свечение: яркость дышит.
    """
    intensity = int(150 + 105 * (1 + __import__("math").sin(t * 2.7)) / 2)
    return f"#{intensity:02x}0022"  # розовый неон (#FF0022 → #990022)


# ----------- Запуск окна и анимации -----------
def run_animation():
    root = tk.Tk()
    root.title("❤️ Neon Heartbeat Animation ❤️")
    root.configure(bg="black")

    text = tk.Label(root,
                    font=("Courier New", 18, "bold"),
                    justify="left",
                    fg="white",
                    bg="black")
    text.pack(padx=20, pady=20)

    def animate():
        t = 0
        while True:
            for frame in frames:
                neon = neon_color(t)
                rendered = "\n".join(frame)
                text.config(text=rendered, fg=neon)
                t += 0.15
                time.sleep(0.12)

    thr = threading.Thread(target=animate, daemon=True)
    thr.start()

    root.mainloop()


run_animation()
