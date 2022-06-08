# Github: https://github.com/beh185
# Telegram: https://T.me/dr_xz
# e-mail: BehnamH.dev@gmail.com
# ____________________________________________

# import part
from random import choice 
from os import system, name
cleaner = '\033[0m'

# colors
colors = ["\u001b[38;5;1m", 
    "\u001b[38;5;2m", 
    "\u001b[38;5;3m", 
    "\u001b[38;5;4m", 
    "\u001b[38;5;5m", 
    "\u001b[38;5;6m", 
    "\u001b[38;5;7m", 
    "\u001b[38;5;8m", 
    "\u001b[38;5;9m", 
    "\u001b[38;5;10m", 
    "\u001b[38;5;11m", 
    "\u001b[38;5;12m", 
    "\u001b[38;5;13m", 
    "\u001b[38;5;14m", 
    "\u001b[38;5;15m", 
    "\u001b[38;5;16m", 
    "\u001b[38;5;17m", 
    "\u001b[38;5;18m", 
    "\u001b[38;5;19m", 
    "\u001b[38;5;20m", 
    "\u001b[38;5;21m", 
    "\u001b[38;5;22m", 
    "\u001b[38;5;23m", 
    "\u001b[38;5;24m", 
    "\u001b[38;5;25m", 
    "\u001b[38;5;26m", 
    "\u001b[38;5;27m", 
    "\u001b[38;5;28m", 
    "\u001b[38;5;29m", 
    "\u001b[38;5;30m", 
    "\u001b[38;5;31m", 
    "\u001b[38;5;32m", 
    "\u001b[38;5;33m", 
    "\u001b[38;5;34m", 
    "\u001b[38;5;35m", 
    "\u001b[38;5;36m", 
    "\u001b[38;5;37m", 
    "\u001b[38;5;38m", 
    "\u001b[38;5;39m", 
    "\u001b[38;5;40m", 
    "\u001b[38;5;41m", 
    "\u001b[38;5;42m", 
    "\u001b[38;5;43m", 
    "\u001b[38;5;44m", 
    "\u001b[38;5;45m", 
    "\u001b[38;5;46m", 
    "\u001b[38;5;47m", 
    "\u001b[38;5;48m", 
    "\u001b[38;5;49m", 
    "\u001b[38;5;50m", 
    "\u001b[38;5;51m", 
    "\u001b[38;5;52m", 
    "\u001b[38;5;53m", 
    "\u001b[38;5;54m", 
    "\u001b[38;5;55m", 
    "\u001b[38;5;56m", 
    "\u001b[38;5;57m", 
    "\u001b[38;5;58m", 
    "\u001b[38;5;59m", 
    "\u001b[38;5;60m", 
    "\u001b[38;5;61m", 
    "\u001b[38;5;62m", 
    "\u001b[38;5;63m", 
    "\u001b[38;5;64m", 
    "\u001b[38;5;65m", 
    "\u001b[38;5;66m", 
    "\u001b[38;5;67m", 
    "\u001b[38;5;68m", 
    "\u001b[38;5;69m", 
    "\u001b[38;5;70m", 
    "\u001b[38;5;71m", 
    "\u001b[38;5;72m", 
    "\u001b[38;5;73m", 
    "\u001b[38;5;74m", 
    "\u001b[38;5;75m", 
    "\u001b[38;5;76m", 
    "\u001b[38;5;77m", 
    "\u001b[38;5;78m", 
    "\u001b[38;5;79m", 
    "\u001b[38;5;80m", 
    "\u001b[38;5;81m", 
    "\u001b[38;5;82m", 
    "\u001b[38;5;83m", 
    "\u001b[38;5;84m", 
    "\u001b[38;5;85m", 
    "\u001b[38;5;86m", 
    "\u001b[38;5;87m", 
    "\u001b[38;5;88m", 
    "\u001b[38;5;89m", 
    "\u001b[38;5;90m", 
    "\u001b[38;5;91m", 
    "\u001b[38;5;92m", 
    "\u001b[38;5;93m", 
    "\u001b[38;5;94m", 
    "\u001b[38;5;95m", 
    "\u001b[38;5;96m", 
    "\u001b[38;5;97m", 
    "\u001b[38;5;98m", 
    "\u001b[38;5;99m", 
    "\u001b[38;5;100m", 
    "\u001b[38;5;101m", 
    "\u001b[38;5;102m", 
    "\u001b[38;5;103m", 
    "\u001b[38;5;104m", 
    "\u001b[38;5;105m", 
    "\u001b[38;5;106m", 
    "\u001b[38;5;107m", 
    "\u001b[38;5;108m", 
    "\u001b[38;5;109m", 
    "\u001b[38;5;110m", 
    "\u001b[38;5;111m", 
    "\u001b[38;5;112m", 
    "\u001b[38;5;113m", 
    "\u001b[38;5;114m", 
    "\u001b[38;5;115m", 
    "\u001b[38;5;116m", 
    "\u001b[38;5;117m", 
    "\u001b[38;5;118m", 
    "\u001b[38;5;119m", 
    "\u001b[38;5;120m", 
    "\u001b[38;5;121m", 
    "\u001b[38;5;122m", 
    "\u001b[38;5;123m", 
    "\u001b[38;5;124m", 
    "\u001b[38;5;125m", 
    "\u001b[38;5;126m", 
    "\u001b[38;5;127m", 
    "\u001b[38;5;128m", 
    "\u001b[38;5;129m", 
    "\u001b[38;5;130m", 
    "\u001b[38;5;131m", 
    "\u001b[38;5;132m", 
    "\u001b[38;5;133m", 
    "\u001b[38;5;134m", 
    "\u001b[38;5;135m", 
    "\u001b[38;5;136m", 
    "\u001b[38;5;137m", 
    "\u001b[38;5;138m", 
    "\u001b[38;5;139m", 
    "\u001b[38;5;140m", 
    "\u001b[38;5;141m", 
    "\u001b[38;5;142m", 
    "\u001b[38;5;143m", 
    "\u001b[38;5;144m", 
    "\u001b[38;5;145m", 
    "\u001b[38;5;146m", 
    "\u001b[38;5;147m", 
    "\u001b[38;5;148m", 
    "\u001b[38;5;149m", 
    "\u001b[38;5;150m", 
    "\u001b[38;5;151m", 
    "\u001b[38;5;152m", 
    "\u001b[38;5;153m", 
    "\u001b[38;5;154m", 
    "\u001b[38;5;155m", 
    "\u001b[38;5;156m", 
    "\u001b[38;5;157m", 
    "\u001b[38;5;158m", 
    "\u001b[38;5;159m", 
    "\u001b[38;5;160m", 
    "\u001b[38;5;161m", 
    "\u001b[38;5;162m", 
    "\u001b[38;5;163m", 
    "\u001b[38;5;164m", 
    "\u001b[38;5;165m", 
    "\u001b[38;5;166m", 
    "\u001b[38;5;167m", 
    "\u001b[38;5;168m", 
    "\u001b[38;5;169m", 
    "\u001b[38;5;170m", 
    "\u001b[38;5;171m", 
    "\u001b[38;5;172m", 
    "\u001b[38;5;173m", 
    "\u001b[38;5;174m", 
    "\u001b[38;5;175m", 
    "\u001b[38;5;176m", 
    "\u001b[38;5;177m", 
    "\u001b[38;5;178m", 
    "\u001b[38;5;179m", 
    "\u001b[38;5;180m", 
    "\u001b[38;5;181m", 
    "\u001b[38;5;182m", 
    "\u001b[38;5;183m", 
    "\u001b[38;5;184m", 
    "\u001b[38;5;185m", 
    "\u001b[38;5;186m", 
    "\u001b[38;5;187m", 
    "\u001b[38;5;188m", 
    "\u001b[38;5;189m", 
    "\u001b[38;5;190m", 
    "\u001b[38;5;191m", 
    "\u001b[38;5;192m", 
    "\u001b[38;5;193m", 
    "\u001b[38;5;194m", 
    "\u001b[38;5;195m", 
    "\u001b[38;5;196m", 
    "\u001b[38;5;197m", 
    "\u001b[38;5;198m", 
    "\u001b[38;5;199m", 
    "\u001b[38;5;200m", 
    "\u001b[38;5;201m", 
    "\u001b[38;5;202m", 
    "\u001b[38;5;203m", 
    "\u001b[38;5;204m", 
    "\u001b[38;5;205m", 
    "\u001b[38;5;206m", 
    "\u001b[38;5;207m", 
    "\u001b[38;5;208m", 
    "\u001b[38;5;209m", 
    "\u001b[38;5;210m", 
    "\u001b[38;5;211m", 
    "\u001b[38;5;212m", 
    "\u001b[38;5;213m", 
    "\u001b[38;5;214m", 
    "\u001b[38;5;215m", 
    "\u001b[38;5;216m", 
    "\u001b[38;5;217m", 
    "\u001b[38;5;218m", 
    "\u001b[38;5;219m", 
    "\u001b[38;5;220m", 
    "\u001b[38;5;221m", 
    "\u001b[38;5;222m", 
    "\u001b[38;5;223m", 
    "\u001b[38;5;224m", 
    "\u001b[38;5;225m", 
    "\u001b[38;5;226m", 
    "\u001b[38;5;227m", 
    "\u001b[38;5;228m", 
    "\u001b[38;5;229m", 
    "\u001b[38;5;230m", 
    "\u001b[38;5;231m", 
    "\u001b[38;5;232m", 
    "\u001b[38;5;233m", 
    "\u001b[38;5;234m", 
    "\u001b[38;5;235m", 
    "\u001b[38;5;236m", 
    "\u001b[38;5;237m", 
    "\u001b[38;5;238m", 
    "\u001b[38;5;239m", 
    "\u001b[38;5;240m", 
    "\u001b[38;5;241m", 
    "\u001b[38;5;242m", 
    "\u001b[38;5;243m", 
    "\u001b[38;5;244m", 
    "\u001b[38;5;245m", 
    "\u001b[38;5;246m", 
    "\u001b[38;5;247m", 
    "\u001b[38;5;248m", 
    "\u001b[38;5;249m", 
    "\u001b[38;5;250m", 
    "\u001b[38;5;251m", 
    "\u001b[38;5;252m", 
    "\u001b[38;5;253m", 
    "\u001b[38;5;254m", 
    "\u001b[38;5;255m"]

