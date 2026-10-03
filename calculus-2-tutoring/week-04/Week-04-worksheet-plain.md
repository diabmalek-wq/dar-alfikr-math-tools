\worksheettitle{04}{Integration Techniques II: Trigonometric Integrals, Partial Fractions \& the Weierstrass Substitution}{}

**Recap and orientation**

Last week covered substitution and integration by parts. This week finishes the integration-techniques toolkit with **trigonometric-integral identities** (for products and powers of $\sin,\cos,\sec,\tan$), **partial fractions** (for rational functions), and one powerful "universal" technique, the **Weierstrass substitution**, which converts *any* rational function of $\sin x$ and $\cos x$ into an ordinary rational function of $t$, solvable by partial fractions.

**Why this matters**

A $\sec^n x\tan^m x$ integral attacked with the wrong parity choice, or a partial-fraction integral where long division is forgotten because the numerator's degree is not smaller than the denominator's, are classic exam traps. The Weierstrass substitution is the technique to reach for when no other pattern applies: it always works, though it is not always the fastest. Units on improper integrals and series (Weeks 5-14) all assume fluency with this full toolkit.

\begin{factbox}{Powers of $\sin x$ and $\cos x$ (OpenStax §3.2)}

To integrate \(\int \sin^n x\cos^m x\,dx\):

\begin{itemize}
\tightlist
\item
  If \textbf{either} exponent is \textbf{odd}, peel off one copy of that
  function, convert the remaining even power using
  \(\sin^2x+\cos^2x=1\), and substitute \(u=\) (the other function). For
  odd \(m\): write \(\cos^m x=\cos^{m-1}x\cos x\), convert
  \(\cos^{m-1}x\) (an even power) via \(\cos^2x=1-\sin^2x\), then let
  \(u=\sin x\).
\item
  If \textbf{both} exponents are \textbf{even}, use the half-angle
  identities \(\sin^2x=\dfrac{1-\cos(2x)}{2}\) and
  \(\cos^2x=\dfrac{1+\cos(2x)}{2}\) to reduce the powers before
  integrating (repeat if needed).
\end{itemize}

\end{factbox}

\begin{factbox}{Powers of $\sec x$ and $\tan x$ (OpenStax §3.2; MAT137 Unit 9)}

To integrate \(\int \sec^n x\tan^m x\,dx\) use
\(\dfrac{d}{dx}[\tan x]=\sec^2x\),
\(\dfrac{d}{dx}[\sec x]=\sec x\tan x\) and \(\tan^2x+1=\sec^2x\):

\begin{itemize}
\tightlist
\item
  If \(n\) (the power of secant) is \textbf{even}, peel off \(\sec^2x\),
  convert the rest of the secant power to tangents via
  \(\sec^2x=1+\tan^2x\), and substitute \(u=\tan x\).
\item
  If \(m\) (the power of tangent) is \textbf{odd}, peel off one
  \(\sec x\tan x\), convert the remaining even tangent power to secants
  via \(\tan^2x=\sec^2x-1\), and substitute \(u=\sec x\).
\item
  The integrals \(\int\sec x\,dx=\ln|\sec x+\tan x|+C\) and
  \(\int\csc x\,dx=-\ln|\csc x+\cot x|+C\) fit neither pattern and must
  be memorized (or re-derived with the trick of multiplying by
  \(\dfrac{\sec x+\tan x}{\sec x+\tan x}\)).
\end{itemize}

\end{factbox}

\begin{definitionbox}{Partial Fraction Decomposition (OpenStax §3.4)}

A rational function \(\dfrac{P(x)}{Q(x)}\) can be decomposed into
simpler fractions \textbf{only when} \(\deg P<\deg Q\). If
\(\deg P\ge\deg Q\), \textbf{long divide first}:
\(\dfrac{P(x)}{Q(x)}=A(x)+\dfrac{R(x)}{Q(x)}\) with \(\deg R<\deg Q\),
and only then decompose \(\dfrac{R(x)}{Q(x)}\). The shape of the
decomposition is determined by factoring \(Q(x)\):

\begin{itemize}
\tightlist
\item
  A \textbf{distinct linear factor} \((x-a)\) contributes
  \(\dfrac{A}{x-a}\).
\item
  A \textbf{repeated linear factor} \((x-a)^k\) contributes
  \(\dfrac{A_1}{x-a}+\dfrac{A_2}{(x-a)^2}+\cdots+\dfrac{A_k}{(x-a)^k}\):
  one term for \emph{every} power from \(1\) to \(k\).
\item
  An \textbf{irreducible quadratic factor} contributes
  \(\dfrac{Ax+B}{x^2+px+q}\) (a linear numerator).
\end{itemize}

Each piece then integrates with \(\int\dfrac{du}{u}=\ln|u|+C\) (linear
factors), the power rule (repeated factors), or
\(\int\dfrac{du}{u^2+a^2}=\dfrac1a\arctan\!\left(\dfrac ua\right)+C\)
(irreducible quadratics).

\end{definitionbox}

\begin{factbox}{The Weierstrass Substitution, a Universal Rational-Trig Technique (Dummit)}

For an integrand that is a rational function of \(\sin x\) and
\(\cos x\), the substitution \(t=\tan\!\left(\dfrac{x}{2}\right)\)
converts the entire integrand into an ordinary rational function of
\(t\) via
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sin x=\frac{2t}{1+t^2},\qquad \cos x=\frac{1-t^2}{1+t^2},\qquad dx=\frac{2\,dt}{1+t^2}.$\end{adjustbox}\par\noindent 
The resulting integral in \(t\) is always solvable by partial fractions.
It is a \textbf{fallback}: it always works on rational-trig integrands,
but is not always the fastest route.

\end{factbox}

\sectionbanner{Worked Examples}

\begin{examplebox}{1}

\textit{Level: Foundational. Odd power of sine}\par\smallskip

Evaluate \(\displaystyle\int \sin^3 x\cos^2 x\,dx\).

\textbf{Step 1.} Identify the powers: \(\sin x\) appears to the power
\(3\) (odd) and \(\cos x\) to the power \(2\) (even). The rule for
\(\int \sin^m x\cos^n x\,dx\) says that when one exponent is odd, we
peel off one copy of that odd-power function.

\smallskip

\textbf{Step 2.} Peel off one factor of \(\sin x\):
\(\sin^3 x = \sin^2 x\cdot \sin x\). The reason for keeping a single
\(\sin x\) is that it will become the \(du\) of a substitution.

\smallskip

\textbf{Step 3.} The remaining even power \(\sin^2 x\) must be written
using cosines. Use the Pythagorean identity \(\sin^2 x + \cos^2 x = 1\),
which gives \(\sin^2 x = 1 - \cos^2 x\).

