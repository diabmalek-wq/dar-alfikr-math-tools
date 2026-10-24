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
