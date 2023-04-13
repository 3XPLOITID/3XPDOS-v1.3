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
    ______  __ ____  ____  ____  _____
  |__  / |/ // __ \/ __ \/ __ \/ ___/
   /_ <|   // /_/ / / / / / / /\__ \
 ___/ /   |/ ____/ /_/ / /_/ /___/ /
/____/_/|_/_/   /_____/\____//____/

GREATZ ALL MEMBER COD-3X & 3XP.OFC
  """

    print(f"{F.BLUE}{logo}")
    print("├─── DOS TOOL")
    print("├─── AVAILABLE METHODS")
    print("├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
    if os.name != "nt":
        print("├─── LAYER 4: SYN-FLOOD")
        print("├─── LAYER 2: ARP-SPOOF | DISCONNECT")
    print("├───┐")