Windows_color = ["\033[30m", 
    "\033[31m", 
    "\033[32m", 
    "\033[33m", 
    "\033[34m", 
    "\033[35m", 
    "\033[36m", 
    "\033[37m", 
    "\033[90m", 
    "\033[91m", 
    "\033[92m", 
    "\033[93m", 
    "\033[94m", 
    "\033[95m", 
    "\033[96m"
    ]

background_color = ["\u001b[48;5;1m", 
    "\u001b[48;5;2m", 
    "\u001b[48;5;3m", 
    "\u001b[48;5;4m", 
    "\u001b[48;5;5m", 
    "\u001b[48;5;6m", 
    "\u001b[48;5;7m", 
    "\u001b[48;5;8m", 
    "\u001b[48;5;9m", 
    "\u001b[48;5;10m", 
    "\u001b[48;5;11m", 
    "\u001b[48;5;12m", 
    "\u001b[48;5;13m", 
    "\u001b[48;5;14m", 
    "\u001b[48;5;15m", 
    "\u001b[48;5;16m", 
    "\u001b[48;5;17m", 
    "\u001b[48;5;18m", 
    "\u001b[48;5;19m", 
    "\u001b[48;5;20m", 
    "\u001b[48;5;21m", 
    "\u001b[48;5;22m", 
    "\u001b[48;5;23m", 
    "\u001b[48;5;24m", 
    "\u001b[48;5;25m", 
    "\u001b[48;5;26m", 
    "\u001b[48;5;27m", 
    "\u001b[48;5;28m", 
    "\u001b[48;5;29m", 
    "\u001b[48;5;30m", 
    "\u001b[48;5;31m", 
    "\u001b[48;5;32m", 
    "\u001b[48;5;33m", 
    "\u001b[48;5;34m", 
    "\u001b[48;5;35m", 
    "\u001b[48;5;36m", 
    "\u001b[48;5;37m", 
    "\u001b[48;5;38m", 
    "\u001b[48;5;39m", 
    "\u001b[48;5;40m", 
    "\u001b[48;5;41m", 
    "\u001b[48;5;42m", 
    "\u001b[48;5;43m", 
    "\u001b[48;5;44m", 
    "\u001b[48;5;45m", 
    "\u001b[48;5;46m", 
    "\u001b[48;5;47m", 
    "\u001b[48;5;48m", 
    "\u001b[48;5;49m", 
    "\u001b[48;5;50m", 
    "\u001b[48;5;51m", 
    "\u001b[48;5;52m", 
    "\u001b[48;5;53m", 
    "\u001b[48;5;54m", 
    "\u001b[48;5;55m", 
    "\u001b[48;5;56m", 
    "\u001b[48;5;57m", 
    "\u001b[48;5;58m", 
    "\u001b[48;5;59m", 
    "\u001b[48;5;60m", 
    "\u001b[48;5;61m", 
    "\u001b[48;5;62m", 
    "\u001b[48;5;63m", 
    "\u001b[48;5;64m", 
    "\u001b[48;5;65m", 
    "\u001b[48;5;66m", 
    "\u001b[48;5;67m", 
    "\u001b[48;5;68m", 
    "\u001b[48;5;69m", 
    "\u001b[48;5;70m", 
    "\u001b[48;5;71m", 
    "\u001b[48;5;72m", 
    "\u001b[48;5;73m", 
    "\u001b[48;5;74m", 
    "\u001b[48;5;75m", 
    "\u001b[48;5;76m", 
    "\u001b[48;5;77m", 
    "\u001b[48;5;78m", 
    "\u001b[48;5;79m", 
    "\u001b[48;5;80m", 
    "\u001b[48;5;81m", 
    "\u001b[48;5;82m", 
    "\u001b[48;5;83m", 
    "\u001b[48;5;84m", 
    "\u001b[48;5;85m", 
    "\u001b[48;5;86m", 
    "\u001b[48;5;87m", 
    "\u001b[48;5;88m", 
    "\u001b[48;5;89m", 
    "\u001b[48;5;90m", 
    "\u001b[48;5;91m", 
    "\u001b[48;5;92m", 
    "\u001b[48;5;93m", 
    "\u001b[48;5;94m", 
    "\u001b[48;5;95m", 
    "\u001b[48;5;96m", 
    "\u001b[48;5;97m", 
    "\u001b[48;5;98m", 
    "\u001b[48;5;99m", 
    "\u001b[48;5;100m", 
    "\u001b[48;5;101m", 
    "\u001b[48;5;102m", 
    "\u001b[48;5;103m", 
    "\u001b[48;5;104m", 
    "\u001b[48;5;105m", 
    "\u001b[48;5;106m", 
    "\u001b[48;5;107m", 
    "\u001b[48;5;108m", 
    "\u001b[48;5;109m", 
    "\u001b[48;5;110m", 
    "\u001b[48;5;111m", 
    "\u001b[48;5;112m", 
    "\u001b[48;5;113m", 
    "\u001b[48;5;114m", 
    "\u001b[48;5;115m", 
    "\u001b[48;5;116m", 
    "\u001b[48;5;117m", 
    "\u001b[48;5;118m", 
    "\u001b[48;5;119m", 
    "\u001b[48;5;120m", 
    "\u001b[48;5;121m", 
    "\u001b[48;5;122m", 
    "\u001b[48;5;123m", 
    "\u001b[48;5;124m", 
    "\u001b[48;5;125m", 
    "\u001b[48;5;126m", 
    "\u001b[48;5;127m", 
    "\u001b[48;5;128m", 
    "\u001b[48;5;129m", 
    "\u001b[48;5;130m", 
    "\u001b[48;5;131m", 
    "\u001b[48;5;132m", 
    "\u001b[48;5;133m", 
    "\u001b[48;5;134m", 
    "\u001b[48;5;135m", 
    "\u001b[48;5;136m", 
    "\u001b[48;5;137m", 
    "\u001b[48;5;138m", 
    "\u001b[48;5;139m", 
    "\u001b[48;5;140m", 
    "\u001b[48;5;141m", 
    "\u001b[48;5;142m", 
    "\u001b[48;5;143m", 
    "\u001b[48;5;144m", 
    "\u001b[48;5;145m", 
    "\u001b[48;5;146m", 
    "\u001b[48;5;147m", 
    "\u001b[48;5;148m", 
    "\u001b[48;5;149m", 
    "\u001b[48;5;150m", 
    "\u001b[48;5;151m", 
    "\u001b[48;5;152m", 
    "\u001b[48;5;153m", 
    "\u001b[48;5;154m", 
    "\u001b[48;5;155m", 
    "\u001b[48;5;156m", 
    "\u001b[48;5;157m", 
    "\u001b[48;5;158m", 
    "\u001b[48;5;159m", 
    "\u001b[48;5;160m", 
    "\u001b[48;5;161m", 
    "\u001b[48;5;162m", 
    "\u001b[48;5;163m", 
    "\u001b[48;5;164m", 
    "\u001b[48;5;165m", 
    "\u001b[48;5;166m", 
    "\u001b[48;5;167m", 
    "\u001b[48;5;168m", 
    "\u001b[48;5;169m", 
    "\u001b[48;5;170m", 
    "\u001b[48;5;171m", 
    "\u001b[48;5;172m", 
    "\u001b[48;5;173m", 
    "\u001b[48;5;174m", 
    "\u001b[48;5;175m", 
    "\u001b[48;5;176m", 
    "\u001b[48;5;177m", 
    "\u001b[48;5;178m", 
    "\u001b[48;5;179m", 
    "\u001b[48;5;180m", 
    "\u001b[48;5;181m", 
    "\u001b[48;5;182m", 
    "\u001b[48;5;183m", 
    "\u001b[48;5;184m", 
    "\u001b[48;5;185m", 
    "\u001b[48;5;186m", 
    "\u001b[48;5;187m", 
    "\u001b[48;5;188m", 
    "\u001b[48;5;189m", 
    "\u001b[48;5;190m", 
    "\u001b[48;5;191m", 
    "\u001b[48;5;192m", 
    "\u001b[48;5;193m", 
    "\u001b[48;5;194m", 
    "\u001b[48;5;195m", 
    "\u001b[48;5;196m", 
    "\u001b[48;5;197m", 
    "\u001b[48;5;198m", 
    "\u001b[48;5;199m", 
    "\u001b[48;5;200m", 
    "\u001b[48;5;201m", 
    "\u001b[48;5;202m", 
    "\u001b[48;5;203m", 
    "\u001b[48;5;204m", 
    "\u001b[48;5;205m", 
    "\u001b[48;5;206m", 
    "\u001b[48;5;207m", 
    "\u001b[48;5;208m", 
    "\u001b[48;5;209m", 
    "\u001b[48;5;210m", 
    "\u001b[48;5;211m", 
    "\u001b[48;5;212m", 
    "\u001b[48;5;213m", 
    "\u001b[48;5;214m", 
    "\u001b[48;5;215m", 
    "\u001b[48;5;216m", 
    "\u001b[48;5;217m", 
    "\u001b[48;5;218m", 
    "\u001b[48;5;219m", 
    "\u001b[48;5;220m", 
    "\u001b[48;5;221m", 
    "\u001b[48;5;222m", 
    "\u001b[48;5;223m", 
    "\u001b[48;5;224m", 
    "\u001b[48;5;225m", 
    "\u001b[48;5;226m", 
    "\u001b[48;5;227m", 
    "\u001b[48;5;228m", 
    "\u001b[48;5;229m", 
    "\u001b[48;5;230m", 
    "\u001b[48;5;231m", 
    "\u001b[48;5;232m", 
    "\u001b[48;5;233m", 
    "\u001b[48;5;234m", 
    "\u001b[48;5;235m", 
    "\u001b[48;5;236m", 
    "\u001b[48;5;237m", 
    "\u001b[48;5;238m", 
    "\u001b[48;5;239m", 
    "\u001b[48;5;240m", 
    "\u001b[48;5;241m", 
    "\u001b[48;5;242m", 
    "\u001b[48;5;243m", 
    "\u001b[48;5;244m", 
    "\u001b[48;5;245m", 
    "\u001b[48;5;246m", 
    "\u001b[48;5;247m", 
    "\u001b[48;5;248m", 
    "\u001b[48;5;249m", 
    "\u001b[48;5;250m", 
    "\u001b[48;5;251m", 
    "\u001b[48;5;252m", 
    "\u001b[48;5;253m", 
    "\u001b[48;5;254m", 
    "\u001b[48;5;255m"]