\smallskip

\textbf{Step 4.} Rewrite the integral:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int \sin^3 x\cos^2 x\,dx = \int (1-\cos^2 x)\cos^2 x\,\sin x\,dx.$\end{adjustbox}\par\noindent 
Now every factor except the lone \(\sin x\) is a function of \(\cos x\).

\smallskip

\textbf{Step 5.} Choose the substitution \(u = \cos x\).
Differentiating, \(du = -\sin x\,dx\), so \(\sin x\,dx = -du\).

\smallskip

\textbf{Step 6.} Substitute: \(\cos^2 x = u^2\) and
\(\sin x\,dx = -du\), so the integral becomes
\par\begin{adjustbox}{max width=\boxmathwidth,center}$-\int (1-u^2)\,u^2\,du.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Expand the product inside the integral:
\((1-u^2)u^2 = u^2 - u^4\). So we need \(-\int (u^2 - u^4)\,du\).

\smallskip

\textbf{Step 8.} Apply the power rule
\(\int u^k\,du = \dfrac{u^{k+1}}{k+1}\) to each term:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$-\left(\dfrac{u^3}{3} - \dfrac{u^5}{5}\right) + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Distribute the minus sign:
\(-\dfrac{u^3}{3} + \dfrac{u^5}{5} + C\).

\smallskip

\textbf{Step 10.} Replace \(u\) by \(\cos x\) to return to the original
variable: \(-\dfrac{\cos^3 x}{3} + \dfrac{\cos^5 x}{5} + C\).

\smallskip

\textbf{Step 11.} Verify by differentiating. By the chain rule,
\(\dfrac{d}{dx}\left[-\dfrac{\cos^3 x}{3}\right] = -\dfrac{3\cos^2 x\,(-\sin x)}{3} = \cos^2 x\sin x\)
and
\(\dfrac{d}{dx}\left[\dfrac{\cos^5 x}{5}\right] = \dfrac{5\cos^4 x\,(-\sin x)}{5} = -\cos^4 x\sin x\).

\smallskip

\textbf{Step 12.} Add the two derivatives:
\(\cos^2 x\sin x - \cos^4 x\sin x = \cos^2 x\sin x\,(1-\cos^2 x) = \cos^2 x\sin x\cdot\sin^2 x = \sin^3 x\cos^2 x\),
which is the original integrand.

\textbf{Answer.} \(-\dfrac{\cos^3 x}{3} + \dfrac{\cos^5 x}{5} + C\)

\end{examplebox}

\begin{examplebox}{2}

\textit{Level: Foundational. Both powers even: half-angle identity}\par\smallskip

Evaluate \(\displaystyle\int \cos^2 x\,dx\).

\textbf{Step 1.} Identify the powers: \(\cos x\) appears to the power
\(2\) and \(\sin x\) to the power \(0\). Both are even, so there is no
odd factor to peel off and the substitution method of Example 1 is
unavailable.

\smallskip

\textbf{Step 2.} Instead, lower the power with a half-angle identity.
Recall the double-angle formula \(\cos(2x) = 2\cos^2 x - 1\).

\smallskip

\textbf{Step 3.} Solve that formula for \(\cos^2 x\): add \(1\) to both
sides to get \(1 + \cos(2x) = 2\cos^2 x\), then divide by \(2\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\cos^2 x = \dfrac{1+\cos(2x)}{2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Replace the integrand using this identity:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int \cos^2 x\,dx = \int \dfrac{1+\cos(2x)}{2}\,dx.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Pull out the constant factor \(\dfrac{1}{2}\) and split
the sum: \par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{1}{2}\int 1\,dx + \dfrac{1}{2}\int \cos(2x)\,dx.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} The first integral is
\(\dfrac{1}{2}\int 1\,dx = \dfrac{x}{2}\).

\smallskip

\textbf{Step 7.} For the second integral use the substitution
\(w = 2x\), so \(dw = 2\,dx\) and \(dx = \dfrac{dw}{2}\). Then
\(\int \cos(2x)\,dx = \dfrac{1}{2}\int \cos w\,dw = \dfrac{\sin w}{2} = \dfrac{\sin(2x)}{2}\).

\smallskip

\textbf{Step 8.} Multiply by the outside factor \(\dfrac{1}{2}\):
\(\dfrac{1}{2}\cdot\dfrac{\sin(2x)}{2} = \dfrac{\sin(2x)}{4}\).

\smallskip

\textbf{Step 9.} Combine the pieces and add the constant:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{x}{2} + \dfrac{\sin(2x)}{4} + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} Verify by differentiating:
\(\dfrac{d}{dx}\left[\dfrac{x}{2}\right] = \dfrac{1}{2}\) and
\(\dfrac{d}{dx}\left[\dfrac{\sin(2x)}{4}\right] = \dfrac{2\cos(2x)}{4} = \dfrac{\cos(2x)}{2}\).
The sum is \(\dfrac{1+\cos(2x)}{2} = \cos^2 x\), as required.

\textbf{Answer.} \(\dfrac{x}{2} + \dfrac{\sin(2x)}{4} + C\)

\end{examplebox}

\begin{examplebox}{3}

\textit{Level: Intermediate. Both powers even: identity used twice}\par\smallskip

Evaluate \(\displaystyle\int \cos^4 x\,dx\).

\textbf{Step 1.} Identify the powers: \(\cos x\) has power \(4\) and
\(\sin x\) has power \(0\), both even, so use the half-angle identity
\(\cos^2 x = \dfrac{1+\cos(2x)}{2}\).

\smallskip

\textbf{Step 2.} Write the fourth power as a square of a square:
\(\cos^4 x = (\cos^2 x)^2\).

\smallskip

\textbf{Step 3.} Apply the identity inside the parentheses:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\cos^4 x = \left(\dfrac{1+\cos(2x)}{2}\right)^2.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Square the fraction: numerator
\((1+\cos 2x)^2 = 1 + 2\cos 2x + \cos^2 2x\) (using
\((a+b)^2 = a^2+2ab+b^2\)) and denominator \(2^2 = 4\). So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\cos^4 x = \dfrac{1 + 2\cos 2x + \cos^2 2x}{4}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} The term \(\cos^2 2x\) is again an even power, so apply
the half-angle identity a second time. Replace the angle \(x\) by \(2x\)
in \(\cos^2\theta = \dfrac{1+\cos 2\theta}{2}\) to get
\(\cos^2 2x = \dfrac{1+\cos 4x}{2}\).

\smallskip

