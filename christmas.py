#!/usr/bin/env python3
import random

# Colors
red = '\033[31m'
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

# Formatting
bold = "\033[1m"
underline = "\033[4m"
end = "\033[0m"

# http://patorjk.com/software/taag/
merry = """
███╗   ███╗███████╗██████╗ ██████╗ ██╗   ██╗
████╗ ████║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
██╔████╔██║█████╗  ██████╔╝██████╔╝ ╚████╔╝ 
██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝  
██║ ╚═╝ ██║███████╗██║  ██║██║  ██║   ██║   
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
"""
christmas = """
 ██████╗██╗  ██╗██████╗ ██╗███████╗████████╗███╗   ███╗ █████╗ ███████╗
██╔════╝██║  ██║██╔══██╗██║██╔════╝╚══██╔══╝████╗ ████║██╔══██╗██╔════╝
██║     ███████║██████╔╝██║███████╗   ██║   ██╔████╔██║███████║███████╗
██║     ██╔══██║██╔══██╗██║╚════██║   ██║   ██║╚██╔╝██║██╔══██║╚════██║
╚██████╗██║  ██║██║  ██║██║███████║   ██║   ██║ ╚═╝ ██║██║  ██║███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
"""

# https://github.com/angelofallars/treefetch
tree = f"""
{green}       /\\
{green}      /\*\\
{green}     /\{red}O{green}\*\\
{green}    /*/\/\/\\
{green}   /\{red}O{green}\/\{blue}O{green}\/\\
{green}  /\*\/\*\/\/\\
{green}  |{blue}O{green}\/\/*/\/{blue}O{green}|
       {yellow}||
       {yellow}||
"""

# https://ascii.co.uk/art/christmas
tree1 = """
         ,' `  
        /.o `,    
        `, |-`,   
       -',    '   
      `,'_)   '\  
     ,'    `-`,  
     _`o,-   (_)/ 
     '_ '    o  `-,
    /   ,-L   `-' 
  _`-`_     ,  `'.
 ;.  (,'  `| `.-. \\
   ,``_'    (_)  o `'
 ,` '_  ,|\   o   _ \ 
/..-(_)' |','..-`(_)-`
         |  |        
       --'  `--
"""

# https://ascii.co.uk/art/snowflakes
snowflake = """
      /\\
 __   \/   __
 \_\_\/\/_/_/
   _\_\/_/_
  __/_/\_\__
 /_/ /\/\ \_\\
      /\\
      \/
"""

merry_christmas = f"{red}{merry}{green}{christmas}"
tree = f"{bold}{tree}"
tree1 = f"{green}{bold}{tree1}"
snowflake = f"{bold}{cyan}{snowflake}"

choices = [merry_christmas, tree, tree1, snowflake]
print(random.choice(choices), end='')