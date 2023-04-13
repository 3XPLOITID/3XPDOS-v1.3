"""This module provides a function that prints the logo's application."""

import os

from colorama import Fore as F


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
    logo = """
    
 .d8888b. Y88b   d88P8888888b. 8888888b.  .d88888b.  .d8888b.  
d88P  Y88b Y88b d88P 888   Y88b888  "Y88bd88P" "Y88bd88P  Y88b 
     .d88P  Y88o88P  888    888888    888888     888Y88b.      
    8888"    Y888P   888   d88P888    888888     888 "Y888b.   
     "Y8b.   d888b   8888888P" 888    888888     888    "Y88b. 
888    888  d88888b  888       888    888888     888      "888 
Y88b  d88P d88P Y88b 888       888  .d88PY88b. .d88PY88b  d88P 
 "Y8888P" d88P   Y88b888       8888888P"  "Y88888P"  "Y8888P"  

GREATZ ALL MEMBER COD-3X AND 3XP.OFC
  """

    print(f"{F.RED}{logo}")
    print("├─── DOS TOOL")
    print("├─── AVAILABLE METHODS")
    print("├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
    if os.name != "nt":
        print("├─── LAYER 4: SYN-FLOOD")
        print("├─── LAYER 2: ARP-SPOOF | DISCONNECT")
    print("├───┐")