\textbf{Step 6.} Substitute this into the numerator:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\cos^4 x = \dfrac{1}{4}\left(1 + 2\cos 2x + \dfrac{1+\cos 4x}{2}\right) = \dfrac14 + \dfrac{\cos 2x}{2} + \dfrac{1}{8} + \dfrac{\cos 4x}{8}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Combine the constants:
\(\dfrac14 + \dfrac18 = \dfrac28 + \dfrac18 = \dfrac38\). So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\cos^4 x = \dfrac38 + \dfrac{\cos 2x}{2} + \dfrac{\cos 4x}{8}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 8.} Integrate term by term.
\(\int \dfrac38\,dx = \dfrac{3x}{8}\).

\smallskip

\textbf{Step 9.} \(\int \dfrac{\cos 2x}{2}\,dx\): since
\(\int\cos(2x)\,dx = \dfrac{\sin 2x}{2}\), this equals
\(\dfrac12\cdot\dfrac{\sin 2x}{2} = \dfrac{\sin 2x}{4}\).

\smallskip

\textbf{Step 10.} \(\int \dfrac{\cos 4x}{8}\,dx\): since
\(\int\cos(4x)\,dx = \dfrac{\sin 4x}{4}\), this equals
\(\dfrac18\cdot\dfrac{\sin 4x}{4} = \dfrac{\sin 4x}{32}\).

\smallskip

\textbf{Step 11.} Add the three results and the constant:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{3x}{8} + \dfrac{\sin 2x}{4} + \dfrac{\sin 4x}{32} + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 12.} Verify at one value. The derivative of the answer is
\(\dfrac38 + \dfrac{\cos 2x}{2} + \dfrac{\cos 4x}{8}\). At \(x = 0\)
this is \(\dfrac38+\dfrac12+\dfrac18 = 1\), and \(\cos^4 0 = 1\). At
\(x = \dfrac{\pi}{2}\) it is \(\dfrac38 - \dfrac12 + \dfrac18 = 0\), and
\(\cos^4\dfrac{\pi}{2} = 0\).

\textbf{Answer.}
\(\dfrac{3x}{8} + \dfrac{\sin 2x}{4} + \dfrac{\sin 4x}{32} + C\)

\end{examplebox}

\begin{examplebox}{4}

\textit{Level: Intermediate. Secant and tangent with odd tangent power}\par\smallskip

Evaluate \(\displaystyle\int \sec^4 x\tan^3 x\,dx\).

\textbf{Step 1.} Identify the powers: secant has power \(n=4\) (even)
and tangent has power \(m=3\) (odd). We will use the derivatives
\(\dfrac{d}{dx}[\sec x] = \sec x\tan x\) and the identity
\(\tan^2 x + 1 = \sec^2 x\).

\smallskip

\textbf{Step 2.} Two rules apply here. Because the tangent power is odd,
we can peel off one factor \(\sec x\tan x\) (which is \(d(\sec x)\)) and
use \(u = \sec x\). (The even secant power would also allow
\(u=\tan x\); we follow the odd-tangent rule.)

\smallskip

\textbf{Step 3.} Split off the factor:
\(\sec^4 x\tan^3 x = \sec^3 x\,\tan^2 x\cdot(\sec x\tan x)\). Check:
\(\sec^3\cdot\sec = \sec^4\) and \(\tan^2\cdot\tan = \tan^3\).

\smallskip

