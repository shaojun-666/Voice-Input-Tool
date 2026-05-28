# 语音输入助手

一个基于百度语音识别 API 的语音转文字工具，支持全局快捷键调用，识别结果自动粘贴到当前光标位置。

## 功能特性

- **语音识别**：使用百度语音识别 API，支持中文语音转文字
- **全局快捷键**：可在任意应用程序中使用快捷键触发录音
- **自动输入**：识别结果自动粘贴到当前光标位置
- **自定义快捷键**：支持用户自定义触发快捷键
- **GUI 界面**：简洁的图形界面，方便设置和启动

## 系统要求

- Windows 操作系统
- Python 3.7+（如需运行源码）
- 麦克风设备

## 安装

### 方式一：直接运行可执行文件

在 `dist/` 目录下找到 `voice_input.exe`，双击运行即可。

### 方式二：从源码运行

1. 克隆或下载本项目

2. 安装依赖：
```bash
pip install speechrecognition pynput pyautogui baidu-aip pyperclip
```

3. 运行程序：
```bash
python voice_input.py
```

## 使用方法

1. 启动程序后，在 GUI 界面中设置快捷键（默认为 `Ctrl+Alt+V`）
2. 点击"启动程序"按钮
3. 在任意应用中按下快捷键开始录音（录音时长约 4 秒）
4. 说话结束后，识别结果会自动粘贴到当前光标位置

### 快捷键说明

| 功能 | 默认快捷键 |
|------|-----------|
| 开始录音 | `Ctrl+Alt+V` |
| 退出程序 | `Ctrl+Shift+Q` |

## 配置

使用前需要在百度 AI 开放平台创建应用，获取 API 密钥：

1. 访问 [百度 AI 开放平台](https://ai.baidu.com/)
2. 创建语音识别应用
3. 获取 `APP_ID`、`API_KEY`、`SECRET_KEY`
4. 在代码中替换相应的配置值

```python
APP_ID = '你的 App ID'
API_KEY = '你的 API Key'
SECRET_KEY = '你的 Secret Key'
```

## 打包说明

使用 PyInstaller 打包为可执行文件：

```bash
pyinstaller voice_input.spec
```

打包后的文件位于 `dist/` 目录。

## 项目结构

```
VoiceInputTool/
├── voice_input.py      # 主程序源码
├── voice_input.spec    # PyInstaller 打包配置
├── build/              # 打包临时目录
├── dist/               # 可执行文件输出目录
│   └── voice_input.exe
└── README.md           # 项目说明文档
```

## 依赖库

- `speech_recognition` - 语音录制
- `pynput` - 全局快捷键监听
- `pyautogui` - 模拟键盘操作
- `baidu-aip` - 百度 AI SDK
- `pyperclip` - 剪贴板操作
- `tkinter` - GUI 界面（Python 内置）

## 注意事项

- 确保麦克风正常工作
- 首次使用需要联网进行语音识别
- 部分安全软件可能会拦截全局快捷键，需添加信任

## 许可证

MIT License
