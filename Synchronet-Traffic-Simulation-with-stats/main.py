# Entry point for the browser build (pygbag looks for main.py).
# On desktop you can run either this file or simulation.py.
import asyncio

import pygame  # noqa: F401 -- pygbag only loads packages imported here

from simulation import main

asyncio.run(main())
