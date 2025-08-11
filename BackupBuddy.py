import yaml

with open("config.yml") as f:
    config = yaml.safe_load(f)

for k, v in config.items():
    print(f"{k.upper()}={v}")