\textbf{Step 4.} Convert the remaining even tangent power with
\(\tan^2 x = \sec^2 x - 1\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sec^4 x\tan^3 x = \sec^3 x\,(\sec^2 x - 1)\,(\sec x\tan x).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Substitute \(u = \sec x\), so
\(du = \sec x\tan x\,dx\). Every factor is now in terms of \(u\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int u^3(u^2-1)\,du.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Expand: \(u^3(u^2 - 1) = u^5 - u^3\).

\smallskip

\textbf{Step 7.} Apply the power rule:
\(\int (u^5 - u^3)\,du = \dfrac{u^6}{6} - \dfrac{u^4}{4} + C\).

\smallskip

\textbf{Step 8.} Back-substitute \(u = \sec x\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{\sec^6 x}{6} - \dfrac{\sec^4 x}{4} + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Verify by differentiating with the chain rule:
\(\dfrac{d}{dx}\left[\dfrac{\sec^6 x}{6}\right] = \sec^5 x\cdot\sec x\tan x = \sec^6 x\tan x\)
and
\(\dfrac{d}{dx}\left[\dfrac{\sec^4 x}{4}\right] = \sec^3 x\cdot\sec x\tan x = \sec^4 x\tan x\).

\smallskip

\textbf{Step 10.} Subtract:
\(\sec^6 x\tan x - \sec^4 x\tan x = \sec^4 x\tan x(\sec^2 x - 1) = \sec^4 x\tan x\cdot\tan^2 x = \sec^4 x\tan^3 x\),
the original integrand.

\textbf{Answer.} \(\dfrac{\sec^6 x}{6} - \dfrac{\sec^4 x}{4} + C\)

\end{examplebox}

\begin{examplebox}{5}

\textit{Level: Advanced. Both powers even: sine squared times cosine squared}\par\smallskip

Evaluate \(\displaystyle\int \sin^2 x\cos^2 x\,dx\).

\textbf{Step 1.} Identify the powers: \(\sin x\) has power \(2\) and
\(\cos x\) has power \(2\), both even, so no factor can be peeled off
for a substitution. Applying half-angle identities to both factors
separately would give a product of two sums, which is messy, so first
combine the factors.

\smallskip

\textbf{Step 2.} Recall the double-angle formula
\(\sin 2x = 2\sin x\cos x\). Dividing by \(2\):
\(\sin x\cos x = \dfrac{\sin 2x}{2}\).

\smallskip

\textbf{Step 3.} Square both sides:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sin^2 x\cos^2 x = (\sin x\cos x)^2 = \dfrac{\sin^2 2x}{4}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} The new factor \(\sin^2 2x\) is an even power of a
single function, so use the half-angle identity
\(\sin^2\theta = \dfrac{1-\cos 2\theta}{2}\) with \(\theta = 2x\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sin^2 2x = \dfrac{1-\cos 4x}{2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Substitute:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sin^2 x\cos^2 x = \dfrac14\cdot\dfrac{1-\cos 4x}{2} = \dfrac{1-\cos 4x}{8}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Check the identity at \(x = \dfrac{\pi}{4}\): the left
side is
\(\left(\dfrac{\sqrt2}{2}\right)^2\left(\dfrac{\sqrt2}{2}\right)^2 = \dfrac14\)
and the right side is
\(\dfrac{1-\cos\pi}{8} = \dfrac{2}{8} = \dfrac14\). They agree.

\smallskip

\textbf{Step 7.} Integrate:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int \dfrac{1-\cos 4x}{8}\,dx = \dfrac18\int 1\,dx - \dfrac18\int\cos 4x\,dx.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 8.} The first term is \(\dfrac{x}{8}\). For the second,
\(\int\cos 4x\,dx = \dfrac{\sin 4x}{4}\) (substitution \(w=4x\),
\(dx = \dfrac{dw}{4}\)), so the term is
\(\dfrac18\cdot\dfrac{\sin 4x}{4} = \dfrac{\sin 4x}{32}\).

\smallskip

\textbf{Step 9.} Combine: \par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{x}{8} - \dfrac{\sin 4x}{32} + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} Verify by differentiating:
\(\dfrac{d}{dx}\left[\dfrac{x}{8} - \dfrac{\sin 4x}{32}\right] = \dfrac18 - \dfrac{4\cos 4x}{32} = \dfrac{1-\cos 4x}{8} = \sin^2 x\cos^2 x\),
as required.

\textbf{Answer.} \(\dfrac{x}{8} - \dfrac{\sin 4x}{32} + C\)

\end{examplebox}

\begin{examplebox}{6}

\textit{Level: Intermediate. Even power of secant: the substitution u = tan x}\par\smallskip

Evaluate \(\displaystyle\int \sec^4 x\tan^2 x\,dx\).

\textbf{Step 1.} Identify the powers: secant has power \(4\) (even) and
tangent has power \(2\) (even). The tangent power is not odd, so the
odd-tangent rule (\(u=\sec x\)) does not apply. The secant power is
even, so we use the even-secant rule with \(u = \tan x\).

\smallskip

\textbf{Step 2.} The reason this works:
\(\dfrac{d}{dx}[\tan x] = \sec^2 x\), so a single factor
\(\sec^2 x\,dx\) becomes \(du\).

\smallskip

\textbf{Step 3.} Peel off one factor \(\sec^2 x\):
\(\sec^4 x = \sec^2 x\cdot\sec^2 x\).

\smallskip

\textbf{Step 4.} Convert the other \(\sec^2 x\) into tangents with the
identity \(\sec^2 x = 1 + \tan^2 x\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sec^4 x\tan^2 x = (1+\tan^2 x)\tan^2 x\cdot\sec^2 x.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Substitute \(u = \tan x\), so \(du = \sec^2 x\,dx\).
The integral becomes \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int (1+u^2)u^2\,du.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Expand: \((1+u^2)u^2 = u^2 + u^4\).

\smallskip

\textbf{Step 7.} Apply the power rule:
\(\int (u^2 + u^4)\,du = \dfrac{u^3}{3} + \dfrac{u^5}{5} + C\).

\smallskip

\textbf{Step 8.} Back-substitute \(u = \tan x\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{\tan^3 x}{3} + \dfrac{\tan^5 x}{5} + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Verify by differentiating:
\(\dfrac{d}{dx}\left[\dfrac{\tan^3 x}{3}\right] = \tan^2 x\sec^2 x\) and
\(\dfrac{d}{dx}\left[\dfrac{\tan^5 x}{5}\right] = \tan^4 x\sec^2 x\).

\smallskip

\textbf{Step 10.} Add:
\(\tan^2 x\sec^2 x + \tan^4 x\sec^2 x = \tan^2 x\sec^2 x(1+\tan^2 x) = \tan^2 x\sec^2 x\cdot\sec^2 x = \sec^4 x\tan^2 x\),
the original integrand.

\smallskip

\textbf{Step 11.} Remark on where \(\int\sec x\,dx\) enters: when the
secant power is odd and the tangent power is even (for example
\(\int \sec x\,dx\) itself), neither rule applies. Multiplying by
\(\dfrac{\sec x + \tan x}{\sec x+\tan x}\) gives
\(\int \dfrac{\sec^2 x + \sec x\tan x}{\sec x + \tan x}\,dx\), and with
\(u = \sec x + \tan x\), \(du = (\sec x\tan x + \sec^2 x)\,dx\), the
result is \(\ln|\sec x + \tan x| + C\). It is not needed in this example
because the secant power here is even.

\textbf{Answer.} \(\dfrac{\tan^3 x}{3} + \dfrac{\tan^5 x}{5} + C\)

\end{examplebox}

\begin{examplebox}{7}

\textit{Level: Foundational. Long division, then integrate}\par\smallskip

Evaluate \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int \dfrac{x^2+3x+5}{x+1}\,dx.$\end{adjustbox}\par\noindent 

\textbf{Step 1.} Compare degrees. The numerator \(x^2+3x+5\) has degree
\(2\) and the denominator \(x+1\) has degree \(1\). Partial fractions
only work when the numerator has strictly smaller degree than the
denominator, so we must first divide the numerator by the denominator
(long division).

\smallskip

\textbf{Step 2.} Start the division. Divide the leading term of the
numerator by the leading term of the denominator: \(\dfrac{x^2}{x}=x\).
This is the first term of the quotient.

\smallskip

\textbf{Step 3.} Multiply that term back by the whole divisor:
\(x\,(x+1)=x^2+x\). Subtract it from the numerator:
\((x^2+3x+5)-(x^2+x)=2x+5\).

\smallskip

\textbf{Step 4.} Repeat with the new leading term: \(\dfrac{2x}{x}=2\).
Multiply back: \(2\,(x+1)=2x+2\). Subtract: \((2x+5)-(2x+2)=3\).

\smallskip

\textbf{Step 5.} The remainder \(3\) has degree \(0\), which is less
than the degree \(1\) of the divisor, so the division stops. The
quotient is \(x+2\) and the remainder is \(3\), that is
\(x^2+3x+5=(x+1)(x+2)+3\).

\smallskip

\textbf{Step 6.} Check the division by expanding:
\((x+1)(x+2)=x^2+2x+x+2=x^2+3x+2\), and adding the remainder gives
\(x^2+3x+2+3=x^2+3x+5\), which is the original numerator.

\smallskip

\textbf{Step 7.} Divide both sides of \(x^2+3x+5=(x+1)(x+2)+3\) by
\(x+1\) to rewrite the integrand:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{x^2+3x+5}{x+1}=x+2+\dfrac{3}{x+1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 8.} Split the integral into three pieces:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\left(x+2+\dfrac{3}{x+1}\right)dx=\int x\,dx+\int 2\,dx+3\int\dfrac{dx}{x+1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Integrate the first two pieces with the power rule
\(\int x^n\,dx=\dfrac{x^{n+1}}{n+1}\) and the constant rule:
\(\int x\,dx=\dfrac{x^2}{2}\) and \(\int 2\,dx=2x\).

\smallskip

\textbf{Step 10.} For the third piece let \(u=x+1\), so \(du=dx\). Then
\(\int\dfrac{dx}{x+1}=\int\dfrac{du}{u}=\ln|u|=\ln|x+1|\), using
\(\int\dfrac{du}{u}=\ln|u|+C\).

\smallskip

\textbf{Step 11.} Assemble the result:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{x^2+3x+5}{x+1}\,dx=\dfrac{x^2}{2}+2x+3\ln|x+1|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 12.} Verify by differentiating:
\(\dfrac{d}{dx}\left[\dfrac{x^2}{2}+2x+3\ln|x+1|\right]=x+2+\dfrac{3}{x+1}=\dfrac{(x+2)(x+1)+3}{x+1}=\dfrac{x^2+3x+5}{x+1}\),
which is the original integrand.

\textbf{Answer.} \(\dfrac{x^2}{2}+2x+3\ln|x+1|+C\)

\end{examplebox}

\begin{examplebox}{8}

\textit{Level: Intermediate. Repeated linear factor}\par\smallskip

Evaluate \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int \dfrac{2x+6}{(x+1)^2}\,dx.$\end{adjustbox}\par\noindent 

\textbf{Step 1.} The numerator has degree \(1\) and the denominator
\((x+1)^2\) has degree \(2\), so no long division is needed and we can
decompose directly.

\smallskip

\textbf{Step 2.} The denominator contains the repeated linear factor
\((x+1)^2\). A repeated factor needs one term for every power from \(1\)
up to \(2\), so the shape is
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{2x+6}{(x+1)^2}=\dfrac{A}{x+1}+\dfrac{B}{(x+1)^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Multiply both sides by the common denominator
\((x+1)^2\) to clear the fractions: \par\begin{adjustbox}{max width=\boxmathwidth,center}$2x+6=A(x+1)+B.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Find \(B\) by choosing the value of \(x\) that kills
the \(A\) term, namely \(x=-1\): \(2(-1)+6=A(0)+B\), so \(B=4\).

\smallskip

\textbf{Step 5.} Find \(A\) by comparing the coefficients of \(x\) on
both sides. The right side expands to \(Ax+A+B\), whose coefficient of
\(x\) is \(A\); the left side has coefficient \(2\). So \(A=2\).

\smallskip

\textbf{Step 6.} Check with the constant terms: \(A+B=2+4=6\), which
matches the constant \(6\) on the left. The decomposition is
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{2x+6}{(x+1)^2}=\dfrac{2}{x+1}+\dfrac{4}{(x+1)^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Integrate term by term:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{2x+6}{(x+1)^2}\,dx=2\int\dfrac{dx}{x+1}+4\int\dfrac{dx}{(x+1)^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 8.} Substitute \(u=x+1\), \(du=dx\) in both integrals. The
first is \(2\int\dfrac{du}{u}=2\ln|u|=2\ln|x+1|\).

\smallskip

\textbf{Step 9.} The second is \(4\int u^{-2}\,du\). By the power rule
\(\int u^{-2}\,du=\dfrac{u^{-1}}{-1}=-\dfrac{1}{u}\), so it equals
\(-\dfrac{4}{u}=-\dfrac{4}{x+1}\).

\smallskip

\textbf{Step 10.} Combine:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{2x+6}{(x+1)^2}\,dx=2\ln|x+1|-\dfrac{4}{x+1}+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 11.} Verify by differentiating:
\(\dfrac{d}{dx}\left[2\ln|x+1|-\dfrac{4}{x+1}\right]=\dfrac{2}{x+1}+\dfrac{4}{(x+1)^2}=\dfrac{2(x+1)+4}{(x+1)^2}=\dfrac{2x+6}{(x+1)^2}\),
the original integrand.

\textbf{Answer.} \(2\ln|x+1|-\dfrac{4}{x+1}+C\)

\end{examplebox}

\begin{examplebox}{9}

\textit{Level: Intermediate. Irreducible quadratic factor}\par\smallskip

Evaluate \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int \dfrac{3x+1}{(x^2+1)(x-2)}\,dx.$\end{adjustbox}\par\noindent 

\textbf{Step 1.} The numerator has degree \(1\) and the denominator has
degree \(3\), so we decompose directly. The factor \(x-2\) is a distinct
linear factor. The factor \(x^2+1\) cannot be factored over the real
numbers (it has no real roots, since \(x^2+1\geq 1\)), so it is an
irreducible quadratic.

\smallskip

\textbf{Step 2.} An irreducible quadratic contributes a term with a
linear numerator, and a linear factor contributes a constant numerator:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{3x+1}{(x^2+1)(x-2)}=\dfrac{Ax+B}{x^2+1}+\dfrac{C}{x-2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Multiply both sides by \((x^2+1)(x-2)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$3x+1=(Ax+B)(x-2)+C(x^2+1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Find \(C\) by substituting \(x=2\), which makes
\(x-2=0\): \(3(2)+1=(2A+B)(0)+C(4+1)\), so \(7=5C\) and
\(C=\dfrac{7}{5}\).

\smallskip

\textbf{Step 5.} Expand the right side fully:
\((Ax+B)(x-2)=Ax^2-2Ax+Bx-2B\), so \par\begin{adjustbox}{max width=\boxmathwidth,center}$3x+1=(A+C)x^2+(B-2A)x+(C-2B).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Match coefficients of \(x^2\): the left side has \(0\),
so \(A+C=0\) and \(A=-C=-\dfrac{7}{5}\).

\smallskip

\textbf{Step 7.} Match the constant terms: \(C-2B=1\), so
\(2B=C-1=\dfrac{7}{5}-1=\dfrac{2}{5}\) and \(B=\dfrac{1}{5}\).

\smallskip

\textbf{Step 8.} Check with the coefficient of \(x\):
\(B-2A=\dfrac{1}{5}+\dfrac{14}{5}=\dfrac{15}{5}=3\), which matches the
\(3\) on the left. So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{3x+1}{(x^2+1)(x-2)}=\dfrac{-\frac{7}{5}x+\frac{1}{5}}{x^2+1}+\dfrac{\frac{7}{5}}{x-2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Split the first fraction into two and integrate each
part:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{3x+1}{(x^2+1)(x-2)}\,dx=-\dfrac{7}{5}\int\dfrac{x}{x^2+1}\,dx+\dfrac{1}{5}\int\dfrac{dx}{x^2+1}+\dfrac{7}{5}\int\dfrac{dx}{x-2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} For the first integral let \(u=x^2+1\), so
\(du=2x\,dx\) and \(x\,dx=\dfrac{du}{2}\). Then
\(\int\dfrac{x}{x^2+1}\,dx=\dfrac{1}{2}\ln|u|=\dfrac{1}{2}\ln(x^2+1)\)
(no absolute value needed since \(x^2+1>0\)).

\smallskip

\textbf{Step 11.} The second integral is the standard form
\(\int\dfrac{du}{u^2+a^2}=\dfrac{1}{a}\arctan\left(\dfrac{u}{a}\right)\)
with \(a=1\), giving \(\arctan x\). The third is \(\ln|x-2|\) by
\(u=x-2\).

\smallskip

\textbf{Step 12.} Assemble:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$-\dfrac{7}{5}\cdot\dfrac{1}{2}\ln(x^2+1)+\dfrac{1}{5}\arctan x+\dfrac{7}{5}\ln|x-2|+C=-\dfrac{7}{10}\ln(x^2+1)+\dfrac{1}{5}\arctan x+\dfrac{7}{5}\ln|x-2|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 13.} Verify at \(x=0\): the integrand is
\(\dfrac{1}{(1)(-2)}=-\dfrac{1}{2}\). The derivative of the answer at
\(0\) is
\(-\dfrac{7}{10}\cdot\dfrac{0}{1}+\dfrac{1}{5}\cdot\dfrac{1}{1}+\dfrac{7}{5}\cdot\dfrac{1}{-2}=\dfrac{1}{5}-\dfrac{7}{10}=-\dfrac{1}{2}\),
as required.

\textbf{Answer.}
\(-\dfrac{7}{10}\ln(x^2+1)+\dfrac{1}{5}\arctan x+\dfrac{7}{5}\ln|x-2|+C\)

\end{examplebox}

\begin{examplebox}{10}

\textit{Level: Advanced. Definite integral with an exact logarithm}\par\smallskip

Evaluate \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int_0^1 \dfrac{4x+5}{(x+1)(x+2)}\,dx$\end{adjustbox}\par\noindent  and give the exact
value as a single logarithm.

\textbf{Step 1.} The numerator has degree \(1\) and the denominator has
degree \(2\), and the denominator is already factored into distinct
linear factors, so the shape is
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{4x+5}{(x+1)(x+2)}=\dfrac{A}{x+1}+\dfrac{B}{x+2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 2.} Clear denominators by multiplying by \((x+1)(x+2)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$4x+5=A(x+2)+B(x+1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Substitute \(x=-1\) (which kills the \(B\) term):
\(4(-1)+5=A(1)+B(0)\), so \(A=1\).

\smallskip

\textbf{Step 4.} Substitute \(x=-2\) (which kills the \(A\) term):
\(4(-2)+5=A(0)+B(-1)\), so \(-3=-B\) and \(B=3\).

\smallskip

\textbf{Step 5.} Check by recombining:
\(1\cdot(x+2)+3(x+1)=x+2+3x+3=4x+5\), which matches. So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{4x+5}{(x+1)(x+2)}=\dfrac{1}{x+1}+\dfrac{3}{x+2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Find an antiderivative. Using
\(\int\dfrac{dx}{x+a}=\ln|x+a|\) (substitute \(u=x+a\)),
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\left(\dfrac{1}{x+1}+\dfrac{3}{x+2}\right)dx=\ln|x+1|+3\ln|x+2|.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} The integrand is continuous on \([0,1]\) (the
denominator vanishes only at \(x=-1\) and \(x=-2\)), so the Fundamental
Theorem of Calculus applies. On \([0,1]\) both \(x+1\) and \(x+2\) are
positive, so the absolute values can be dropped.

\smallskip

\textbf{Step 8.} Evaluate at the upper limit \(x=1\): \(\ln 2+3\ln 3\).

\smallskip

\textbf{Step 9.} Evaluate at the lower limit \(x=0\):
\(\ln 1+3\ln 2=0+3\ln 2=3\ln 2\).

\smallskip

\textbf{Step 10.} Subtract (upper minus lower):
\(\ln 2+3\ln 3-3\ln 2=3\ln 3-2\ln 2\).

\smallskip

\textbf{Step 11.} Combine into one logarithm using \(n\ln a=\ln a^n\)
and \(\ln a-\ln b=\ln\dfrac{a}{b}\):
\(3\ln 3-2\ln 2=\ln 27-\ln 4=\ln\dfrac{27}{4}\).

\smallskip

\textbf{Step 12.} Sanity check numerically:
\(3\ln 3-2\ln 2\approx 3(1.0986)-2(0.6931)=3.2958-1.3863=1.9095\), and
\(\ln\dfrac{27}{4}=\ln 6.75\approx 1.9095\). The integrand is between
\(\dfrac{5}{2}\) (at \(x=0\)) and \(\dfrac{9}{6}=1.5\) (at \(x=1\)) on
an interval of length \(1\), so a value near \(1.9\) is reasonable.

\textbf{Answer.} \(\ln\dfrac{27}{4}=3\ln 3-2\ln 2\approx 1.9095\)

\end{examplebox}

\begin{examplebox}{11}

\textit{Level: Advanced. Weierstrass substitution with arctangent}\par\smallskip

Evaluate \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int \dfrac{1}{2+\cos x}\,dx.$\end{adjustbox}\par\noindent 

\textbf{Step 1.} Choose the technique. The integrand is a rational
function of \(\cos x\) with no power of sine or cosine to peel off and
no secant or tangent structure, so the odd-power, even-power and sec/tan
rules do not apply. The Weierstrass substitution
\(t=\tan\left(\dfrac{x}{2}\right)\) converts any rational function of
\(\sin x\) and \(\cos x\) into a rational function of \(t\).

\smallskip

\textbf{Step 2.} Derive \(\cos x\) in terms of \(t\). By the
double-angle identity
\(\cos x=\cos^2\left(\dfrac{x}{2}\right)-\sin^2\left(\dfrac{x}{2}\right)\),
and by the Pythagorean identity
\(1=\cos^2\left(\dfrac{x}{2}\right)+\sin^2\left(\dfrac{x}{2}\right)\).
Write
\(\cos x=\dfrac{\cos^2(x/2)-\sin^2(x/2)}{\cos^2(x/2)+\sin^2(x/2)}\) and
divide numerator and denominator by \(\cos^2\left(\dfrac{x}{2}\right)\)
to get
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\cos x=\dfrac{1-\tan^2(x/2)}{1+\tan^2(x/2)}=\dfrac{1-t^2}{1+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Find \(dx\). From \(t=\tan\left(\dfrac{x}{2}\right)\)
we get \(x=2\arctan t\), and since
\(\dfrac{d}{dt}\arctan t=\dfrac{1}{1+t^2}\),
\par\begin{adjustbox}{max width=\boxmathwidth,center}$dx=\dfrac{2\,dt}{1+t^2}.$\end{adjustbox}\par\noindent  (This is valid for \(-\pi<x<\pi\), where
\(\tan\left(\dfrac{x}{2}\right)\) is defined.)

\smallskip

\textbf{Step 4.} Substitute into the integral:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1}{2+\dfrac{1-t^2}{1+t^2}}\cdot\dfrac{2\,dt}{1+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Simplify the denominator by writing \(2\) over the
common denominator \(1+t^2\):
\(2+\dfrac{1-t^2}{1+t^2}=\dfrac{2(1+t^2)+(1-t^2)}{1+t^2}=\dfrac{2+2t^2+1-t^2}{1+t^2}=\dfrac{t^2+3}{1+t^2}\).

\smallskip

\textbf{Step 6.} Dividing by a fraction means multiplying by its
reciprocal, so the integrand becomes
\(\dfrac{1+t^2}{t^2+3}\cdot\dfrac{2}{1+t^2}\). The factor \(1+t^2\)
cancels: \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{2\,dt}{t^2+3}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Recognise the standard form
\(\int\dfrac{du}{u^2+a^2}=\dfrac{1}{a}\arctan\left(\dfrac{u}{a}\right)+C\)
with \(u=t\) and \(a=\sqrt{3}\) (since \(3=(\sqrt{3})^2\)).

\smallskip

\textbf{Step 8.} Apply it:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{2\,dt}{t^2+3}=\dfrac{2}{\sqrt{3}}\arctan\left(\dfrac{t}{\sqrt{3}}\right)+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Return to the original variable by replacing
\(t=\tan\left(\dfrac{x}{2}\right)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1}{2+\cos x}\,dx=\dfrac{2}{\sqrt{3}}\arctan\left(\dfrac{\tan(x/2)}{\sqrt{3}}\right)+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} Verify by differentiating with respect to \(x\). Use
\(\dfrac{dt}{dx}=\dfrac{1}{2}\sec^2\left(\dfrac{x}{2}\right)=\dfrac{1+t^2}{2}\)
and the chain rule:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{d}{dx}\left[\dfrac{2}{\sqrt{3}}\arctan\left(\dfrac{t}{\sqrt{3}}\right)\right]=\dfrac{2}{\sqrt{3}}\cdot\dfrac{1}{1+t^2/3}\cdot\dfrac{1}{\sqrt{3}}\cdot\dfrac{1+t^2}{2}=\dfrac{1+t^2}{3+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 11.} Compare with the integrand:
\(\dfrac{1}{2+\cos x}=\dfrac{1+t^2}{3+t^2}\) from step 5 (the reciprocal
of \(\dfrac{t^2+3}{1+t^2}\)). The two agree, so the antiderivative is
correct. The substitution turned an integral with no obvious pattern
into a routine arctangent integral.

\textbf{Answer.}
\(\dfrac{2}{\sqrt{3}}\arctan\left(\dfrac{\tan(x/2)}{\sqrt{3}}\right)+C\)

\end{examplebox}

\begin{examplebox}{12}

\textit{Level: Challenge. Weierstrass substitution leading to a logarithm}\par\smallskip

Evaluate \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int \dfrac{1}{4+5\sin x}\,dx.$\end{adjustbox}\par\noindent 

\textbf{Step 1.} The integrand is a rational function of \(\sin x\)
alone with no power to peel off, so use the Weierstrass substitution
\(t=\tan\left(\dfrac{x}{2}\right)\), for which
\(\sin x=\dfrac{2t}{1+t^2}\) and \(dx=\dfrac{2\,dt}{1+t^2}\). (The
identity for sine comes from
\(\sin x=2\sin\left(\dfrac{x}{2}\right)\cos\left(\dfrac{x}{2}\right)\)
divided by
\(1=\cos^2\left(\dfrac{x}{2}\right)+\sin^2\left(\dfrac{x}{2}\right)\),
then dividing top and bottom by \(\cos^2\left(\dfrac{x}{2}\right)\).)

\smallskip

\textbf{Step 2.} Rewrite the denominator over the common denominator
\(1+t^2\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$4+5\sin x=4+\dfrac{10t}{1+t^2}=\dfrac{4(1+t^2)+10t}{1+t^2}=\dfrac{4t^2+10t+4}{1+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Substitute into the integral and take the reciprocal of
the denominator:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1+t^2}{4t^2+10t+4}\cdot\dfrac{2\,dt}{1+t^2}=\int\dfrac{2\,dt}{4t^2+10t+4}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Cancel the factor \(1+t^2\) and divide numerator and
denominator by \(2\): \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{dt}{2t^2+5t+2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Decide arctangent or logarithm by the discriminant of
\(2t^2+5t+2\): \(b^2-4ac=25-16=9>0\). It is positive, so the quadratic
factors over the real numbers and we expect a logarithm rather than an
arctangent.

\smallskip

\textbf{Step 6.} Factor: \(2t^2+5t+2=(2t+1)(t+2)\). Check by expanding:
\((2t+1)(t+2)=2t^2+4t+t+2=2t^2+5t+2\).

\smallskip

\textbf{Step 7.} Set up partial fractions:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{1}{(2t+1)(t+2)}=\dfrac{A}{2t+1}+\dfrac{B}{t+2},\qquad\text{so}\qquad 1=A(t+2)+B(2t+1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 8.} Substitute \(t=-2\): \(1=A(0)+B(-4+1)=-3B\), so
\(B=-\dfrac{1}{3}\).

\smallskip

\textbf{Step 9.} Substitute \(t=-\dfrac{1}{2}\):
\(1=A\left(\dfrac{3}{2}\right)+B(0)\), so \(A=\dfrac{2}{3}\). Check by
recombining:
\(\dfrac{2}{3}(t+2)-\dfrac{1}{3}(2t+1)=\dfrac{2t+4-2t-1}{3}=1\).

\smallskip

\textbf{Step 10.} Integrate, using
\(\int\dfrac{dt}{at+b}=\dfrac{1}{a}\ln|at+b|\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\left(\dfrac{2/3}{2t+1}-\dfrac{1/3}{t+2}\right)dt=\dfrac{2}{3}\cdot\dfrac{1}{2}\ln|2t+1|-\dfrac{1}{3}\ln|t+2|=\dfrac{1}{3}\ln|2t+1|-\dfrac{1}{3}\ln|t+2|.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 11.} Combine with \(\ln a-\ln b=\ln\dfrac{a}{b}\) and
substitute back \(t=\tan\left(\dfrac{x}{2}\right)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{dx}{4+5\sin x}=\dfrac{1}{3}\ln\left|\dfrac{2\tan(x/2)+1}{\tan(x/2)+2}\right|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 12.} Verify by differentiating. With
\(\dfrac{dt}{dx}=\dfrac{1+t^2}{2}\):
\(\dfrac{d}{dx}\left[\dfrac{1}{3}\ln\left|\dfrac{2t+1}{t+2}\right|\right]=\dfrac{1}{3}\left(\dfrac{2}{2t+1}-\dfrac{1}{t+2}\right)\dfrac{1+t^2}{2}=\dfrac{1}{(2t+1)(t+2)}\cdot\dfrac{1+t^2}{2}=\dfrac{1+t^2}{4t^2+10t+4}\),
and this equals \(\dfrac{1}{4+5\sin x}\) by step 2.

\textbf{Answer.}
\(\dfrac{1}{3}\ln\left|\dfrac{2\tan(x/2)+1}{\tan(x/2)+2}\right|+C\)

\end{examplebox}

\sectionbanner{Practice Problems}

\vspace{6pt}\noindent{\bfseries\large Trigonometric Integrals}\par\vspace{2pt}

**1.** Evaluate (a) $\displaystyle\int \sin^{10}x\cos x\,dx$ and (b) $\displaystyle\int\sin^{10}x\cos^7x\,dx$. Identify which technique each needs.

\worklines{6}
\vspace{6pt}

**2.** Evaluate $\displaystyle\int \sec^2 x\tan^3 x\,dx$.

\worklines{4}
\vspace{6pt}

**3.** Evaluate $\displaystyle\int \tan^3 x\,dx$.

\worklines{6}
\vspace{6pt}

**4.** Evaluate $\displaystyle\int_0^{\pi/2}\cos^3 x\,dx$.

\worklines{6}
\vspace{6pt}

**5.** Evaluate $\displaystyle\int_0^{\pi}\cos^2 x\,dx$.

\worklines{6}
\vspace{6pt}

**6.** Evaluate $\displaystyle\int \tan^4 x\,dx$.

\worklines{6}
\vspace{6pt}

**7.** Evaluate $\displaystyle\int \sin^4 x\,dx$. (Both powers are even, so apply the half-angle identity twice.)

\worklines{8}
\vspace{6pt}

**8.** State which substitution ($u=\tan x$ or $u=\sec x$) is appropriate for $\displaystyle\int \sec^5 x\tan^3 x\,dx$ and explain why, using the rules for $\int\sec^n x\tan^m x\,dx$. Then evaluate the integral.

\worklines{8}
\vspace{6pt}

**9.** Evaluate $\displaystyle\int \sin^2 x\cos^4 x\,dx$.

\worklines{8}
\vspace{6pt}

**10.** A student claims that $\displaystyle\int \sin^3 x\,dx = -\cos x - \dfrac{\cos^3 x}{3} + C$, using the step $\sin^3 x = \sin x\,(1+\cos^2 x)$. Find the error and give the correct result.

\worklines{8}
\vspace{6pt}

\vspace{6pt}\noindent{\bfseries\large Partial Fractions}\par\vspace{2pt}

**11.** Factor the denominator completely and evaluate $$\int\dfrac{1}{x^2+3x}\,dx.$$

\worklines{4}
\vspace{6pt}

**12.** Factor the denominator completely and evaluate $$\int\dfrac{1}{x^3-x}\,dx.$$

\worklines{6}
\vspace{6pt}

**13.** Evaluate $$\int\dfrac{5x+1}{2x^2+5x-3}\,dx.$$

\worklines{6}
\vspace{6pt}

**14.** A student evaluates $\displaystyle\int\dfrac{3x+1}{(x-1)(x+2)}\,dx$ as follows. They write $\dfrac{3x+1}{(x-1)(x+2)}=\dfrac{A}{x-1}+\dfrac{B}{x+2}$, then use the cover-up shortcut: at $x=1$ they compute $A=3(1)+1=4$, and at $x=-2$ they compute $B=3(-2)+1=-5$. They conclude that the integral equals $4\ln|x-1|-5\ln|x+2|+C$. Find the error and give the correct result.

\worklines{6}
\vspace{6pt}

**15.** Evaluate the definite integral $$\int_2^3\dfrac{1}{x^2-1}\,dx$$ and give the exact value as a single logarithm.

\worklines{6}
\vspace{6pt}

**16.** Evaluate $$\int\dfrac{3x^2+2}{x^2+1}\,dx.$$

\worklines{4}
\vspace{6pt}

**17.** Evaluate $$\int\dfrac{x+1}{x^2(x-2)}\,dx.$$

\worklines{8}
\vspace{6pt}

**18.** Evaluate $$\int\dfrac{2x}{(x^2+1)(x-1)}\,dx.$$

\worklines{8}
\vspace{6pt}

**19.** Evaluate $$\int\dfrac{x^4+3x^2-x+1}{(x-1)(x^2+1)}\,dx.$$

\worklines{8}
\vspace{6pt}

\vspace{6pt}\noindent{\bfseries\large The Weierstrass Substitution}\par\vspace{2pt}

**20.** Use $t=\tan\left(\dfrac{x}{2}\right)$ to evaluate $$\int\dfrac{1}{1+\sin x}\,dx.$$

\worklines{6}
\vspace{6pt}

**21.** Use $t=\tan\left(\dfrac{x}{2}\right)$ to evaluate $$\int_0^{\pi/2}\dfrac{1}{1+\sin x+\cos x}\,dx.$$

\worklines{6}
\vspace{6pt}

**22.** Use $t=\tan\left(\dfrac{x}{2}\right)$ to evaluate $$\int\dfrac{1}{3+5\cos x}\,dx,$$ and simplify the resulting expression fully.

\worklines{8}
\vspace{6pt}

**23.** Use $t=\tan\left(\dfrac{x}{2}\right)$ to evaluate $$\int\dfrac{1}{2+\sin x}\,dx.$$

\worklines{8}
\vspace{6pt}

**24.** Show that $\displaystyle\int\sec x\,dx$ can be evaluated with the substitution $t=\tan\left(\dfrac{x}{2}\right)$, and confirm that the result agrees with the memorised formula $\ln|\sec x+\tan x|+C$.

\worklines{8}
\vspace{6pt}

\vspace{6pt}\noindent{\bfseries\large Mixed Technique Identification}\par\vspace{2pt}

**25.** For each integral, state which single technique from Weeks 3 and 4 (substitution, integration by parts, trig-power identities, partial fractions, or the Weierstrass substitution) is the most efficient, explain why, and then evaluate it: (a) $\displaystyle\int\dfrac{x}{x^2-9}\,dx$; (b) $\displaystyle\int x^2\cos(x^3)\,dx$; (c) $\displaystyle\int\dfrac{1}{\sin x-\cos x}\,dx$; (d) $\displaystyle\int\sec^6x\,dx$.

\worklines{8}
\vspace{6pt}

**26.** For each integral, name the most efficient single technique (substitution, integration by parts, trig-power identities, partial fractions, or the Weierstrass substitution) and then evaluate it: (a) $\displaystyle\int x\cos x\,dx$; (b) $\displaystyle\int\dfrac{1}{x^2-4x+3}\,dx$; (c) $\displaystyle\int\cos^3x\,dx$.

\worklines{8}
\vspace{6pt}

