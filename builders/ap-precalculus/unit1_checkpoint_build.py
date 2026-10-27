import subprocess, sys

PRE = r"""\documentclass[10pt]{article}
\usepackage[a4paper,left=1.8cm,right=1.8cm,top=3.1cm,bottom=2.2cm,headheight=1.9cm,headsep=0.3cm,footskip=0.9cm]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{xcolor,graphicx,array,booktabs,enumitem,lastpage,pgffor,needspace}
\usepackage[most]{tcolorbox}
\usepackage{fancyhdr}\usepackage{fontspec}\usepackage{microtype}
\definecolor{NAVY}{HTML}{1F3A5F}\definecolor{INK}{HTML}{1A1A1A}\definecolor{TEAL}{HTML}{1A7F8E}
\definecolor{GREY}{HTML}{6B7280}\definecolor{LINE}{HTML}{C7CDD6}\definecolor{SOL}{HTML}{15803D}\definecolor{MAROON}{HTML}{7A1F2B}
\setlength{\parindent}{0pt}\setlength{\parskip}{3pt}\renewcommand{\arraystretch}{1.25}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyhead[L]{\raisebox{-0.5\height}{\includegraphics[height=11mm]{dept_logo.png}}}
\fancyhead[C]{\raisebox{-0.5\height}{\includegraphics[height=15mm]{cognia_badge.png}}}
\fancyhead[R]{\raisebox{-0.5\height}{\includegraphics[height=11mm]{school_logo.png}}}
\fancyfoot[L]{\footnotesize\color{GREY}@@CODE@@}
\fancyfoot[C]{\footnotesize\bfseries\color{NAVY}\textsc{Faith, Righteousness and Wisdom}}
\fancyfoot[R]{\footnotesize\color{GREY}Mr Malek Thiab \textperiodcentered\ Page \thepage\ of \pageref{LastPage}}
\newcommand{\banner}[1]{\vspace{5pt}\par\noindent\begin{tcolorbox}[enhanced,colback=NAVY,colframe=NAVY,boxrule=0pt,arc=2pt,left=6pt,top=1pt,bottom=1pt,nobeforeafter]\color{white}\bfseries\small\MakeUppercase{#1}\end{tcolorbox}\par\nopagebreak\vspace{2pt}}
\newcommand{\worklines}[1]{\par\nopagebreak\foreach \i in {1,...,#1}{\par\vspace{0.62cm}{\color{LINE}\hrule height 0.4pt}}\par\vspace{2pt}}
\newcommand{\qh}[3]{\par\needspace{5\baselineskip}\noindent\textbf{\textcolor{NAVY}{#1}}\hfill{\scriptsize\textcolor{GREY}{\textsc{#2}}\ \ \textbf{[#3]}}\par\nopagebreak}
\newcommand{\pt}[1]{\hfill{\scriptsize\textcolor{GREY}{[#1]}}}
\newcommand{\sol}[1]{\begin{tcolorbox}[enhanced,breakable,colback=SOL!6,colframe=SOL!70!black,boxrule=0.5pt,arc=2pt,left=5pt,right=5pt,top=2pt,bottom=2pt,fonttitle=\bfseries\small,title={Solution and marks}]\small #1\end{tcolorbox}}
\newcommand{\src}[1]{{\scriptsize\textcolor{GREY}{\textit{#1}}}}
\newcommand{\dd}{\mathrm{d}}
\begin{document}
"""

def sub(label, text, pts):
    return r"\par\vspace{2pt}\textbf{%s}\ %s\pt{%s}" % (label, text, pts)

