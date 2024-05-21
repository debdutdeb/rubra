from typing import Callable

import asyncio

def once(function: Callable) -> Callable:
    ran = False
    async def run_once(*args, **kwargs):
        nonlocal ran
        if ran:
            return

        ret = function(*args, **kwargs)
        if asyncio.iscoroutine(ret):
            await ret

        ran = True

    return run_once
