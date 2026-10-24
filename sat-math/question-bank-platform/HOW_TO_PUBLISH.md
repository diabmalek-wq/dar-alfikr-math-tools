# Publish SAT Aceit (free)
Folder `site/`: `index.html` = question bank + exam builder, `exam1/index.html` = the 44-question exam.
Both are blocked from search engines (robots.txt, noindex). Delete those two lines/files to allow Google.

## Easiest: Cloudflare Pages (drag and drop)
1. Sign up free at dash.cloudflare.com, then Workers & Pages > Create > Pages > Upload assets.
2. Name the project (e.g. `aceit`), drag the `site` folder, Deploy.
3. Link: https://aceit.pages.dev  (exam 1: /exam1/)

## Alternative: Netlify Drop
app.netlify.com/drop: drag the `site` folder. You get a random link, rename it in Site settings.

## Own domain later
Buy a domain, then Pages > Custom domains > add `aceit.yourname.com` and follow the DNS prompt.

## Before sharing widely
- Desmos: the built page needs a Desmos API key (pass it to build.py). For a public or paid site, request your own key from Desmos and set DESMOS_API_KEY when running build.py.
- Answer keys are inside the page, so this is for practice, not graded exams.

## Exam integrity (proctoring)
The builder has an **Exam integrity** section (on by default for Full mock, One module and Hard only; off for Topic drill).
- **Proctor mode**: the exam goes fullscreen; switching tab, minimising, clicking outside the window or leaving fullscreen is a "leave". Each leave shows a warning and is logged. Copy, cut, paste, right-click, drag, print and common dev-tool shortcuts are blocked (Desmos and the answer box still work).
- **Auto-submit on leave number N** (default 3rd): the exam is submitted, unanswered questions count as incorrect, and the report is flagged. Choose "Never" to only warn and report.
- **Integrity report** on the results page: leaves, time away, blocked actions, fullscreen/SEB status and a log of each leave. "Copy report" puts it on the clipboard so the student can send it to the teacher. The student can type a name on the start page.
- The settings travel with the exam link (`#x=`) and the downloaded single-exam file.

A web page cannot block other apps or websites and cannot see other devices, so this detects and records. It is a deterrent, not a lock.

### Real lock: Safe Exam Browser (free)
1. Install SEB (safeexambrowser.org) on the lab computers or iPads.
2. Open the SEB Config Tool, set **Start URL** to your exam link (for example `https://acesat.pages.dev/#x=...`), and on the *Browser* tab restrict navigation to that site only.
3. Save the `.seb` file, give it to students, and open it on their machine. Tick **Require Safe Exam Browser** in the builder so a normal browser cannot start the exam. The page checks the SEB user agent. This is a convenience check, not tamper-proof; use SEB's own Browser Exam Key for strict control.
4. Inside SEB the page does not force fullscreen (SEB already does) but still records leaves.

### Chromebooks
Use a managed Chromebook kiosk or single-app mode (Google Admin console) with the exam link as the only allowed page.

### Limits
Phones and second devices cannot be seen by any web page. Keep in-person supervision for graded exams.
