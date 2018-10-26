import re

example_str = "gorodetskiykp-1982@gmail.inbox.com; https://vk.com/python_korolev"

print(re.findall(r'[\w-]+@[\w\.]+\.\w{2,4}', example_str))
