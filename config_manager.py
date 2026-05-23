import json

def load_config(filename):
    with open(filename) as f:
        # 用 json.load 读取并返回
        return json.load(f)

def save_config(config, filename):
    with open(filename, "w") as f:
        # 用 json.dump 写入，加 indent=2
        json.dump(config, f, indent=2)

def update_config(config):
    print("Current settings:")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    key = input("\nWhich setting to update? ")
    
    if key not in config:
        print("Setting not found.")
        return config
    
    value = input(f"New value for {key}: ")
    
    # 数据验证：如果 key 是 font_size
    # 把 value 转成整数
    # 检查是否在 8 到 32 之间
    # 如果不在范围内，打印错误提示并 return config 不保存
    
    if key == "font_size":
        try:
            value = int(value)
            if not (8 <= value <= 32):
                print("Font size must be between 8 and 32.")
                return config
        except ValueError:
            print("Invalid font size. Please enter a number.")
            return config

    config[key] = value
    return config

config = load_config("config.json")
config = update_config(config)
save_config(config, "config.json")
print("Saved!")       