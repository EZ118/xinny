import webview
import os
import sys
import pathlib
def get_datadir():
    data_dir = 'xinny-app'
    home = pathlib.Path.home()
    final_path = ''

    if sys.platform == "win32":
        final_path = home / "AppData/Local" / data_dir
    elif sys.platform == "linux":
        final_path = home / ".local/share" / data_dir
    elif sys.platform == "darwin":
        final_path = home / "Library/Application Support" / data_dir
    else:
        print("Unsupported platform")
        final_path = ''
    
    final_path = str(final_path)

    if not os.path.exists(final_path):
        os.makedirs(final_path)
    
    return final_path

user_data_path = get_datadir()

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
