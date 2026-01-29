# fix_connection.py - 修复插件连接问题（在舍友电脑上运行）
import json
import os

# 这里的IP要改成你的真实IP
SERVER_IP = "10.129.79.124"  # 修改为你的IP

ext_dir = os.path.dirname(os.path.abspath(__file__))

# 1. 修复 constants.js
constants_path = os.path.join(ext_dir, "content", "constants.js")
if os.path.exists(constants_path):
    with open(constants_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 强制替换所有可能的地址
    content = content.replace("localhost:3000", f"{SERVER_IP}:3000")
    content = content.replace("127.0.0.1:3000", f"{SERVER_IP}:3000")
    
    with open(constants_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ constants.js 已修复")

# 2. 修复 popup.js（如果有）
popup_js_path = os.path.join(ext_dir, "popup", "popup.js")
if os.path.exists(popup_js_path):
    with open(popup_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("localhost:3000", f"{SERVER_IP}:3000")
    
    with open(popup_js_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ popup.js 已修复")

# 3. 修复 manifest.json（关键！添加权限）
manifest_path = os.path.join(ext_dir, "manifest.json")
if os.path.exists(manifest_path):
    with open(manifest_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 确保你的IP在权限列表中
    host_perms = data.get('host_permissions', [])
    required = f"http://{SERVER_IP}:3000/*"
    
    if required not in host_perms:
        host_perms.append(required)
        data['host_permissions'] = host_perms
        
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("✅ manifest.json 已添加权限")

print("\n🔄 修复完成！请按以下步骤操作：")
print("1. 关闭Chrome（整个浏览器，不只是标签页）")
print("2. 重新打开Chrome")
print("3. 进入 chrome://extensions/")
print("4. 找到'B站广告跳过'插件，点击'刷新'按钮（↻）")
print("5. 点击插件图标测试登录")
print(f"\n如果还是不行，在插件图标上右键 → 检查弹出内容 → Console 看报错")
input("\n按回车退出...")