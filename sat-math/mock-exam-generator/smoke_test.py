#!/usr/bin/env python3
"""Open a built exam in headless Chromium, answer every question, submit both modules and
check there are no script errors and no raw LaTeX ($ or \\) left on screen.
Needs: pip install playwright && playwright install chromium   Usage: python3 smoke_test.py dist/exam.html"""
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

async def main(path):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1400, "height": 800})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto(Path(path).resolve().as_uri())
        await pg.click("#go"); await pg.wait_for_timeout(300)
        raw = 0
        for mod in range(2):
            for k in range(22):
                txt = await pg.evaluate("document.querySelector('#qa').innerText")
                if "$" in txt or "\\" in txt:
                    raw += 1; print(f"RAW LaTeX on module {mod+1} question {k+1}")
                if await pg.query_selector(".opt"): await pg.click(".opt >> nth=0")
                else: await pg.fill("#spr", "3")
                await pg.click("#next")
            await pg.click("#sub")
            if mod == 0: await pg.click("#m2")
        await pg.wait_for_timeout(500)
        body = await pg.evaluate("document.body.innerText")
        ok = not errs and not raw and "EXPECTED MATH SCORE" in body.upper()
        print("errors:", errs, "| raw-LaTeX screens:", raw, "| results page:", "EXPECTED MATH SCORE" in body.upper())
        print("PASS" if ok else "FAIL")
        await b.close(); sys.exit(0 if ok else 1)

asyncio.run(main(sys.argv[1]))