# ------------------------------------------------------------------ student paper
def exam():
    t = PRE.replace("@@CODE@@", r"AP Precalculus Unit 1 Checkpoint")
    t += r"""
\begin{tcolorbox}[enhanced,colback=NAVY!4,colframe=NAVY,boxrule=0.8pt,arc=3pt,top=3pt,bottom=3pt]
{\Large\bfseries\color{NAVY} AP Precalculus \textperiodcentered\ Unit 1 Checkpoint}\\[1pt]
{\large\bfseries Lessons 1.1 to 1.10 \textemdash\ Polynomial and Rational Functions (first ten topics)}\\[3pt]
\begin{tabular}{@{}p{0.17\linewidth}p{0.78\linewidth}@{}}
\textbf{Time} & 50 minutes: Part A (calculator) 30 minutes, then Part B (no calculator) 20 minutes.\\
\textbf{Marks} & 29: Part A 14, Part B 15. Every lettered part is worth 1 mark.\\
\textbf{Rules} & Show the work that leads to each answer. Calculator in radian mode. Unless told otherwise, give decimal approximations to three places after the decimal point and do not round intermediate values. Express limits in limit notation.\\
\textbf{Name / Date} & \rule{6cm}{0.3pt}\ \ \rule{3cm}{0.3pt}\\
\end{tabular}
\end{tcolorbox}
"""
    t += r"\banner{Part A \textperiodcentered\ A graphing calculator is required \textperiodcentered\ 14 marks}" + "\n"

    # Q1 : 2025 Q2
    t += r"\qh{1.}{Rates of change \textperiodcentered\ quadratic model}{6}" + "\n"
    t += r"""A musician released a new song on a streaming service. A streaming service is an online entertainment source that allows users to play music on their computers and mobile devices. Several months later, the musician began using an app (at time $t=0$) that counts the total number of plays for the song since its release. A ``play'' is a single stream of the song on the streaming service. The table gives the total number of plays, in thousands, for selected times $t$ months after the musician began using the app. At $t=0$, the total number of plays was $25$ thousand. At $t=2$, the total number of plays was $30$ thousand. At $t=4$, the total number of plays was $34$ thousand.
\begin{center}\begin{tabular}{|p{6.6cm}|c|c|c|}\hline Months after the musician began using the app & $0$ & $2$ & $4$\\\hline Total number of plays for the song since its release (thousands) & $25$ & $30$ & $34$\\\hline\end{tabular}\end{center}
The total number of plays, in thousands, for the song since its release can be modeled by the function $D$ given by $D(t)=at^{2}+bt+c$, where $D(t)$ is the total number of plays, in thousands, for the song since its release, and $t$ is the number of months after the musician began using the app.
"""
    t += sub("A.", r"(i) Use the given data to write three equations that can be used to find the values for constants $a$, $b$, and $c$ in the expression for $D(t)$.", "1") + r"\worklines{3}"
    t += r"\hspace{1.3em}\textbf{(ii)} Find the values for $a$, $b$, and $c$ as decimal approximations.\pt{1}" + r"\worklines{3}"
    t += sub("B.", r"(i) Use the given data to find the average rate of change of the total number of plays for the song, in thousands per month, from $t=0$ to $t=4$ months. Express your answer as a decimal approximation. Show the computations that lead to your answer.", "1") + r"\worklines{3}"
    t += r"\hspace{1.3em}\textbf{(ii)} Use the average rate of change found in part B (i) to estimate the total number of plays for the song, in thousands, for $t=1.5$ months. Show the work that leads to your answer.\pt{1}" + r"\worklines{3}"
    t += r"\hspace{1.3em}\textbf{(iii)} Let $A_t$ represent the estimate of the total number of plays for the song, in thousands, using the average rate of change found in part B (i). For $A_{1.5}$ found in part B (ii), it can be shown that $A_{1.5}<D(1.5)$. Explain why, in general, $A_t<D(t)$ for all $t$, where $0<t<4$. Your explanation should include a reference to the graph of $D$ and its relationship to $A_t$.\pt{1}" + r"\worklines{4}"
    t += sub("C.", r"The quadratic function model $D$ has exactly one absolute minimum or one absolute maximum. That minimum or maximum can be used to determine a domain restriction for $D$. Based on the context of the problem, explain how that minimum or maximum can be used to determine a boundary for the domain of $D$.", "1") + r"\worklines{4}"
    t += r"\par\src{Source: College Board, AP Precalculus 2025 Free-Response Questions, Question 2. Reproduced for classroom use.}"

    # Q2 : 2024 Q2 B
    t += r"\par\vspace{6pt}\qh{2.}{Rates of change \textperiodcentered\ concavity}{3}" + "\n"
    t += r"""On the initial day of sales ($t=0$) for a new video game, there were $40$ thousand units of the game sold that day. Ninety-one days later ($t=91$), there were $76$ thousand units of the game sold that day.

The number of units of the video game sold on a given day can be modeled by the function $G$ given by $G(t)=a+b\ln(t+1)$, where $G(t)$ is the number of units sold, in thousands, on day $t$ since the initial day of sales.
"""
    t += sub("B.", r"(i) Use the given data to find the average rate of change of the number of units of the video game sold, in thousands per day, from $t=0$ to $t=91$ days. Express your answer as a decimal approximation. Show the computations that lead to your answer.", "1") + r"\worklines{3}"
    t += r"\hspace{1.3em}\textbf{(ii)} Use the average rate of change found in (i) to estimate the number of units of the video game sold, in thousands, on day $t=50$. Show the work that leads to your answer.\pt{1}" + r"\worklines{3}"
    t += r"\hspace{1.3em}\textbf{(iii)} Let $A_t$ represent the estimate of the number of units of the video game sold, in thousands, using the average rate of change found in (i). For $A_{50}$, found in (ii), it can be shown that $A_{50}<G(50)$. Explain why, in general, $A_t<G(t)$ for all $t$, where $0<t<91$.\pt{1}" + r"\worklines{4}"
    t += r"\par\src{Source: College Board, AP Precalculus 2024 Free-Response Questions, Question 2, part B only (parts A and C are Unit 2 content). Reproduced for classroom use.}"

    # Q3 : 2026 Q2 B
    t += r"\par\vspace{6pt}\qh{3.}{Rates of change \textperiodcentered\ concavity}{3}" + "\n"
    t += r"""A person purchased a car at the end of the year 2019 ($t=0$). The car's value decreases over time. At the end of the year 2020 ($t=1$), the car was valued at $27.2$ thousand dollars. At the end of the year 2025 ($t=6$), the car was valued at $14.8$ thousand dollars.

The value of the car can be modeled by the function $V$ given by $V(t)=ab^{t}$, where $V(t)$ is the value of the car, in thousands of dollars, at time $t$, and $t$ is the number of years since the end of 2019.
"""
    t += sub("B.", r"(i) Use the given data to find the average rate of change of the value of the car, in thousands of dollars per year, from $t=1$ to $t=6$ years. Express your answer as a decimal approximation. Show the computations that lead to your answer.", "1") + r"\worklines{3}"
    t += r"\hspace{1.3em}\textbf{(ii)} Use the average rate of change found in part B (i) to estimate the value of the car, in thousands of dollars, at $t=3$ years. Show the work that leads to your answer.\pt{1}" + r"\worklines{3}"
    t += r"\hspace{1.3em}\textbf{(iii)} The average rate of change found in part B (i) can be used to determine the secant line for the graph of $V$ on the interval $1\le t\le 6$. Let $A(t)$ represent the estimate of the value of the car, in thousands of dollars, at time $t$ years, using the secant line. For $A(3)$, found in part B (ii), it can be shown that $A(3)>V(3)$. In general, $A(t)>V(t)$ for all $t$, where $1<t<6$. Use the secant line and the graph of $V$ to explain why this is true.\pt{1}" + r"\worklines{4}"
    t += r"\par\src{Source: College Board, AP Precalculus 2026 Free-Response Questions, Question 2, part B only (parts A and C are Unit 2 content). Reproduced for classroom use.}"

    # Q4 : 2025 Q1 B
    t += r"\par\vspace{6pt}\qh{4.}{Polynomial zeros \textperiodcentered\ end behavior}{2}" + "\n"
    t += r"The function $g$ is given by $g(x)=-0.167x^{3}+x^{2}-1.834$." + "\n"
    t += sub("B.", r"(i) Find all values of $x$, as decimal approximations, for which $g(x)=0$, or indicate that there are no such values.", "1") + r"\worklines{3}"
    t += r"\hspace{1.3em}\textbf{(ii)} Determine the end behavior of $g$ as $x$ increases without bound. Express your answer using the mathematical notation of a limit.\pt{1}" + r"\worklines{3}"
    t += r"\par\src{Source: College Board, AP Precalculus 2025 Free-Response Questions, Question 1, part B only (parts A and C are Unit 2 content). Reproduced for classroom use.}"

    t += r"\par\vspace{4pt}\begin{center}\textbf{\textcolor{NAVY}{End of Part A. Stop and hand in the calculator before Part B.}}\end{center}"

    # PART B
    t += r"\newpage\banner{Part B \textperiodcentered\ No calculator \textperiodcentered\ 15 marks}" + "\n"
    t += r"\par\src{Questions 5 to 7 are original AP-style questions written for this checkpoint by Mr Malek Thiab, because the 2024--2026 official free-response papers contain no question on rational functions or on change in tandem.}" + "\n"

    t += r"\par\vspace{4pt}\qh{5.}{Change in tandem \textperiodcentered\ rate of change}{3}" + "\n"
    t += r"""A cyclist rides along the Jeddah Corniche. The table gives $d(t)$, the distance in kilometres she has travelled from the start, $t$ hours after she set off.
\begin{center}\begin{tabular}{|c|c|c|c|c|c|}\hline $t$ (hours) & $0$ & $1$ & $2$ & $3$ & $4$\\\hline $d(t)$ (km) & $0$ & $12$ & $22$ & $30$ & $36$\\\hline\end{tabular}\end{center}
"""
    t += sub("A.", r"Based on the table, does $d(t)$ increase or decrease as $t$ increases? Justify your answer.", "1") + r"\worklines{2}"
    t += sub("B.", r"Find the average rate of change of $d$ from $t=1$ to $t=3$. Include units.", "1") + r"\worklines{2}"
    t += sub("C.", r"Find the average rate of change of $d$ over each of the four one-hour intervals. Use these values to describe how the rate of change of $d$ is changing, and state the concavity of the graph of $d$ on $0\le t\le 4$.", "1") + r"\worklines{3}"

    t += r"\par\vspace{4pt}\qh{6.}{Polynomial zeros \textperiodcentered\ end behavior}{4}" + "\n"
    t += r"""The polynomial function $p$ has real coefficients and a leading coefficient of $2$. Two of its zeros are $x=3$, with multiplicity $2$, and $x=1-2i$.
"""
    t += sub("A.", r"Explain why $x=1+2i$ must also be a zero of $p$.", "1") + r"\worklines{2}"
    t += sub("B.", r"Assuming $p$ has the least possible degree, state the degree of $p$ and write $p(x)$ as a product of a constant and factors with real coefficients. Do not expand.", "1") + r"\worklines{3}"
    t += sub("C.", r"Describe the end behavior of $p$ as $x$ increases without bound and as $x$ decreases without bound. Use limit notation.", "1") + r"\worklines{3}"
    t += sub("D.", r"Describe the behavior of the graph of $p$ at $x=3$. Justify your answer using the multiplicity of the zero.", "1") + r"\worklines{3}"

    t += r"\par\vspace{6pt}\qh{7.}{Rational functions \textperiodcentered\ zeros, asymptotes, holes, end behavior}{8}" + "\n"
    t += r"The rational function $r$ is given by $r(x)=\dfrac{2x^{2}-2x-12}{x^{2}-9}$." + "\n"
    t += sub("A.", r"(i) Write the numerator and the denominator of $r$ in factored form, and state all values of $x$ that are not in the domain of $r$.", "1") + r"\worklines{3}"
    t += r"\hspace{1.3em}\textbf{(ii)} The graph of $r$ has a hole. Find the coordinates of the hole. Show the work that leads to your answer.\pt{1}" + r"\worklines{3}"
    t += sub("B.", r"(i) Find all zeros of $r$.", "1") + r"\worklines{2}"
    t += r"\hspace{1.3em}\textbf{(ii)} A student claims that $x=3$ is a zero of $r$ because $x-3$ is a factor of the numerator. Is the student correct? Justify your answer.\pt{1}" + r"\worklines{3}"
    t += sub("C.", r"(i) Write the equation of the vertical asymptote of the graph of $r$.", "1") + r"\worklines{2}"
    t += r"\hspace{1.3em}\textbf{(ii)} Determine $\displaystyle\lim_{x\to -3^{-}} r(x)$ and $\displaystyle\lim_{x\to -3^{+}} r(x)$. Use limit notation.\pt{1}" + r"\worklines{3}"
    t += sub("D.", r"(i) Determine $\displaystyle\lim_{x\to\infty} r(x)$. Use limit notation.", "1") + r"\worklines{2}"
    t += r"\hspace{1.3em}\textbf{(ii)} Write the equation of the horizontal asymptote and explain, using the degrees and leading coefficients, why it is the same as $x$ decreases without bound.\pt{1}" + r"\worklines{3}"
    t += r"\par\vspace{4pt}\begin{center}\textbf{\textcolor{NAVY}{End of checkpoint.}}\end{center}\end{document}"
    return t

