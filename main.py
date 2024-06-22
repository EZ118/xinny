import webview
import os

user_data_path = os.path.join(os.getenv('LOCALAPPDATA'), 'xinny-app')

# 如果目录不存在，创建该目录
if not os.path.exists(user_data_path):
    os.makedirs(user_data_path)

webview.settings['OPEN_DEVTOOLS_IN_DEBUG'] = False
webview.settings['ALLOW_DOWNLOADS'] = True

window = webview.create_window(
    title='Xinny',
    url='./res/index.html',
    width=900,
    height=610,
    resizable=True,    # 固定窗口大小
    text_select=True,   # 禁止选择文字内容
    confirm_close=False,   # 关闭时提示
    background_color='#15171a'
)

webview.start(storage_path=user_data_path, private_mode=False, debug=True)