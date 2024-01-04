import subprocess

def get_device_model():
    try:
        result = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.model'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return "未知设备型号"
    except Exception as e:
        return f"获取设备型号失败：{e}"