# ------------------------------------------------------------------ answer key
def key():
    t = PRE.replace("@@CODE@@", r"AP Precalculus Unit 1 Checkpoint: key")
    t += r"""
\begin{tcolorbox}[enhanced,colback=SOL!5,colframe=SOL!70!black,boxrule=0.8pt,arc=3pt,top=3pt,bottom=3pt]
{\Large\bfseries\color{NAVY} AP Precalculus \textperiodcentered\ Unit 1 Checkpoint}\\[1pt]
{\large\bfseries Answer key, marking guide and readiness decision rules \textemdash\ teacher copy}\\[2pt]
{\small Marks below are assigned by the teacher (1 mark per lettered part, 29 in total). They are not College Board scoring guidelines.}
\end{tcolorbox}
"""
    t += r"\banner{1. Source map and coverage}"
    t += r"""
\begin{tabular}{@{}p{1.2cm}p{5.2cm}p{9cm}@{}}
\toprule \textbf{Q} & \textbf{Official source} & \textbf{Lessons tested}\\\midrule
1 & 2025 Q2 (all parts) & 1.2 average rate of change and secant estimate; 1.3 quadratic from three points and its extreme value; 1.4 concavity\\
2 & 2024 Q2 part B & 1.2 average rate of change; 1.4 concave down means secant below the graph\\
3 & 2026 Q2 part B & 1.2 average rate of change; 1.4 concave up means secant above the graph\\
4 & 2025 Q1 part B & 1.5 real zeros by technology; 1.6 polynomial end behavior\\
5--7 & Original (no official source exists) & 1.1 change in tandem; 1.5 complex zeros and multiplicity; 1.6 end behavior; 1.7 to 1.10 rational functions\\\bottomrule
\end{tabular}

\par\vspace{3pt}{\small\textbf{Left out on purpose.} 2024 Q1 and 2025 Q1 parts A and C and 2026 Q1 (composition, inverse functions, exponential and logarithmic models: Unit 2). Part A of 2024 Q2 and 2026 Q2 and part C (exponential and logarithmic modelling and model error: Unit 2). Question 3 (sinusoidal models) and Question 4 (equations and identities) of all three years (Unit 3 and Unit 2). Rational functions (1.7 to 1.10) and change in tandem (1.1) do not appear in any 2024--2026 free-response question, which is why Questions 5 to 7 are original.}
"""
    t += r"\banner{2. Solutions and marks \textemdash\ Part A (calculator)}"

    t += r"\qh{1.}{2025 Q2}{6}"
    t += r"\sol{"
    t += r"""\textbf{A(i)} [1] $D(0)=25$, so $c=25$; $4a+2b+c=30$; $16a+4b+c=34$ (equivalent forms accepted: $a(0)^2+b(0)+c=25$, and so on). \emph{Common error:} writing $D(2)=34$ or substituting $t=30$.\\
\textbf{A(ii)} [1] $a=-0.125$, $b=2.75$, $c=25$ (all three needed). By hand: $4a+2b=5$ and $16a+4b=9$ give $8a=-1$.\\
\textbf{B(i)} [1] $\dfrac{D(4)-D(0)}{4-0}=\dfrac{34-25}{4}=2.25$ thousand plays per month. \emph{Common error:} dividing by $34-25$ or using $t=2$.\\
\textbf{B(ii)} [1] $A_{1.5}=25+2.25(1.5)=28.375$ thousand. \emph{Common error:} evaluating $D(1.5)=28.844$ instead of the secant estimate.\\
\textbf{B(iii)} [1] $a=-0.125<0$, so the graph of $D$ is concave down on $0<t<4$; the secant line through $(0,25)$ and $(4,34)$, which is the graph of $A_t$, lies below the graph of $D$ between the endpoints, so $A_t<D(t)$. Needs concave down and the secant-versus-graph position.\\
\textbf{C} [1] The vertex is at $t=-\dfrac{b}{2a}=11$, with maximum $D(11)=40.125$. After $t=11$ the model decreases, but a running total of plays cannot decrease, so the domain must stop at $t=11$ (that is, $0\le t\le 11$).
"""
    t += r"}"
    t += r"\qh{2.}{2024 Q2 part B}{3}"
    t += r"\sol{\textbf{B(i)} [1] $\dfrac{76-40}{91-0}=\dfrac{36}{91}\approx 0.396$ thousand units per day.\\ \textbf{B(ii)} [1] $A_{50}=40+\dfrac{36}{91}(50)\approx 59.780$ thousand.\\ \textbf{B(iii)} [1] $G(t)=a+b\ln(t+1)$ with $b=\dfrac{36}{\ln 92}>0$ is increasing and concave down (its rate of change is decreasing), so the graph lies above the secant line between $t=0$ and $t=91$; the secant line is $A_t$, so $A_t<G(t)$.}"
    t += r"\qh{3.}{2026 Q2 part B}{3}"
    t += r"\sol{\textbf{B(i)} [1] $\dfrac{14.8-27.2}{6-1}=\dfrac{-12.4}{5}=-2.48$ thousand dollars per year (negative sign required).\\ \textbf{B(ii)} [1] $A(3)=27.2+(-2.48)(3-1)=22.24$ thousand dollars.\\ \textbf{B(iii)} [1] $V(t)=ab^{t}$ with $0<b<1$ ($a\approx 30.721$, $b\approx 0.885$) is decreasing and concave up (the rate of change increases toward $0$), so the graph lies below the secant line on $1<t<6$; the secant line is $A(t)$, so $A(t)>V(t)$. Check: $V(3)\approx 21.323<22.24$.}"
    t += r"\qh{4.}{2025 Q1 part B}{2}"
    t += r"\sol{\textbf{B(i)} [1] $x\approx -1.233$, $x\approx 1.578$, $x\approx 5.643$ (all three needed; graph $y=g(x)$ and read the three $x$-intercepts, or solve numerically). \emph{Common error:} reporting only the positive roots.\\ \textbf{B(ii)} [1] $\displaystyle\lim_{x\to\infty} g(x)=-\infty$. The leading term $-0.167x^{3}$ is negative and odd. Accept ``$g(x)\to-\infty$ as $x\to\infty$''; do not accept ``the graph goes down'' without a limit.}"

    t += r"\banner{3. Solutions and marks \textemdash\ Part B (no calculator)}"
    t += r"\qh{5.}{Original}{3}"
    t += r"\sol{\textbf{A} [1] Increases: every time the input $t$ rises, the output $d(t)$ rises ($0<12<22<30<36$).\\ \textbf{B} [1] $\dfrac{d(3)-d(1)}{3-1}=\dfrac{30-12}{2}=9$ km per hour.\\ \textbf{C} [1] Over the four hours the rates are $12,\ 10,\ 8,\ 6$ km per hour. The rate of change is decreasing (by $2$ km per hour each hour), so the graph of $d$ is increasing and concave down. Needs the four values and a statement that the rate is decreasing leading to concave down. \emph{Common error:} ``the rate is decreasing so $d$ is decreasing.''}"
    t += r"\qh{6.}{Original}{4}"
    t += r"\sol{\textbf{A} [1] Non-real zeros of a polynomial with real coefficients occur in conjugate pairs, so $1-2i$ forces $1+2i$.\\ \textbf{B} [1] Degree $4$ ($2+1+1$). $p(x)=2(x-3)^{2}\big(x^{2}-2x+5\big)$, since $(x-(1-2i))(x-(1+2i))=(x-1)^{2}+4=x^{2}-2x+5$. Accept $2(x-3)^2(x-1+2i)(x-1-2i)$ only if the factors with real coefficients are also given; the question asks for real coefficients.\\ \textbf{C} [1] $\displaystyle\lim_{x\to\infty}p(x)=\infty$ and $\displaystyle\lim_{x\to-\infty}p(x)=\infty$ (even degree, positive leading coefficient).\\ \textbf{D} [1] The graph touches the $x$-axis at $x=3$ and turns back without crossing, because the multiplicity $2$ is even.}"
    t += r"\qh{7.}{Original}{8}"
    t += r"\sol{Write $r(x)=\dfrac{2(x-3)(x+2)}{(x-3)(x+3)}$.\\ \textbf{A(i)} [1] Numerator $2(x-3)(x+2)$, denominator $(x-3)(x+3)$; $x\ne 3$ and $x\ne -3$ (both values needed).\\ \textbf{A(ii)} [1] The factor $x-3$ cancels, so there is a hole at $x=3$. For $x\ne3$, $r(x)=\dfrac{2(x+2)}{x+3}$; at $x=3$ this is $\dfrac{10}{6}=\dfrac53$. Hole at $\left(3,\dfrac53\right)$.\\ \textbf{B(i)} [1] Only $x=-2$.\\ \textbf{B(ii)} [1] No. $x=3$ is not in the domain of $r$, so $r(3)$ is undefined; the cancelled factor gives a hole, not a zero.\\ \textbf{C(i)} [1] $x=-3$.\\ \textbf{C(ii)} [1] Near $x=-3$, $r(x)=\dfrac{2(x+2)}{x+3}$ with numerator close to $-2$. From the left the denominator is a small negative number, so $\displaystyle\lim_{x\to-3^{-}}r(x)=\infty$; from the right it is a small positive number, so $\displaystyle\lim_{x\to-3^{+}}r(x)=-\infty$ (both needed).\\ \textbf{D(i)} [1] $\displaystyle\lim_{x\to\infty}r(x)=2$.\\ \textbf{D(ii)} [1] $y=2$. The numerator and denominator both have degree $2$, so the end behavior is the ratio of leading coefficients $\dfrac21=2$ in both directions, and $\displaystyle\lim_{x\to-\infty}r(x)=2$ as well.}"

    # decision guide
    t += r"\banner{4. Mark map by cluster}"
    t += r"""
\begin{tabular}{@{}p{3.1cm}p{4.0cm}p{2.0cm}p{6.4cm}@{}}
\toprule \textbf{Cluster} & \textbf{Lessons} & \textbf{Marks} & \textbf{Where}\\\midrule
C1 Rates of change and concavity & 1.1, 1.2, 1.3, 1.4 & 15 & Q1 (6), Q2 (3), Q3 (3), Q5 (3)\\
C2 Polynomial zeros and end behavior & 1.5, 1.6 & 6 & Q4 (2), Q6 (4)\\
C3 Rational functions & 1.7, 1.8, 1.9, 1.10 & 8 & Q7 (8): D 1.7, B 1.8, C 1.9, A 1.10, two marks each\\\midrule
Total & & 29 & Part A 14, Part B 15\\\bottomrule
\end{tabular}
"""
    t += r"\banner{5. Readiness bands and when an intervention plan is required}"
    t += r"""
\textbf{Individual readiness (total out of 29).}

\begin{tabular}{@{}p{3.2cm}p{2.6cm}p{10cm}@{}}
\toprule \textbf{Band} & \textbf{Marks} & \textbf{Action}\\\midrule
Ready & 22 to 29 ($\ge 75\%$) & Continue with the pacing. Practise the flagged cluster, if any, in the weekly mixed-review session.\\
Developing & 18 to 21 ($62\%$ to $74\%$) & Continue, and add a 20-minute targeted clinic on each cluster scoring under $60\%$.\\
Intervention & 0 to 17 ($<60\%$) & Individual intervention plan: reteach the weakest cluster, rework the missed parts from Lessons 1.1 to 1.10, then a short retest.\\\bottomrule
\end{tabular}

\par\vspace{4pt}\textbf{Cluster flag.} A cluster is flagged for a student when the student earns under $60\%$ of its marks (C1 under 9, C2 under 4, C3 under 5), whatever the total.

\par\vspace{4pt}\textbf{Group decision.} Count the students in the Intervention band and the class average for each cluster.

\begin{tabular}{@{}p{7cm}p{9cm}@{}}
\toprule \textbf{If} & \textbf{Then}\\\midrule
$30\%$ or more of the group is in the Intervention band, \emph{or} any cluster class average is under $70\%$, \emph{or} two or more students are flagged on the same cluster & \textbf{An intervention plan is required.} Reteach the weakest cluster to the whole group before Lesson 1.11 (one full session: Diagnose, Targeted Instruction, Practice, Mastery Gate), then give a parallel retest of that cluster.\\
Fewer than $30\%$ in Intervention, every cluster average at $70\%$ or more, and no cluster flagged by two students & \textbf{No group intervention.} Individual clinics only for the students flagged above; carry on with Lesson 1.11.\\\bottomrule
\end{tabular}

\par\vspace{4pt}\textbf{Reading a weak cluster.}\par\vspace{2pt}\noindent\begin{tabular}{@{}p{3.1cm}p{12.6cm}@{}}
C1 low & Check Q1 B(i) and Q2 B(i) first: if average rate of change is wrong the rest follows. If the calculation is right but B(iii) is missed, the gap is concavity and the secant position, not arithmetic.\\
C2 low & Q4 B(i) missed all three zeros means calculator graphing and intersection skills; Q6 A and D missed means conjugate pairs and multiplicity.\\
C3 low & Q7 A and B missed means factoring and cancelling; C missed means one-sided limits and the sign of the denominator; D missed means degrees and leading coefficients.\\
\end{tabular}
"""
    t += r"\par\vspace{4pt}{\small A spreadsheet that applies these rules automatically is supplied with this exam: enter each student's mark for every part and it returns the total, band, flagged clusters and the group decision.}"
    t += r"\end{document}"
    return t

import re
def wrap(t):
    pat=re.compile(r'((?:\\par\\vspace\{2pt\}\\textbf\{[A-D]\.\}|\\hspace\{1\.3em\}\\textbf\{\([iv]+\)\})(?:(?!\\worklines).)*?\\worklines\{\d+\})',re.S)
    return pat.sub(lambda m:r'\par\begin{minipage}{\linewidth}'+m.group(1)+r'\end{minipage}',t)
for name, f in (("AP-Precalc_Unit1_Checkpoint_Exam", exam), ("AP-Precalc_Unit1_Checkpoint_Answer-Key", key)):
    open(name + ".tex", "w").write(wrap(f()) if "Exam" in name else f())
    for _ in range(2):
        subprocess.run(["xelatex", "-interaction=nonstopmode", name + ".tex"], capture_output=True, text=True)
    log = open(name + ".log", errors="ignore").read()
    print(name, [l for l in log.splitlines() if l.startswith("!")][:5], log.count("Overfull"))
    print(subprocess.run(["pdfinfo", name + ".pdf"], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0], "pages")
