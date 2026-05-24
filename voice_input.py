import speech_recognition as sr
from pynput import keyboard
import pyautogui
import threading
from aip import AipSpeech
import os
import sys
import pyperclip  # 剪贴板操作
import asyncio   # 异步处理

# ==================== 百度语音识别配置 ====================
APP_ID = '122074865'         # 替换为你的百度 App ID
API_KEY = 'qccNshss5o0ypEaSEXKolIRw'       # 替换为你的百度 API Key
SECRET_KEY = 'R0bVQyLcolZ9Z0P8z0xgjnsq1Ob5qS36' # 替换为你的百度 Secret Key

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# ==================== 日志记录函数 ====================
def log(message):
    print(f"[LOG] {message}")

# ==================== 语音识别函数（修复版） ====================
async def recognize_speech_baidu():
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone(sample_rate=16000) as source:
            log("开始录音...")
            # 延长录音时间为 4 秒
            audio = recognizer.listen(source, phrase_time_limit=4)

        temp_audio_path = "temp.wav"
        with open(temp_audio_path, "wb") as f:
            f.write(audio.get_wav_data(convert_rate=16000, convert_width=2))

        try:
            with open(temp_audio_path, "rb") as f:
                result = client.asr(f.read(), 'wav', 16000, {'dev_pid': 1537})
        except Exception as e:
            log(f"调用百度 API 失败: {e}")
            os.remove(temp_audio_path)
            return

        os.remove(temp_audio_path)

        if result['err_no'] == 0:
            text = result['result'][0]
            log(f"识别结果: {text}")
            # 使用剪贴板插入文本
            pyperclip.copy(text)
            pyautogui.hotkey('ctrl', 'v')
        else:
            log(f"识别失败: {result['err_msg']}")
    except Exception as e:
        log(f"语音识别过程中发生错误: {e}")

# ==================== 快捷键回调函数 ====================
is_listening = False

def on_activate():
    global is_listening
    if not is_listening:
        is_listening = True
        # 在新线程中运行异步任务，避免阻塞主线程
        thread = threading.Thread(target=lambda: asyncio.run(recognize_speech_baidu()))
        thread.daemon = True  # 设置为守护线程
        thread.start()
        is_listening = False

# ==================== 退出程序函数 ====================
def exit_program():
    log("程序正在退出...")
    sys.exit(0)

# ==================== 全局快捷键监听 ====================
def start_hotkey_listener(hotkey='<ctrl>+<alt>+v', exit_key='<ctrl>+<shift>+q'):
    log(f"监听快捷键: {hotkey} | 退出快捷键: {exit_key}")
    with keyboard.GlobalHotKeys({
        hotkey: on_activate,
        exit_key: exit_program
    }) as h:
        h.join()

# ==================== GUI 界面 ====================
def create_gui():
    def start_program():
        hotkey = entry_hotkey.get()
        if not hotkey:
            messagebox.showerror("错误", "请输入快捷键组合！")
            return
        messagebox.showinfo("提示", f"程序已启动，快捷键为: {hotkey}\n退出快捷键: Ctrl+Shift+Q")
        root.destroy()
        start_hotkey_listener(hotkey)

    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.title("语音输入助手")
    root.geometry("300x150")

    label_title = tk.Label(root, text="语音输入助手", font=("Arial", 14))
    label_title.pack(pady=10)

    label_hotkey = tk.Label(root, text="设置快捷键（例如 <ctrl>+<alt>+v）:")
    label_hotkey.pack()

    entry_hotkey = tk.Entry(root, width=30)
    entry_hotkey.insert(0, "<ctrl>+<alt>+v")
    entry_hotkey.pack(pady=5)

    button_start = tk.Button(root, text="启动程序", command=start_program)
    button_start.pack(pady=10)

    root.mainloop()

# ==================== 主程序入口 ====================
if __name__ == "__main__":
    log("程序初始化中...")
    create_gui()