Windows_background = ["\033[100m",
                      "\033[101m",
                      "\033[102m",
                      "\033[103m",
                      "\033[104m",
                      "\033[105m",
                      "\033[106m",
                      "\033[107m", ]

style1 = ['\033[1m',
         '\033[2m',
         '\033[3m',
         '\033[4m',]
# random color
def color (user_input):
    user_input = str(user_input)
    random_color = choice(colors)
    return random_color + user_input + cleaner

# random background color
def background (user_input):
    user_input = str(user_input)
    random_color = choice(background_color)
    return random_color + user_input + cleaner

# random Windows color
def windows_color(user_input):
    from colorama import init
    init()
    user_input = str(user_input)
    random_color = choice(Windows_color)
    return random_color + user_input + cleaner

# random Windows background color
def windows_background(user_input): 
    from colorama import init
    init()
    user_input = str(user_input)
    random_color = choice(Windows_background)
    return random_color + user_input + cleaner

# random style
def style(user_input):
    user_input = str(user_input)
    random_style = choice(style1)
    return random_style + user_input + cleaner

# Automatically detects the operating system and return the correct color
def auto_color(user_input):
    if name == 'nt':
        return windows_color(user_input)
    else:
        return color(user_input)

# Automatically detects the operating system and return the correct background color
def auto_background(user_input):
    if name == 'nt':
        return windows_background(user_input)
    else:
        return background(user_input)

# return random color and background color
def color_background (user_input):
    return auto_color(auto_background(user_input))

# return random color and style
def color_style (user_input):
    return auto_color(style(user_input))

# return random background color and style
def background_style (user_input):
    return auto_background(style(user_input))

# return random color and background color and style
def color_background_style (user_input):
    return auto_color(auto_background(style(user_input)))
    