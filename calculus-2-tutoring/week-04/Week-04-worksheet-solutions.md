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

*Worked-solutions version: every step of each solution is shown in green beneath its problem.*

\vspace{6pt}\noindent{\bfseries\large Trigonometric Integrals}\par\vspace{2pt}

**1.** Evaluate (a) $\displaystyle\int \sin^{10}x\cos x\,dx$ and (b) $\displaystyle\int\sin^{10}x\cos^7x\,dx$. Identify which technique each needs.

\begin{solbox}\sollabel

\textbf{Step 1.} Part (a). The integrand \(\sin^{10}x\cos x\) contains
\(\cos x\,dx\), which is exactly the differential of \(\sin x\). So the
direct substitution \(u = \sin x\) works with no rewriting.

\smallskip

\textbf{Step 2.} Set \(u = \sin x\), so \(du = \cos x\,dx\). Then
\(\sin^{10}x = u^{10}\) and the integral is \(\int u^{10}\,du\).

\smallskip

\textbf{Step 3.} Apply the power rule:
\(\int u^{10}\,du = \dfrac{u^{11}}{11} + C\), so (a) equals
\(\dfrac{\sin^{11}x}{11} + C\).

\smallskip

\textbf{Step 4.} Part (b). The power of cosine is \(7\) (odd), so we
peel off one factor: \(\cos^7 x = \cos^6 x\cdot\cos x\). The single
\(\cos x\) will supply \(du\).

\smallskip

\textbf{Step 5.} Write the remaining even power as a power of
\(\cos^2 x\) and use \(\cos^2 x = 1 - \sin^2 x\) (from
\(\sin^2 x+\cos^2 x = 1\)):
\(\cos^6 x = (\cos^2 x)^3 = (1-\sin^2 x)^3\).

\smallskip

\textbf{Step 6.} The integral is
\(\int \sin^{10}x\,(1-\sin^2 x)^3\cos x\,dx\). Substitute
\(u = \sin x\), \(du = \cos x\,dx\): \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int u^{10}(1-u^2)^3\,du.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Expand \((1-u^2)^3\) with
\((a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3\):
\((1-u^2)^3 = 1 - 3u^2 + 3u^4 - u^6\).

\smallskip

\textbf{Step 8.} Multiply by \(u^{10}\):
\(u^{10} - 3u^{12} + 3u^{14} - u^{16}\).

\smallskip

\textbf{Step 9.} Integrate term by term:
\(\dfrac{u^{11}}{11} - \dfrac{3u^{13}}{13} + \dfrac{3u^{15}}{15} - \dfrac{u^{17}}{17} + C\),
and \(\dfrac{3}{15} = \dfrac15\).

\smallskip

\textbf{Step 10.} Back-substitute \(u = \sin x\): (b) equals
\(\dfrac{\sin^{11}x}{11} - \dfrac{3\sin^{13}x}{13} + \dfrac{\sin^{15}x}{5} - \dfrac{\sin^{17}x}{17} + C\).

\smallskip

\textbf{Step 11.} Verify (a):
\(\dfrac{d}{dx}\left[\dfrac{\sin^{11}x}{11}\right] = \sin^{10}x\cos x\).
Verify (b) by differentiating each term: each gives
\(\sin^{k-1}x\cos x\) times its coefficient times \(k\) over \(k\), and
the sum is
\(\cos x\,(\sin^{10}x - 3\sin^{12}x + 3\sin^{14}x - \sin^{16}x) = \cos x\sin^{10}x(1-\sin^2x)^3\).

\textbf{Answer.} (a) \(\dfrac{\sin^{11}x}{11} + C\) (substitution
\(u=\sin x\)). (b)
\(\dfrac{\sin^{11}x}{11} - \dfrac{3\sin^{13}x}{13} + \dfrac{\sin^{15}x}{5} - \dfrac{\sin^{17}x}{17} + C\)
(peel off one cosine, odd power).
\end{solbox}
\vspace{4pt}

**2.** Evaluate $\displaystyle\int \sec^2 x\tan^3 x\,dx$.

\begin{solbox}\sollabel

\textbf{Step 1.} Identify the pattern: the integrand contains
\(\sec^2 x\), and \(\dfrac{d}{dx}[\tan x] = \sec^2 x\). So
\(\sec^2 x\,dx\) is the differential of \(\tan x\), and the rest of the
integrand, \(\tan^3 x\), is a function of \(\tan x\).

\smallskip

\textbf{Step 2.} Choose the substitution \(u = \tan x\).

\smallskip

\textbf{Step 3.} Differentiate: \(du = \sec^2 x\,dx\).

\smallskip

\textbf{Step 4.} Replace \(\tan^3 x\) by \(u^3\) and \(\sec^2 x\,dx\) by
\(du\): the integral becomes \(\int u^3\,du\).

\smallskip

\textbf{Step 5.} Apply the power rule
\(\int u^k\,du = \dfrac{u^{k+1}}{k+1}\) with \(k=3\):
\(\dfrac{u^4}{4} + C\).

\smallskip

\textbf{Step 6.} Back-substitute \(u = \tan x\):
\(\dfrac{\tan^4 x}{4} + C\).

\smallskip

\textbf{Step 7.} Verify by the chain rule:
\(\dfrac{d}{dx}\left[\dfrac{\tan^4 x}{4}\right] = \dfrac{4\tan^3 x\cdot\sec^2 x}{4} = \sec^2 x\tan^3 x\),
the original integrand.

\textbf{Answer.} \(\dfrac{\tan^4 x}{4} + C\)
\end{solbox}
\vspace{4pt}

**3.** Evaluate $\displaystyle\int \tan^3 x\,dx$.

\begin{solbox}\sollabel

\textbf{Step 1.} The integrand has no secant factor, so the sec/tan
rules do not apply directly. Instead create a \(\sec^2 x\) factor using
the identity \(\tan^2 x = \sec^2 x - 1\) (from
\(\tan^2 x + 1 = \sec^2 x\)).

\smallskip

\textbf{Step 2.} Split off one tangent:
\(\tan^3 x = \tan x\cdot\tan^2 x\).

\smallskip

\textbf{Step 3.} Replace \(\tan^2 x\):
\(\tan^3 x = \tan x(\sec^2 x - 1)\).

\smallskip

\textbf{Step 4.} Distribute:
\(\tan x(\sec^2 x - 1) = \tan x\sec^2 x - \tan x\). So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\tan^3 x\,dx = \int \tan x\sec^2 x\,dx - \int \tan x\,dx.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} First integral: let \(u = \tan x\),
\(du = \sec^2 x\,dx\). Then
\(\int \tan x\sec^2 x\,dx = \int u\,du = \dfrac{u^2}{2} = \dfrac{\tan^2 x}{2}\).

\smallskip

\textbf{Step 6.} Second integral: write
\(\tan x = \dfrac{\sin x}{\cos x}\) and let \(w = \cos x\),
\(dw = -\sin x\,dx\). Then
\(\int\dfrac{\sin x}{\cos x}\,dx = -\int\dfrac{dw}{w} = -\ln|w| = -\ln|\cos x|\).

\smallskip

\textbf{Step 7.} Rewrite using
\(-\ln|\cos x| = \ln\left|\dfrac{1}{\cos x}\right| = \ln|\sec x|\). So
\(\int \tan x\,dx = \ln|\sec x| + C\).

\smallskip

\textbf{Step 8.} Combine, remembering the minus sign in front of the
second integral: \par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{\tan^2 x}{2} - \ln|\sec x| + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Verify:
\(\dfrac{d}{dx}\left[\dfrac{\tan^2 x}{2}\right] = \tan x\sec^2 x\) and
\(\dfrac{d}{dx}\left[\ln|\sec x|\right] = \dfrac{\sec x\tan x}{\sec x} = \tan x\).

\smallskip

\textbf{Step 10.} The difference is
\(\tan x\sec^2 x - \tan x = \tan x(\sec^2 x - 1) = \tan x\cdot\tan^2 x = \tan^3 x\),
as required.

\textbf{Answer.} \(\dfrac{\tan^2 x}{2} - \ln|\sec x| + C\)
\end{solbox}
\vspace{4pt}

**4.** Evaluate $\displaystyle\int_0^{\pi/2}\cos^3 x\,dx$.

\begin{solbox}\sollabel

\textbf{Step 1.} The power of cosine is \(3\) (odd), so peel off one
factor: \(\cos^3 x = \cos^2 x\cdot\cos x\).

\smallskip

\textbf{Step 2.} Convert the even power with
\(\cos^2 x = 1 - \sin^2 x\): \(\cos^3 x = (1-\sin^2 x)\cos x\).

\smallskip

\textbf{Step 3.} Choose \(u = \sin x\), so \(du = \cos x\,dx\).

\smallskip

\textbf{Step 4.} Change the limits of integration to match the new
variable. When \(x = 0\): \(u = \sin 0 = 0\). When
\(x = \dfrac{\pi}{2}\): \(u = \sin\dfrac{\pi}{2} = 1\).

\smallskip

\textbf{Step 5.} Rewrite the definite integral entirely in \(u\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int_0^{1}(1-u^2)\,du.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Find an antiderivative:
\(\int (1-u^2)\,du = u - \dfrac{u^3}{3}\).

\smallskip

\textbf{Step 7.} Evaluate at the upper limit \(u=1\):
\(1 - \dfrac13 = \dfrac23\).

\smallskip

\textbf{Step 8.} Evaluate at the lower limit \(u=0\): \(0 - 0 = 0\).

\smallskip

\textbf{Step 9.} Subtract (upper minus lower):
\(\dfrac23 - 0 = \dfrac23\).

\smallskip

\textbf{Step 10.} Sanity check: \(\cos^3 x\) is between \(0\) and \(1\)
on \(\left[0,\dfrac{\pi}{2}\right]\), an interval of length about
\(1.57\), and \(\cos^3 x \le \cos x\) whose integral is \(1\). The value
\(\dfrac23\approx 0.667\) is below \(1\) and positive, which is
consistent.

\textbf{Answer.} \(\dfrac{2}{3}\)
\end{solbox}
\vspace{4pt}

**5.** Evaluate $\displaystyle\int_0^{\pi}\cos^2 x\,dx$.

\begin{solbox}\sollabel

\textbf{Step 1.} Both powers are even (\(\cos^2 x\) and \(\sin^0 x\)),
so use the half-angle identity \(\cos^2 x = \dfrac{1+\cos 2x}{2}\) (from
\(\cos 2x = 2\cos^2 x - 1\)).

\smallskip

\textbf{Step 2.} Rewrite:
\(\displaystyle\int_0^{\pi}\cos^2 x\,dx = \int_0^{\pi}\dfrac{1+\cos 2x}{2}\,dx\).

\smallskip

\textbf{Step 3.} Find an antiderivative of \(\dfrac{1+\cos 2x}{2}\): the
term \(\dfrac12\) gives \(\dfrac{x}{2}\), and \(\dfrac{\cos 2x}{2}\)
gives \(\dfrac12\cdot\dfrac{\sin 2x}{2} = \dfrac{\sin 2x}{4}\)
(substitution \(w=2x\), \(dx=\dfrac{dw}{2}\)).

\smallskip

\textbf{Step 4.} So \(F(x) = \dfrac{x}{2} + \dfrac{\sin 2x}{4}\). No
substitution was made in the definite integral itself, so the limits
stay \(0\) and \(\pi\).

\smallskip

\textbf{Step 5.} Evaluate at the upper limit:
\(F(\pi) = \dfrac{\pi}{2} + \dfrac{\sin 2\pi}{4} = \dfrac{\pi}{2} + 0 = \dfrac{\pi}{2}\).

\smallskip

\textbf{Step 6.} Evaluate at the lower limit:
\(F(0) = 0 + \dfrac{\sin 0}{4} = 0\).

\smallskip

\textbf{Step 7.} Subtract: \(F(\pi) - F(0) = \dfrac{\pi}{2}\).

\smallskip

\textbf{Step 8.} Cross-check by symmetry: \(\sin^2 x + \cos^2 x = 1\),
so \(\int_0^\pi \sin^2 x\,dx + \int_0^\pi\cos^2 x\,dx = \pi\). Over a
full half-period the two integrals are equal, so each is
\(\dfrac{\pi}{2}\), in agreement.

\textbf{Answer.} \(\dfrac{\pi}{2}\)
\end{solbox}
\vspace{4pt}

**6.** Evaluate $\displaystyle\int \tan^4 x\,dx$.

\begin{solbox}\sollabel

\textbf{Step 1.} There is no secant factor, so create one with
\(\tan^2 x = \sec^2 x - 1\). Split \(\tan^4 x = \tan^2 x\cdot\tan^2 x\).

\smallskip

\textbf{Step 2.} Replace only one of the two factors:
\(\tan^4 x = \tan^2 x(\sec^2 x - 1)\).

\smallskip

\textbf{Step 3.} Distribute: \(\tan^4 x = \tan^2 x\sec^2 x - \tan^2 x\).

\smallskip

\textbf{Step 4.} Apply the identity once more to the leftover
\(\tan^2 x\): \(\tan^2 x = \sec^2 x - 1\), so
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\tan^4 x = \tan^2 x\sec^2 x - \sec^2 x + 1.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Integrate the first term with \(u = \tan x\),
\(du = \sec^2 x\,dx\):
\(\int \tan^2 x\sec^2 x\,dx = \int u^2\,du = \dfrac{u^3}{3} = \dfrac{\tan^3 x}{3}\).

\smallskip

\textbf{Step 6.} Integrate the second term using
\(\dfrac{d}{dx}[\tan x] = \sec^2 x\): \(\int \sec^2 x\,dx = \tan x\), so
with its minus sign this contributes \(-\tan x\).

\smallskip

\textbf{Step 7.} Integrate the third term: \(\int 1\,dx = x\).

\smallskip

\textbf{Step 8.} Add the pieces:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{\tan^3 x}{3} - \tan x + x + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Verify: the derivative is
\(\tan^2 x\sec^2 x - \sec^2 x + 1 = \sec^2 x(\tan^2 x - 1) + 1\). Using
\(\sec^2 x = \tan^2 x + 1\) this is
\((\tan^2 x+1)(\tan^2 x-1) + 1 = \tan^4 x - 1 + 1 = \tan^4 x\), as
required.

\textbf{Answer.} \(\dfrac{\tan^3 x}{3} - \tan x + x + C\)
\end{solbox}
\vspace{4pt}

**7.** Evaluate $\displaystyle\int \sin^4 x\,dx$. (Both powers are even, so apply the half-angle identity twice.)

\begin{solbox}\sollabel

\textbf{Step 1.} Both exponents are even (\(\sin^4 x\), \(\cos^0 x\)),
so use the half-angle identity \(\sin^2 x = \dfrac{1-\cos 2x}{2}\) (from
\(\cos 2x = 1 - 2\sin^2 x\)).

\smallskip

\textbf{Step 2.} Write
\(\sin^4 x = (\sin^2 x)^2 = \left(\dfrac{1-\cos 2x}{2}\right)^2\).

\smallskip

\textbf{Step 3.} Square, using \((a-b)^2 = a^2 - 2ab + b^2\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sin^4 x = \dfrac{1 - 2\cos 2x + \cos^2 2x}{4}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} The term \(\cos^2 2x\) is again an even power. Use
\(\cos^2\theta = \dfrac{1+\cos 2\theta}{2}\) with \(\theta = 2x\):
\(\cos^2 2x = \dfrac{1+\cos 4x}{2}\).

\smallskip

\textbf{Step 5.} Substitute and distribute the \(\dfrac14\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sin^4 x = \dfrac14 - \dfrac{\cos 2x}{2} + \dfrac18 + \dfrac{\cos 4x}{8}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Combine constants: \(\dfrac14 + \dfrac18 = \dfrac38\).
So \(\sin^4 x = \dfrac38 - \dfrac{\cos 2x}{2} + \dfrac{\cos 4x}{8}\).

\smallskip

\textbf{Step 7.} Integrate term by term:
\(\int\dfrac38\,dx = \dfrac{3x}{8}\);
\(\int -\dfrac{\cos 2x}{2}\,dx = -\dfrac12\cdot\dfrac{\sin 2x}{2} = -\dfrac{\sin 2x}{4}\);
\(\int\dfrac{\cos 4x}{8}\,dx = \dfrac18\cdot\dfrac{\sin 4x}{4} = \dfrac{\sin 4x}{32}\).

\smallskip

\textbf{Step 8.} Combine:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{3x}{8} - \dfrac{\sin 2x}{4} + \dfrac{\sin 4x}{32} + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Verify: the derivative is
\(\dfrac38 - \dfrac{\cos 2x}{2} + \dfrac{\cos 4x}{8}\). At
\(x = \dfrac{\pi}{2}\) this is
\(\dfrac38 + \dfrac12 + \dfrac18 = 1 = \sin^4\dfrac{\pi}{2}\), and at
\(x=0\) it is \(\dfrac38 - \dfrac12 + \dfrac18 = 0 = \sin^4 0\).

\textbf{Answer.}
\(\dfrac{3x}{8} - \dfrac{\sin 2x}{4} + \dfrac{\sin 4x}{32} + C\)
\end{solbox}
\vspace{4pt}

**8.** State which substitution ($u=\tan x$ or $u=\sec x$) is appropriate for $\displaystyle\int \sec^5 x\tan^3 x\,dx$ and explain why, using the rules for $\int\sec^n x\tan^m x\,dx$. Then evaluate the integral.

\begin{solbox}\sollabel

\textbf{Step 1.} Test the even-secant rule: it needs \(n\) (the secant
power) to be even so that a factor \(\sec^2 x\) can be peeled off for
\(u=\tan x\). Here \(n = 5\) is odd, so that rule fails.

\smallskip

\textbf{Step 2.} Test the odd-tangent rule: it needs \(m\) (the tangent
power) to be odd so that one factor \(\sec x\tan x\) can be peeled off
for \(u=\sec x\). Here \(m = 3\) is odd and \(n\ge1\), so this rule
applies. The substitution is \(u = \sec x\).

\smallskip

\textbf{Step 3.} Peel off \(\sec x\tan x\):
\(\sec^5 x\tan^3 x = \sec^4 x\,\tan^2 x\cdot(\sec x\tan x)\). Check:
\(\sec^4\cdot\sec = \sec^5\) and \(\tan^2\cdot\tan = \tan^3\).

\smallskip

\textbf{Step 4.} Convert the even tangent power using
\(\tan^2 x = \sec^2 x - 1\):
\(\sec^5 x\tan^3 x = \sec^4 x(\sec^2 x - 1)(\sec x\tan x)\).

\smallskip

\textbf{Step 5.} Substitute \(u = \sec x\), \(du = \sec x\tan x\,dx\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int u^4(u^2-1)\,du.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Expand: \(u^4(u^2 - 1) = u^6 - u^4\).

\smallskip

\textbf{Step 7.} Integrate with the power rule:
\(\dfrac{u^7}{7} - \dfrac{u^5}{5} + C\).

\smallskip

\textbf{Step 8.} Back-substitute \(u = \sec x\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{\sec^7 x}{7} - \dfrac{\sec^5 x}{5} + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Verify:
\(\dfrac{d}{dx}\left[\dfrac{\sec^7 x}{7}\right] = \sec^6 x\cdot\sec x\tan x = \sec^7 x\tan x\)
and \(\dfrac{d}{dx}\left[\dfrac{\sec^5 x}{5}\right] = \sec^5 x\tan x\).

\smallskip

\textbf{Step 10.} Subtract:
\(\sec^7 x\tan x - \sec^5 x\tan x = \sec^5 x\tan x(\sec^2 x - 1) = \sec^5 x\tan^3 x\),
the original integrand.

\textbf{Answer.} Use \(u=\sec x\) (tangent power \(3\) is odd; secant
power \(5\) is odd so \(u=\tan x\) fails). Result:
\(\dfrac{\sec^7 x}{7} - \dfrac{\sec^5 x}{5} + C\)
\end{solbox}
\vspace{4pt}

**9.** Evaluate $\displaystyle\int \sin^2 x\cos^4 x\,dx$.

\begin{solbox}\sollabel

\textbf{Step 1.} Both exponents are even, so no factor can be peeled off
for a substitution. Combine part of the product first:
\(\sin^2 x\cos^4 x = (\sin x\cos x)^2\cos^2 x\).

\smallskip

\textbf{Step 2.} Use \(\sin 2x = 2\sin x\cos x\), so
\(\sin x\cos x = \dfrac{\sin 2x}{2}\) and
\((\sin x\cos x)^2 = \dfrac{\sin^2 2x}{4}\).

\smallskip

\textbf{Step 3.} Use \(\cos^2 x = \dfrac{1+\cos 2x}{2}\) for the
remaining factor, so
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sin^2 x\cos^4 x = \dfrac{\sin^2 2x}{4}\cdot\dfrac{1+\cos 2x}{2} = \dfrac{\sin^2 2x\,(1+\cos 2x)}{8}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Distribute:
\(\sin^2 x\cos^4 x = \dfrac{\sin^2 2x}{8} + \dfrac{\sin^2 2x\cos 2x}{8}\).

\smallskip

\textbf{Step 5.} First term: use
\(\sin^2\theta = \dfrac{1-\cos 2\theta}{2}\) with \(\theta = 2x\),
giving \(\sin^2 2x = \dfrac{1-\cos 4x}{2}\). So
\(\dfrac{\sin^2 2x}{8} = \dfrac{1-\cos 4x}{16}\).

\smallskip

\textbf{Step 6.} Integrate it:
\(\int \dfrac{1-\cos 4x}{16}\,dx = \dfrac{x}{16} - \dfrac{1}{16}\cdot\dfrac{\sin 4x}{4} = \dfrac{x}{16} - \dfrac{\sin 4x}{64}\).

\smallskip

\textbf{Step 7.} Second term: \(\int\dfrac{\sin^2 2x\cos 2x}{8}\,dx\).
It contains \(\cos 2x\) (the derivative of \(\sin 2x\) up to a
constant), so let \(w = \sin 2x\), \(dw = 2\cos 2x\,dx\), so
\(\cos 2x\,dx = \dfrac{dw}{2}\).

\smallskip

\textbf{Step 8.} Substitute:
\(\dfrac18\int w^2\cdot\dfrac{dw}{2} = \dfrac{1}{16}\cdot\dfrac{w^3}{3} = \dfrac{w^3}{48} = \dfrac{\sin^3 2x}{48}\).

\smallskip

\textbf{Step 9.} Add both results and the constant:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{x}{16} - \dfrac{\sin 4x}{64} + \dfrac{\sin^3 2x}{48} + C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} Verify at \(x = \dfrac{\pi}{4}\): the integrand is
\(\sin^2\dfrac{\pi}{4}\cos^4\dfrac{\pi}{4} = \dfrac12\cdot\dfrac14 = \dfrac18\).
The derivative of the answer is
\(\dfrac1{16} - \dfrac{\cos 4x}{16} + \dfrac{\sin^2 2x\cos 2x}{8}\),
which at \(x=\dfrac{\pi}{4}\) is
\(\dfrac{1}{16} + \dfrac{1}{16} + 0 = \dfrac18\). They agree.

\textbf{Answer.}
\(\dfrac{x}{16} - \dfrac{\sin 4x}{64} + \dfrac{\sin^3 2x}{48} + C\)
\end{solbox}
\vspace{4pt}

**10.** A student claims that $\displaystyle\int \sin^3 x\,dx = -\cos x - \dfrac{\cos^3 x}{3} + C$, using the step $\sin^3 x = \sin x\,(1+\cos^2 x)$. Find the error and give the correct result.

\begin{solbox}\sollabel

\textbf{Step 1.} Examine the student's step
\(\sin^3 x = \sin x\,(1+\cos^2 x)\). It would need
\(\sin^2 x = 1 + \cos^2 x\).

\smallskip

\textbf{Step 2.} The correct Pythagorean identity is
\(\sin^2 x + \cos^2 x = 1\), so \(\sin^2 x = 1 - \cos^2 x\). The student
used a plus sign where a minus sign belongs.

\smallskip

\textbf{Step 3.} Test the student's claim numerically at
\(x = \dfrac{\pi}{4}\): \(\sin^2\dfrac{\pi}{4} = \dfrac12\) but
\(1 + \cos^2\dfrac{\pi}{4} = 1+\dfrac12 = \dfrac32\). These are not
equal, so the step is false.

\smallskip

\textbf{Step 4.} Redo the problem. The sine power \(3\) is odd, so peel
off one factor: \(\sin^3 x = \sin^2 x\cdot\sin x = (1-\cos^2 x)\sin x\).

\smallskip

\textbf{Step 5.} Distribute: \(\sin^3 x = \sin x - \cos^2 x\sin x\), so
\(\int \sin^3 x\,dx = \int \sin x\,dx - \int\cos^2 x\sin x\,dx\).

\smallskip

\textbf{Step 6.} First integral: \(\int\sin x\,dx = -\cos x\).

\smallskip

\textbf{Step 7.} Second integral: let \(u = \cos x\),
\(du = -\sin x\,dx\). Then
\(\int\cos^2 x\sin x\,dx = -\int u^2\,du = -\dfrac{u^3}{3} = -\dfrac{\cos^3 x}{3}\).

\smallskip

\textbf{Step 8.} Combine, remembering the subtraction:
\(-\cos x - \left(-\dfrac{\cos^3 x}{3}\right) = -\cos x + \dfrac{\cos^3 x}{3}\).

\smallskip

\textbf{Step 9.} Verify the correct answer:
\(\dfrac{d}{dx}\left[-\cos x + \dfrac{\cos^3 x}{3}\right] = \sin x + \dfrac{3\cos^2 x(-\sin x)}{3} = \sin x - \cos^2 x\sin x = \sin x(1-\cos^2 x) = \sin^3 x\).

\smallskip

\textbf{Step 10.} Verify that the student's answer fails: its derivative
is \(\sin x + \cos^2 x\sin x = \sin x(1+\cos^2 x)\). At
\(x = \dfrac{\pi}{4}\) this is
\(\dfrac{\sqrt2}{2}\cdot\dfrac32 \approx 1.061\), while
\(\sin^3\dfrac{\pi}{4}\approx 0.354\).

\textbf{Answer.} The error is \(\sin^2 x = 1+\cos^2 x\) (should be
\(1-\cos^2 x\)). Correct result: \(-\cos x + \dfrac{\cos^3 x}{3} + C\)
\end{solbox}
\vspace{4pt}

\vspace{6pt}\noindent{\bfseries\large Partial Fractions}\par\vspace{2pt}

**11.** Factor the denominator completely and evaluate $$\int\dfrac{1}{x^2+3x}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} The numerator has degree \(0\) and the denominator
degree \(2\), so no long division is needed. Factor the denominator by
taking out the common factor \(x\): \(x^2+3x=x(x+3)\).

\smallskip

\textbf{Step 2.} Both factors are distinct linear factors, so each gets
one constant-numerator term:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{1}{x(x+3)}=\dfrac{A}{x}+\dfrac{B}{x+3}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Multiply both sides by \(x(x+3)\): \par\begin{adjustbox}{max width=\boxmathwidth,center}$1=A(x+3)+Bx.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Substitute \(x=0\) (kills the \(B\) term):
\(1=A(3)+0\), so \(A=\dfrac{1}{3}\).

\smallskip

\textbf{Step 5.} Substitute \(x=-3\) (kills the \(A\) term):
\(1=A(0)+B(-3)\), so \(B=-\dfrac{1}{3}\).

\smallskip

\textbf{Step 6.} Check by recombining:
\(\dfrac{1}{3}(x+3)-\dfrac{1}{3}x=\dfrac{x+3-x}{3}=1\), which matches
the left side. So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{1}{x^2+3x}=\dfrac{1}{3}\cdot\dfrac{1}{x}-\dfrac{1}{3}\cdot\dfrac{1}{x+3}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Integrate term by term using
\(\int\dfrac{du}{u}=\ln|u|\) (with \(u=x\) and \(u=x+3\), \(du=dx\)):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1}{x^2+3x}\,dx=\dfrac{1}{3}\ln|x|-\dfrac{1}{3}\ln|x+3|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 8.} Optionally combine with
\(\ln a-\ln b=\ln\dfrac{a}{b}\): the result is
\(\dfrac{1}{3}\ln\left|\dfrac{x}{x+3}\right|+C\).

\smallskip

\textbf{Step 9.} Verify by differentiating:
\(\dfrac{1}{3}\cdot\dfrac{1}{x}-\dfrac{1}{3}\cdot\dfrac{1}{x+3}=\dfrac{1}{3}\cdot\dfrac{(x+3)-x}{x(x+3)}=\dfrac{1}{3}\cdot\dfrac{3}{x(x+3)}=\dfrac{1}{x^2+3x}\).

\textbf{Answer.}
\(\dfrac{1}{3}\ln|x|-\dfrac{1}{3}\ln|x+3|+C=\dfrac{1}{3}\ln\left|\dfrac{x}{x+3}\right|+C\)
\end{solbox}
\vspace{4pt}

**12.** Factor the denominator completely and evaluate $$\int\dfrac{1}{x^3-x}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} The numerator has degree \(0\) and the denominator
degree \(3\), so no long division is needed. Take out the common factor
\(x\): \(x^3-x=x(x^2-1)\).

\smallskip

\textbf{Step 2.} Do not stop there. The factor \(x^2-1\) is a difference
of squares, \(a^2-b^2=(a-b)(a+b)\), so \(x^2-1=(x-1)(x+1)\) and
\par\begin{adjustbox}{max width=\boxmathwidth,center}$x^3-x=x(x-1)(x+1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} There are three distinct linear factors, so three terms
are needed:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{1}{x(x-1)(x+1)}=\dfrac{A}{x}+\dfrac{B}{x-1}+\dfrac{C}{x+1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Multiply both sides by \(x(x-1)(x+1)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$1=A(x-1)(x+1)+Bx(x+1)+Cx(x-1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Substitute \(x=0\): \(1=A(-1)(1)+0+0\), so \(A=-1\).

\smallskip

\textbf{Step 6.} Substitute \(x=1\): \(1=0+B(1)(2)+0\), so
\(B=\dfrac{1}{2}\).

\smallskip

\textbf{Step 7.} Substitute \(x=-1\): \(1=0+0+C(-1)(-2)=2C\), so
\(C=\dfrac{1}{2}\).

\smallskip

\textbf{Step 8.} Check by comparing the \(x^2\) coefficients: expanding
gives \((A+B+C)x^2+(B-C)x-A\), and
\(A+B+C=-1+\dfrac{1}{2}+\dfrac{1}{2}=0\) (left side has no \(x^2\)),
\(B-C=0\) (no \(x\) term), \(-A=1\) (the constant). All three match.

\smallskip

\textbf{Step 9.} Integrate each term with \(\int\dfrac{du}{u}=\ln|u|\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\left(-\dfrac{1}{x}+\dfrac{1/2}{x-1}+\dfrac{1/2}{x+1}\right)dx=-\ln|x|+\dfrac{1}{2}\ln|x-1|+\dfrac{1}{2}\ln|x+1|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} Verify at \(x=2\): the integrand is
\(\dfrac{1}{8-2}=\dfrac{1}{6}\), and the derivative of the answer is
\(-\dfrac{1}{2}+\dfrac{1}{2}\cdot\dfrac{1}{1}+\dfrac{1}{2}\cdot\dfrac{1}{3}=-\dfrac{1}{2}+\dfrac{1}{2}+\dfrac{1}{6}=\dfrac{1}{6}\).

\textbf{Answer.} \(-\ln|x|+\dfrac{1}{2}\ln|x-1|+\dfrac{1}{2}\ln|x+1|+C\)
\end{solbox}
\vspace{4pt}

**13.** Evaluate $$\int\dfrac{5x+1}{2x^2+5x-3}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} The numerator has degree \(1\) and the denominator
degree \(2\), so no long division is needed. First factor the
denominator, whose leading coefficient is \(2\) rather than \(1\).

\smallskip

\textbf{Step 2.} Use the product-of-roots method: multiply the leading
coefficient and constant, \(2\cdot(-3)=-6\), and find two numbers with
product \(-6\) and sum \(5\) (the middle coefficient). They are \(6\)
and \(-1\).

\smallskip

\textbf{Step 3.} Split the middle term: \(2x^2+5x-3=2x^2+6x-x-3\).
Group: \(2x(x+3)-1(x+3)=(2x-1)(x+3)\). Check by expanding:
\((2x-1)(x+3)=2x^2+6x-x-3=2x^2+5x-3\).

\smallskip

\textbf{Step 4.} Two distinct linear factors, so
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{5x+1}{(2x-1)(x+3)}=\dfrac{A}{2x-1}+\dfrac{B}{x+3}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Multiply by \((2x-1)(x+3)\): \par\begin{adjustbox}{max width=\boxmathwidth,center}$5x+1=A(x+3)+B(2x-1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Substitute \(x=\dfrac{1}{2}\) (makes \(2x-1=0\)):
\(5\cdot\dfrac{1}{2}+1=\dfrac{7}{2}=A\left(\dfrac{7}{2}\right)\), so
\(A=1\).

\smallskip

\textbf{Step 7.} Substitute \(x=-3\) (makes \(x+3=0\)):
\(5(-3)+1=-14=B(-6-1)=-7B\), so \(B=2\).

\smallskip

\textbf{Step 8.} Check by recombining:
\(1\cdot(x+3)+2(2x-1)=x+3+4x-2=5x+1\). So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{5x+1}{2x^2+5x-3}=\dfrac{1}{2x-1}+\dfrac{2}{x+3}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Integrate the first term with \(u=2x-1\), \(du=2\,dx\),
so \(dx=\dfrac{du}{2}\):
\(\int\dfrac{dx}{2x-1}=\dfrac{1}{2}\int\dfrac{du}{u}=\dfrac{1}{2}\ln|2x-1|\).
The factor \(\dfrac{1}{2}\) comes from the leading coefficient \(2\) of
the linear factor.

\smallskip

\textbf{Step 10.} Integrate the second term with \(u=x+3\):
\(2\int\dfrac{dx}{x+3}=2\ln|x+3|\).

\smallskip

\textbf{Step 11.} Combine:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{5x+1}{2x^2+5x-3}\,dx=\dfrac{1}{2}\ln|2x-1|+2\ln|x+3|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 12.} Verify by differentiating:
\(\dfrac{d}{dx}\left[\dfrac{1}{2}\ln|2x-1|\right]=\dfrac{1}{2}\cdot\dfrac{2}{2x-1}=\dfrac{1}{2x-1}\)
and \(\dfrac{d}{dx}[2\ln|x+3|]=\dfrac{2}{x+3}\), whose sum is the
decomposition above.

\textbf{Answer.} \(\dfrac{1}{2}\ln|2x-1|+2\ln|x+3|+C\)
\end{solbox}
\vspace{4pt}

**14.** A student evaluates $\displaystyle\int\dfrac{3x+1}{(x-1)(x+2)}\,dx$ as follows. They write $\dfrac{3x+1}{(x-1)(x+2)}=\dfrac{A}{x-1}+\dfrac{B}{x+2}$, then use the cover-up shortcut: at $x=1$ they compute $A=3(1)+1=4$, and at $x=-2$ they compute $B=3(-2)+1=-5$. They conclude that the integral equals $4\ln|x-1|-5\ln|x+2|+C$. Find the error and give the correct result.

\begin{solbox}\sollabel

\textbf{Step 1.} Test the claim first. Pick \(x=0\), where the integrand
is \(\dfrac{3(0)+1}{(0-1)(0+2)}=\dfrac{1}{-2}=-\dfrac{1}{2}\).

\smallskip

\textbf{Step 2.} The derivative of the student answer at \(x=0\) is
\(\dfrac{4}{0-1}-\dfrac{5}{0+2}=-4-\dfrac{5}{2}=-\dfrac{13}{2}\). This
is not \(-\dfrac{1}{2}\), so the claimed antiderivative is wrong.

\smallskip

\textbf{Step 3.} Locate the error. The decomposition shape is correct.
The error is in the value of the coefficients. Clearing denominators
gives \par\begin{adjustbox}{max width=\boxmathwidth,center}$3x+1=A(x+2)+B(x-1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Setting \(x=1\) in this equation gives
\(3(1)+1=A(1+2)+B(0)\), that is \(4=3A\). The student wrote \(A=4\) and
forgot to divide by the value \(x+2=3\) of the remaining factor.

\smallskip

\textbf{Step 5.} Setting \(x=-2\) gives \(3(-2)+1=A(0)+B(-2-1)\), that
is \(-5=-3B\). The student wrote \(B=-5\), forgetting both to divide by
the value \(x-1=-3\) of the remaining factor and the resulting sign.

\smallskip

\textbf{Step 6.} Correct values: \(A=\dfrac{4}{3}\) and
\(B=\dfrac{-5}{-3}=\dfrac{5}{3}\).

\smallskip

\textbf{Step 7.} Check by recombining:
\(\dfrac{4}{3}(x+2)+\dfrac{5}{3}(x-1)=\dfrac{4x+8+5x-5}{3}=\dfrac{9x+3}{3}=3x+1\),
which matches the numerator. (The student version would give
\(4(x+2)-5(x-1)=-x+13\neq 3x+1\).)

\smallskip

\textbf{Step 8.} So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{3x+1}{(x-1)(x+2)}=\dfrac{4/3}{x-1}+\dfrac{5/3}{x+2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Integrate each term with \(\int\dfrac{du}{u}=\ln|u|\)
(\(u=x-1\) and \(u=x+2\), \(du=dx\)):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{3x+1}{(x-1)(x+2)}\,dx=\dfrac{4}{3}\ln|x-1|+\dfrac{5}{3}\ln|x+2|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} Verify at \(x=0\): the derivative of the correct
answer is
\(\dfrac{4}{3}\cdot\dfrac{1}{-1}+\dfrac{5}{3}\cdot\dfrac{1}{2}=-\dfrac{4}{3}+\dfrac{5}{6}=-\dfrac{8}{6}+\dfrac{5}{6}=-\dfrac{1}{2}\),
which equals the integrand value found in the first step.

\textbf{Answer.} Error: the cover-up values were not divided by the
remaining factor (\(A=\dfrac{4}{3}\), \(B=\dfrac{5}{3}\), not \(4\) and
\(-5\)). Correct result: \(\dfrac{4}{3}\ln|x-1|+\dfrac{5}{3}\ln|x+2|+C\)
\end{solbox}
\vspace{4pt}

**15.** Evaluate the definite integral $$\int_2^3\dfrac{1}{x^2-1}\,dx$$ and give the exact value as a single logarithm.

\begin{solbox}\sollabel

\textbf{Step 1.} The numerator has degree \(0\) and the denominator
degree \(2\), so no long division is needed. Factor with the difference
of squares \(a^2-b^2=(a-b)(a+b)\): \(x^2-1=(x-1)(x+1)\).

\smallskip

\textbf{Step 2.} Set up two terms:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{1}{(x-1)(x+1)}=\dfrac{A}{x-1}+\dfrac{B}{x+1},\qquad 1=A(x+1)+B(x-1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Substitute \(x=1\): \(1=A(2)+0\), so
\(A=\dfrac{1}{2}\). Substitute \(x=-1\): \(1=0+B(-2)\), so
\(B=-\dfrac{1}{2}\).

\smallskip

\textbf{Step 4.} Check by recombining:
\(\dfrac{1}{2}(x+1)-\dfrac{1}{2}(x-1)=\dfrac{x+1-x+1}{2}=1\). So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{1}{x^2-1}=\dfrac{1}{2}\cdot\dfrac{1}{x-1}-\dfrac{1}{2}\cdot\dfrac{1}{x+1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Find an antiderivative using
\(\int\dfrac{du}{u}=\ln|u|\):
\(F(x)=\dfrac{1}{2}\ln|x-1|-\dfrac{1}{2}\ln|x+1|=\dfrac{1}{2}\ln\left|\dfrac{x-1}{x+1}\right|\).

\smallskip

\textbf{Step 6.} The integrand is continuous on \([2,3]\) (the
denominator vanishes only at \(x=\pm1\)), and on this interval \(x-1>0\)
and \(x+1>0\), so the absolute values may be dropped.

\smallskip

\textbf{Step 7.} Upper limit \(x=3\):
\(F(3)=\dfrac{1}{2}\ln\dfrac{2}{4}=\dfrac{1}{2}\ln\dfrac{1}{2}\).

\smallskip

\textbf{Step 8.} Lower limit \(x=2\):
\(F(2)=\dfrac{1}{2}\ln\dfrac{1}{3}\).

\smallskip

\textbf{Step 9.} Subtract:
\(F(3)-F(2)=\dfrac{1}{2}\left(\ln\dfrac{1}{2}-\ln\dfrac{1}{3}\right)=\dfrac{1}{2}\ln\left(\dfrac{1}{2}\div\dfrac{1}{3}\right)=\dfrac{1}{2}\ln\dfrac{3}{2}\),
using \(\ln a-\ln b=\ln\dfrac{a}{b}\).

\smallskip

\textbf{Step 10.} Numerical sanity check:
\(\dfrac{1}{2}\ln 1.5\approx\dfrac{1}{2}(0.4055)=0.2027\). The integrand
decreases from \(\dfrac{1}{3}\approx0.333\) at \(x=2\) to
\(\dfrac{1}{8}=0.125\) at \(x=3\) over an interval of length \(1\), and
the midpoint value \(\dfrac{1}{2.5^2-1}\approx0.190\) is close to
\(0.2027\), so the answer is reasonable.

\textbf{Answer.} \(\dfrac{1}{2}\ln\dfrac{3}{2}\approx 0.2027\)
\end{solbox}
\vspace{4pt}

**16.** Evaluate $$\int\dfrac{3x^2+2}{x^2+1}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} Compare degrees: the numerator \(3x^2+2\) and the
denominator \(x^2+1\) both have degree \(2\). Since the numerator degree
is not smaller than the denominator degree, partial fractions cannot be
applied directly; divide first.

\smallskip

\textbf{Step 2.} Long division: the leading terms give
\(\dfrac{3x^2}{x^2}=3\). Multiply back: \(3(x^2+1)=3x^2+3\). Subtract:
\((3x^2+2)-(3x^2+3)=-1\).

\smallskip

\textbf{Step 3.} The remainder \(-1\) has degree \(0<2\), so we stop.
Thus \(3x^2+2=3(x^2+1)-1\).

\smallskip

\textbf{Step 4.} Divide by \(x^2+1\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{3x^2+2}{x^2+1}=3-\dfrac{1}{x^2+1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Check:
\(3-\dfrac{1}{x^2+1}=\dfrac{3(x^2+1)-1}{x^2+1}=\dfrac{3x^2+3-1}{x^2+1}=\dfrac{3x^2+2}{x^2+1}\).

\smallskip

\textbf{Step 6.} The remaining fraction already has an irreducible
denominator and a constant numerator, so no further decomposition is
needed.

\smallskip

\textbf{Step 7.} Integrate term by term: \(\int 3\,dx=3x\) and, by the
standard form
\(\int\dfrac{du}{u^2+a^2}=\dfrac{1}{a}\arctan\left(\dfrac{u}{a}\right)\)
with \(a=1\), \(\int\dfrac{dx}{x^2+1}=\arctan x\).

\smallskip

\textbf{Step 8.} Result:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{3x^2+2}{x^2+1}\,dx=3x-\arctan x+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Verify by differentiating:
\(\dfrac{d}{dx}[3x-\arctan x]=3-\dfrac{1}{1+x^2}=\dfrac{3x^2+3-1}{x^2+1}=\dfrac{3x^2+2}{x^2+1}\).

\textbf{Answer.} \(3x-\arctan x+C\)
\end{solbox}
\vspace{4pt}

**17.** Evaluate $$\int\dfrac{x+1}{x^2(x-2)}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} The numerator has degree \(1\) and the denominator
degree \(3\), so no long division is needed. The denominator is already
factored: \(x^2=(x-0)^2\) is a repeated linear factor and \(x-2\) is a
distinct linear factor.

\smallskip

\textbf{Step 2.} A repeated factor \(x^2\) needs a term for every power
from \(1\) to \(2\), and \(x-2\) needs one term:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{x+1}{x^2(x-2)}=\dfrac{A}{x}+\dfrac{B}{x^2}+\dfrac{C}{x-2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Multiply by \(x^2(x-2)\): \par\begin{adjustbox}{max width=\boxmathwidth,center}$x+1=Ax(x-2)+B(x-2)+Cx^2.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Substitute \(x=0\): \(1=0+B(-2)+0\), so
\(B=-\dfrac{1}{2}\).

\smallskip

\textbf{Step 5.} Substitute \(x=2\): \(3=0+0+C(4)\), so
\(C=\dfrac{3}{4}\).

\smallskip

\textbf{Step 6.} Expand the right side to compare coefficients:
\(Ax^2-2Ax+Bx-2B+Cx^2=(A+C)x^2+(B-2A)x-2B\).

\smallskip

\textbf{Step 7.} Match the \(x^2\) coefficient (left side has \(0\)):
\(A+C=0\), so \(A=-C=-\dfrac{3}{4}\).

\smallskip

\textbf{Step 8.} Check with the \(x\) coefficient:
\(B-2A=-\dfrac{1}{2}+\dfrac{3}{2}=1\), which matches the \(1\) on the
left. Check the constant: \(-2B=1\), which matches. So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{x+1}{x^2(x-2)}=-\dfrac{3/4}{x}-\dfrac{1/2}{x^2}+\dfrac{3/4}{x-2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Integrate the logarithmic terms with
\(\int\dfrac{du}{u}=\ln|u|\): \(-\dfrac{3}{4}\ln|x|\) and
\(\dfrac{3}{4}\ln|x-2|\).

\smallskip

\textbf{Step 10.} Integrate the repeated-factor term with the power
rule:
\(-\dfrac{1}{2}\int x^{-2}\,dx=-\dfrac{1}{2}\cdot\dfrac{x^{-1}}{-1}=\dfrac{1}{2x}\).

\smallskip

\textbf{Step 11.} Combine:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{x+1}{x^2(x-2)}\,dx=-\dfrac{3}{4}\ln|x|+\dfrac{1}{2x}+\dfrac{3}{4}\ln|x-2|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 12.} Verify at \(x=1\): the integrand is
\(\dfrac{2}{1\cdot(-1)}=-2\). The derivative of the answer is
\(-\dfrac{3}{4}\cdot\dfrac{1}{1}-\dfrac{1}{2\cdot1^2}+\dfrac{3}{4}\cdot\dfrac{1}{-1}=-\dfrac{3}{4}-\dfrac{1}{2}-\dfrac{3}{4}=-2\).

\textbf{Answer.}
\(-\dfrac{3}{4}\ln|x|+\dfrac{1}{2x}+\dfrac{3}{4}\ln|x-2|+C\)
\end{solbox}
\vspace{4pt}

**18.** Evaluate $$\int\dfrac{2x}{(x^2+1)(x-1)}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} The numerator has degree \(1\) and the denominator
degree \(3\), so no long division is needed. The factor \(x^2+1\) is
irreducible over the reals and \(x-1\) is a distinct linear factor.

\smallskip

\textbf{Step 2.} The irreducible quadratic needs a linear numerator and
the linear factor a constant:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{2x}{(x^2+1)(x-1)}=\dfrac{Ax+B}{x^2+1}+\dfrac{C}{x-1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Multiply by \((x^2+1)(x-1)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$2x=(Ax+B)(x-1)+C(x^2+1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Substitute \(x=1\) (kills the first term):
\(2=0+C(2)\), so \(C=1\).

\smallskip

\textbf{Step 5.} Expand the right side: \((Ax+B)(x-1)=Ax^2-Ax+Bx-B\), so
\par\begin{adjustbox}{max width=\boxmathwidth,center}$2x=(A+C)x^2+(B-A)x+(C-B).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Match the \(x^2\) coefficient: \(A+C=0\), so \(A=-1\).

\smallskip

\textbf{Step 7.} Match the constant term: \(C-B=0\), so \(B=C=1\).

\smallskip

\textbf{Step 8.} Check with the \(x\) coefficient: \(B-A=1-(-1)=2\),
which matches the \(2\) on the left. So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{2x}{(x^2+1)(x-1)}=\dfrac{-x+1}{x^2+1}+\dfrac{1}{x-1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Check at \(x=0\): left side \(0\); right side
\(\dfrac{1}{1}+\dfrac{1}{-1}=0\). Good.

\smallskip

\textbf{Step 10.} Split the first fraction:
\(\dfrac{-x+1}{x^2+1}=-\dfrac{x}{x^2+1}+\dfrac{1}{x^2+1}\). For
\(\int\dfrac{x}{x^2+1}\,dx\) let \(u=x^2+1\), \(du=2x\,dx\), giving
\(\dfrac{1}{2}\ln(x^2+1)\). For \(\int\dfrac{dx}{x^2+1}\) use the
standard form \(\arctan x\).

\smallskip

\textbf{Step 11.} The third term is \(\int\dfrac{dx}{x-1}=\ln|x-1|\).
Combine:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{2x}{(x^2+1)(x-1)}\,dx=-\dfrac{1}{2}\ln(x^2+1)+\arctan x+\ln|x-1|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 12.} Verify by differentiating:
\(-\dfrac{x}{x^2+1}+\dfrac{1}{x^2+1}+\dfrac{1}{x-1}=\dfrac{-x+1}{x^2+1}+\dfrac{1}{x-1}\),
which is the decomposition just checked.

\textbf{Answer.} \(-\dfrac{1}{2}\ln(x^2+1)+\arctan x+\ln|x-1|+C\)
\end{solbox}
\vspace{4pt}

**19.** Evaluate $$\int\dfrac{x^4+3x^2-x+1}{(x-1)(x^2+1)}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} Compare degrees: the numerator has degree \(4\); the
denominator \((x-1)(x^2+1)\) has degree \(3\). The numerator degree is
not smaller, so we must long-divide first.

\smallskip

\textbf{Step 2.} Expand the denominator:
\((x-1)(x^2+1)=x^3+x-x^2-1=x^3-x^2+x-1\).

\smallskip

\textbf{Step 3.} Divide \(x^4+0x^3+3x^2-x+1\) by \(x^3-x^2+x-1\).
Leading terms: \(\dfrac{x^4}{x^3}=x\). Multiply back:
\(x(x^3-x^2+x-1)=x^4-x^3+x^2-x\). Subtract:
\((x^4+0x^3+3x^2-x+1)-(x^4-x^3+x^2-x)=x^3+2x^2+0x+1\).

\smallskip

\textbf{Step 4.} Next: \(\dfrac{x^3}{x^3}=1\). Multiply back:
\(1\cdot(x^3-x^2+x-1)\). Subtract:
\((x^3+2x^2+0x+1)-(x^3-x^2+x-1)=3x^2-x+2\).

\smallskip

\textbf{Step 5.} The remainder \(3x^2-x+2\) has degree \(2<3\), so the
division stops. The quotient is \(x+1\), and
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{x^4+3x^2-x+1}{(x-1)(x^2+1)}=x+1+\dfrac{3x^2-x+2}{(x-1)(x^2+1)}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Decompose the proper fraction:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{3x^2-x+2}{(x-1)(x^2+1)}=\dfrac{Ax+B}{x^2+1}+\dfrac{C}{x-1},\qquad 3x^2-x+2=(Ax+B)(x-1)+C(x^2+1).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Substitute \(x=1\): \(3-1+2=4=C(2)\), so \(C=2\).

\smallskip

\textbf{Step 8.} Expand the right side: \((A+C)x^2+(B-A)x+(C-B)\). Match
\(x^2\): \(A+C=3\), so \(A=1\). Match the constant: \(C-B=2\), so
\(B=0\).

\smallskip

\textbf{Step 9.} Check with the \(x\) coefficient: \(B-A=0-1=-1\), which
matches the \(-1\) on the left. So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{3x^2-x+2}{(x-1)(x^2+1)}=\dfrac{x}{x^2+1}+\dfrac{2}{x-1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} The full integrand is therefore
\(x+1+\dfrac{x}{x^2+1}+\dfrac{2}{x-1}\).

\smallskip

\textbf{Step 11.} Integrate: \(\int(x+1)\,dx=\dfrac{x^2}{2}+x\). For
\(\int\dfrac{x}{x^2+1}\,dx\) let \(u=x^2+1\), \(du=2x\,dx\), giving
\(\dfrac{1}{2}\ln(x^2+1)\). For \(\int\dfrac{2}{x-1}\,dx=2\ln|x-1|\).

\smallskip

\textbf{Step 12.} Combine:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{x^4+3x^2-x+1}{(x-1)(x^2+1)}\,dx=\dfrac{x^2}{2}+x+\dfrac{1}{2}\ln(x^2+1)+2\ln|x-1|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 13.} Verify at \(x=2\): the integrand is
\(\dfrac{16+12-2+1}{(1)(5)}=\dfrac{27}{5}=5.4\). The derivative of the
answer is \(2+1+\dfrac{2}{5}+\dfrac{2}{1}=5.4\).

\textbf{Answer.} \(\dfrac{x^2}{2}+x+\dfrac{1}{2}\ln(x^2+1)+2\ln|x-1|+C\)
\end{solbox}
\vspace{4pt}

\vspace{6pt}\noindent{\bfseries\large The Weierstrass Substitution}\par\vspace{2pt}

**20.** Use $t=\tan\left(\dfrac{x}{2}\right)$ to evaluate $$\int\dfrac{1}{1+\sin x}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} Use the Weierstrass substitution
\(t=\tan\left(\dfrac{x}{2}\right)\) with \(\sin x=\dfrac{2t}{1+t^2}\)
and \(dx=\dfrac{2\,dt}{1+t^2}\).

\smallskip

\textbf{Step 2.} Rewrite the denominator over the common denominator
\(1+t^2\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$1+\sin x=1+\dfrac{2t}{1+t^2}=\dfrac{1+t^2+2t}{1+t^2}=\dfrac{(1+t)^2}{1+t^2},$\end{adjustbox}\par\noindent 
using the perfect square \(t^2+2t+1=(t+1)^2\).

\smallskip

\textbf{Step 3.} Substitute and take the reciprocal:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1+t^2}{(1+t)^2}\cdot\dfrac{2\,dt}{1+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Cancel \(1+t^2\): \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{2\,dt}{(1+t)^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} This needs no partial fractions. Let \(u=1+t\),
\(du=dt\): \(2\int u^{-2}\,du\).

\smallskip

\textbf{Step 6.} By the power rule
\(\int u^{-2}\,du=\dfrac{u^{-1}}{-1}=-\dfrac{1}{u}\), so the integral is
\(-\dfrac{2}{u}=-\dfrac{2}{1+t}\).

\smallskip

\textbf{Step 7.} Substitute back \(t=\tan\left(\dfrac{x}{2}\right)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1}{1+\sin x}\,dx=-\dfrac{2}{1+\tan(x/2)}+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 8.} Verify by differentiating, using
\(\dfrac{dt}{dx}=\dfrac{1+t^2}{2}\):
\(\dfrac{d}{dx}\left[-\dfrac{2}{1+t}\right]=\dfrac{2}{(1+t)^2}\cdot\dfrac{1+t^2}{2}=\dfrac{1+t^2}{(1+t)^2}\),
which equals \(\dfrac{1}{1+\sin x}\) by the second step.

\textbf{Answer.} \(-\dfrac{2}{1+\tan(x/2)}+C\)
\end{solbox}
\vspace{4pt}

**21.** Use $t=\tan\left(\dfrac{x}{2}\right)$ to evaluate $$\int_0^{\pi/2}\dfrac{1}{1+\sin x+\cos x}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} The denominator mixes \(\sin x\) and \(\cos x\), so use
the Weierstrass substitution \(t=\tan\left(\dfrac{x}{2}\right)\), with
\(\sin x=\dfrac{2t}{1+t^2}\), \(\cos x=\dfrac{1-t^2}{1+t^2}\) and
\(dx=\dfrac{2\,dt}{1+t^2}\).

\smallskip

\textbf{Step 2.} Change the limits. When \(x=0\): \(t=\tan 0=0\). When
\(x=\dfrac{\pi}{2}\): \(t=\tan\dfrac{\pi}{4}=1\). The function
\(\tan\left(\dfrac{x}{2}\right)\) is continuous on
\(\left[0,\dfrac{\pi}{2}\right]\), so the substitution is valid on the
whole interval.

\smallskip

\textbf{Step 3.} Rewrite the denominator over \(1+t^2\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$1+\sin x+\cos x=\dfrac{(1+t^2)+2t+(1-t^2)}{1+t^2}=\dfrac{2+2t}{1+t^2}=\dfrac{2(1+t)}{1+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Substitute and take the reciprocal:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int_0^1\dfrac{1+t^2}{2(1+t)}\cdot\dfrac{2\,dt}{1+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Cancel the factor \(1+t^2\) and the factor \(2\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int_0^1\dfrac{dt}{1+t}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Integrate with \(u=1+t\), \(du=dt\):
\(\int\dfrac{dt}{1+t}=\ln|1+t|\).

\smallskip

\textbf{Step 7.} Evaluate between the new limits:
\(\ln(1+1)-\ln(1+0)=\ln 2-\ln 1=\ln 2-0=\ln 2\).

\smallskip

\textbf{Step 8.} Numerical check: \(\ln 2\approx0.6931\). At \(x=0\) the
integrand is \(\dfrac{1}{0+1}=1\), at \(x=\dfrac{\pi}{2}\) it is also
\(\dfrac{1}{1+0}=1\), and at \(x=\dfrac{\pi}{4}\) it is
\(\dfrac{1}{1+\sqrt{2}}\approx0.414\). The average is near \(0.44\), and
\(0.44\times\dfrac{\pi}{2}\approx0.69\), consistent with \(\ln 2\).

\textbf{Answer.} \(\ln 2\approx 0.6931\)
\end{solbox}
\vspace{4pt}

**22.** Use $t=\tan\left(\dfrac{x}{2}\right)$ to evaluate $$\int\dfrac{1}{3+5\cos x}\,dx,$$ and simplify the resulting expression fully.

\begin{solbox}\sollabel

\textbf{Step 1.} Use \(t=\tan\left(\dfrac{x}{2}\right)\) with
\(\cos x=\dfrac{1-t^2}{1+t^2}\) and \(dx=\dfrac{2\,dt}{1+t^2}\).

\smallskip

\textbf{Step 2.} Rewrite the denominator over \(1+t^2\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$3+5\cos x=\dfrac{3(1+t^2)+5(1-t^2)}{1+t^2}=\dfrac{3+3t^2+5-5t^2}{1+t^2}=\dfrac{8-2t^2}{1+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Substitute and take the reciprocal:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1+t^2}{8-2t^2}\cdot\dfrac{2\,dt}{1+t^2}=\int\dfrac{2\,dt}{8-2t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Factor \(2\) out of the denominator and cancel:
\(\dfrac{2}{8-2t^2}=\dfrac{2}{2(4-t^2)}=\dfrac{1}{4-t^2}\), so the
integral is \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{dt}{4-t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Decide between arctangent and logarithm: \(4-t^2\) is a
difference of squares and factors over the reals, \(4-t^2=(2-t)(2+t)\),
so partial fractions will give logarithms.

\smallskip

\textbf{Step 6.} Set up
\(\dfrac{1}{(2-t)(2+t)}=\dfrac{A}{2-t}+\dfrac{B}{2+t}\), so
\(1=A(2+t)+B(2-t)\).

\smallskip

\textbf{Step 7.} Substitute \(t=2\): \(1=A(4)\), so \(A=\dfrac{1}{4}\).
Substitute \(t=-2\): \(1=B(4)\), so \(B=\dfrac{1}{4}\). Check:
\(\dfrac{1}{4}(2+t)+\dfrac{1}{4}(2-t)=\dfrac{4}{4}=1\).

\smallskip

\textbf{Step 8.} Integrate: \(\int\dfrac{dt}{2+t}=\ln|2+t|\) and
\(\int\dfrac{dt}{2-t}=-\ln|2-t|\) (let \(u=2-t\), \(du=-dt\)). Hence
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{dt}{4-t^2}=\dfrac{1}{4}\ln|2+t|-\dfrac{1}{4}\ln|2-t|=\dfrac{1}{4}\ln\left|\dfrac{2+t}{2-t}\right|.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Substitute back \(t=\tan\left(\dfrac{x}{2}\right)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{dx}{3+5\cos x}=\dfrac{1}{4}\ln\left|\dfrac{2+\tan(x/2)}{2-\tan(x/2)}\right|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} Verify by differentiating, using
\(\dfrac{dt}{dx}=\dfrac{1+t^2}{2}\):
\(\dfrac{1}{4}\left(\dfrac{1}{2+t}+\dfrac{1}{2-t}\right)\dfrac{1+t^2}{2}=\dfrac{1}{4}\cdot\dfrac{4}{4-t^2}\cdot\dfrac{1+t^2}{2}=\dfrac{1+t^2}{2(4-t^2)}=\dfrac{1+t^2}{8-2t^2}=\dfrac{1}{3+5\cos x}\)
by the second step.

\textbf{Answer.}
\(\dfrac{1}{4}\ln\left|\dfrac{2+\tan(x/2)}{2-\tan(x/2)}\right|+C\)
\end{solbox}
\vspace{4pt}

**23.** Use $t=\tan\left(\dfrac{x}{2}\right)$ to evaluate $$\int\dfrac{1}{2+\sin x}\,dx.$$

\begin{solbox}\sollabel

\textbf{Step 1.} Use \(t=\tan\left(\dfrac{x}{2}\right)\) with
\(\sin x=\dfrac{2t}{1+t^2}\) and \(dx=\dfrac{2\,dt}{1+t^2}\).

\smallskip

\textbf{Step 2.} Rewrite the denominator over \(1+t^2\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$2+\sin x=\dfrac{2(1+t^2)+2t}{1+t^2}=\dfrac{2t^2+2t+2}{1+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} Substitute and take the reciprocal:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1+t^2}{2t^2+2t+2}\cdot\dfrac{2\,dt}{1+t^2}=\int\dfrac{2\,dt}{2t^2+2t+2}=\int\dfrac{dt}{t^2+t+1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 4.} Check the discriminant of \(t^2+t+1\):
\(b^2-4ac=1-4=-3<0\), so it does not factor over the reals and the
result will be an arctangent.

\smallskip

\textbf{Step 5.} Complete the square:
\(t^2+t+1=\left(t+\dfrac{1}{2}\right)^2-\dfrac{1}{4}+1=\left(t+\dfrac{1}{2}\right)^2+\dfrac{3}{4}\).

\smallskip

\textbf{Step 6.} Let \(u=t+\dfrac{1}{2}\), \(du=dt\), and
\(a=\dfrac{\sqrt{3}}{2}\) (since \(a^2=\dfrac{3}{4}\)). Use
\(\int\dfrac{du}{u^2+a^2}=\dfrac{1}{a}\arctan\left(\dfrac{u}{a}\right)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{dt}{\left(t+\frac{1}{2}\right)^2+\frac{3}{4}}=\dfrac{2}{\sqrt{3}}\arctan\left(\dfrac{t+\frac{1}{2}}{\frac{\sqrt{3}}{2}}\right).$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Simplify the argument by multiplying top and bottom by
\(2\):
\(\dfrac{t+\frac{1}{2}}{\frac{\sqrt{3}}{2}}=\dfrac{2t+1}{\sqrt{3}}\).

\smallskip

\textbf{Step 8.} Substitute back \(t=\tan\left(\dfrac{x}{2}\right)\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{dx}{2+\sin x}=\dfrac{2}{\sqrt{3}}\arctan\left(\dfrac{2\tan(x/2)+1}{\sqrt{3}}\right)+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 9.} Verify by differentiating, using
\(\dfrac{dt}{dx}=\dfrac{1+t^2}{2}\):
\(\dfrac{2}{\sqrt{3}}\cdot\dfrac{1}{1+\frac{(2t+1)^2}{3}}\cdot\dfrac{2}{\sqrt{3}}\cdot\dfrac{1+t^2}{2}=\dfrac{4}{3}\cdot\dfrac{3}{3+(2t+1)^2}\cdot\dfrac{1+t^2}{2}=\dfrac{2(1+t^2)}{4t^2+4t+4}=\dfrac{1+t^2}{2t^2+2t+2}\),
which equals \(\dfrac{1}{2+\sin x}\) by the second step.

\textbf{Answer.}
\(\dfrac{2}{\sqrt{3}}\arctan\left(\dfrac{2\tan(x/2)+1}{\sqrt{3}}\right)+C\)
\end{solbox}
\vspace{4pt}

**24.** Show that $\displaystyle\int\sec x\,dx$ can be evaluated with the substitution $t=\tan\left(\dfrac{x}{2}\right)$, and confirm that the result agrees with the memorised formula $\ln|\sec x+\tan x|+C$.

\begin{solbox}\sollabel

\textbf{Step 1.} Write the integrand as a rational function of
\(\cos x\): \(\sec x=\dfrac{1}{\cos x}\). Use
\(t=\tan\left(\dfrac{x}{2}\right)\) with \(\cos x=\dfrac{1-t^2}{1+t^2}\)
and \(dx=\dfrac{2\,dt}{1+t^2}\).

\smallskip

\textbf{Step 2.} Then \(\sec x=\dfrac{1+t^2}{1-t^2}\), and
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\sec x\,dx=\int\dfrac{1+t^2}{1-t^2}\cdot\dfrac{2\,dt}{1+t^2}=\int\dfrac{2\,dt}{1-t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 3.} The denominator is a difference of squares,
\(1-t^2=(1-t)(1+t)\), so use partial fractions:
\(\dfrac{2}{(1-t)(1+t)}=\dfrac{A}{1-t}+\dfrac{B}{1+t}\), giving
\(2=A(1+t)+B(1-t)\).

\smallskip

\textbf{Step 4.} Substitute \(t=1\): \(2=A(2)\), so \(A=1\). Substitute
\(t=-1\): \(2=B(2)\), so \(B=1\). Check: \((1+t)+(1-t)=2\). So
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{2}{1-t^2}=\dfrac{1}{1-t}+\dfrac{1}{1+t}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 5.} Integrate: \(\int\dfrac{dt}{1+t}=\ln|1+t|\) and
\(\int\dfrac{dt}{1-t}=-\ln|1-t|\) (let \(u=1-t\), \(du=-dt\)). Therefore
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\sec x\,dx=\ln|1+t|-\ln|1-t|+C=\ln\left|\dfrac{1+t}{1-t}\right|+C=\ln\left|\dfrac{1+\tan(x/2)}{1-\tan(x/2)}\right|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 6.} Now show this equals \(\ln|\sec x+\tan x|\). Write
\(c=\cos\left(\dfrac{x}{2}\right)\) and
\(s=\sin\left(\dfrac{x}{2}\right)\), so \(t=\dfrac{s}{c}\). Then
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{1+t}{1-t}=\dfrac{1+\frac{s}{c}}{1-\frac{s}{c}}=\dfrac{\frac{c+s}{c}}{\frac{c-s}{c}}=\dfrac{c+s}{c-s}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Multiply numerator and denominator by \(c+s\) (allowed
whenever \(c+s\neq0\)):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{c+s}{c-s}=\dfrac{(c+s)^2}{(c-s)(c+s)}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 8.} Expand the numerator:
\((c+s)^2=c^2+2cs+s^2=(c^2+s^2)+2cs\). Use
\(c^2+s^2=\cos^2\left(\dfrac{x}{2}\right)+\sin^2\left(\dfrac{x}{2}\right)=1\)
(Pythagorean identity) and
\(2cs=2\sin\left(\dfrac{x}{2}\right)\cos\left(\dfrac{x}{2}\right)=\sin x\)
(double-angle identity). So the numerator is \(1+\sin x\).

\smallskip

\textbf{Step 9.} Expand the denominator with the difference of squares:
\((c-s)(c+s)=c^2-s^2=\cos^2\left(\dfrac{x}{2}\right)-\sin^2\left(\dfrac{x}{2}\right)=\cos x\)
(double-angle identity).

\smallskip

\textbf{Step 10.} Therefore
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\dfrac{1+t}{1-t}=\dfrac{1+\sin x}{\cos x}=\dfrac{1}{\cos x}+\dfrac{\sin x}{\cos x}=\sec x+\tan x.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 11.} This is an exact equality of the expressions inside
the logarithm, so
\(\ln\left|\dfrac{1+\tan(x/2)}{1-\tan(x/2)}\right|=\ln|\sec x+\tan x|\)
with no extra constant. The Weierstrass result and the memorised formula
are the same antiderivative: \par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\sec x\,dx=\ln|\sec x+\tan x|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 12.} Numerical check at \(x=0\): \(t=0\), so
\(\dfrac{1+0}{1-0}=1\), and \(\sec 0+\tan 0=1+0=1\). At
\(x=\dfrac{\pi}{2}\) both expressions are undefined, consistent with
\(\sec x\) having a vertical asymptote there.

\textbf{Answer.}
\(\ln\left|\dfrac{1+\tan(x/2)}{1-\tan(x/2)}\right|+C=\ln|\sec x+\tan x|+C\),
because
\(\dfrac{1+\tan(x/2)}{1-\tan(x/2)}=\dfrac{(c+s)^2}{c^2-s^2}=\dfrac{1+\sin x}{\cos x}=\sec x+\tan x\)
\end{solbox}
\vspace{4pt}

\vspace{6pt}\noindent{\bfseries\large Mixed Technique Identification}\par\vspace{2pt}

**25.** For each integral, state which single technique from Weeks 3 and 4 (substitution, integration by parts, trig-power identities, partial fractions, or the Weierstrass substitution) is the most efficient, explain why, and then evaluate it: (a) $\displaystyle\int\dfrac{x}{x^2-9}\,dx$; (b) $\displaystyle\int x^2\cos(x^3)\,dx$; (c) $\displaystyle\int\dfrac{1}{\sin x-\cos x}\,dx$; (d) $\displaystyle\int\sec^6x\,dx$.

\begin{solbox}\sollabel

\textbf{Step 1.} Part (a), choice: SUBSTITUTION with \(u=x^2-9\). The
numerator \(x\) is, up to the constant factor \(\dfrac{1}{2}\), the
derivative of the denominator \(x^2-9\) (since
\(\dfrac{d}{dx}(x^2-9)=2x\)), which is the pattern
\(\int\dfrac{u^{\prime}}{u}\). Partial fractions would also work after
factoring \(x^2-9=(x-3)(x+3)\) but takes more steps; the Weierstrass
substitution is irrelevant because there is no trigonometric function.

\smallskip

\textbf{Step 2.} Part (a), evaluation: let \(u=x^2-9\), so \(du=2x\,dx\)
and \(x\,dx=\dfrac{du}{2}\). Then
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{x}{x^2-9}\,dx=\dfrac{1}{2}\int\dfrac{du}{u}=\dfrac{1}{2}\ln|u|+C=\dfrac{1}{2}\ln|x^2-9|+C.$\end{adjustbox}\par\noindent 
Verify:
\(\dfrac{d}{dx}\left[\dfrac{1}{2}\ln|x^2-9|\right]=\dfrac{1}{2}\cdot\dfrac{2x}{x^2-9}=\dfrac{x}{x^2-9}\).

\smallskip

\textbf{Step 3.} Part (b), choice: SUBSTITUTION with \(u=x^3\). The
inner function of the cosine is \(x^3\) and its derivative is \(3x^2\),
and the factor \(x^2\) in front of the cosine is (up to the constant
\(3\)) exactly that derivative. Integration by parts would make the
integral harder, and no trigonometric-power identity helps because the
argument is \(x^3\), not \(x\).

\smallskip

\textbf{Step 4.} Part (b), evaluation: let \(u=x^3\), so \(du=3x^2\,dx\)
and \(x^2\,dx=\dfrac{du}{3}\). Then
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int x^2\cos(x^3)\,dx=\dfrac{1}{3}\int\cos u\,du=\dfrac{1}{3}\sin u+C=\dfrac{1}{3}\sin\left(x^3\right)+C.$\end{adjustbox}\par\noindent 
Verify:
\(\dfrac{d}{dx}\left[\dfrac{1}{3}\sin(x^3)\right]=\dfrac{1}{3}\cos(x^3)\cdot3x^2=x^2\cos(x^3)\).

\smallskip

\textbf{Step 5.} Part (c), choice: WEIERSTRASS SUBSTITUTION
\(t=\tan\left(\dfrac{x}{2}\right)\). The integrand is a rational
function of \(\sin x\) and \(\cos x\) with a sum \(\sin x-\cos x\) in
the denominator. There is no power of sine or cosine to peel off, no
secant or tangent structure, and no \(u\) whose derivative appears in
the numerator (the numerator is just \(1\)), so the odd-power,
even-power and sec/tan rules and plain substitution all fail. Partial
fractions alone does not apply because the integrand is not yet rational
in \(x\). The Weierstrass substitution always works for such integrands.

\smallskip

\textbf{Step 6.} Part (c), evaluation, step 1: use
\(\sin x=\dfrac{2t}{1+t^2}\), \(\cos x=\dfrac{1-t^2}{1+t^2}\),
\(dx=\dfrac{2\,dt}{1+t^2}\). Then
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\sin x-\cos x=\dfrac{2t-(1-t^2)}{1+t^2}=\dfrac{t^2+2t-1}{1+t^2}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 7.} Part (c), evaluation, step 2: substitute and take the
reciprocal:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1+t^2}{t^2+2t-1}\cdot\dfrac{2\,dt}{1+t^2}=\int\dfrac{2\,dt}{t^2+2t-1}.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 8.} Part (c), evaluation, step 3: the discriminant of
\(t^2+2t-1\) is \(4+4=8>0\), so it factors over the reals and the result
is a logarithm. Complete the square: \(t^2+2t-1=(t+1)^2-2\). Let
\(u=t+1\), \(a=\sqrt{2}\).

\smallskip

\textbf{Step 9.} Part (c), evaluation, step 4: use
\(\int\dfrac{du}{u^2-a^2}=\dfrac{1}{2a}\ln\left|\dfrac{u-a}{u+a}\right|\)
(from partial fractions
\(\dfrac{1}{u^2-a^2}=\dfrac{1}{2a}\left(\dfrac{1}{u-a}-\dfrac{1}{u+a}\right)\)).
With \(a=\sqrt{2}\), \(2\cdot\dfrac{1}{2\sqrt{2}}=\dfrac{1}{\sqrt{2}}\),
so
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{1}{\sin x-\cos x}\,dx=\dfrac{1}{\sqrt{2}}\ln\left|\dfrac{t+1-\sqrt{2}}{t+1+\sqrt{2}}\right|+C=\dfrac{1}{\sqrt{2}}\ln\left|\dfrac{\tan(x/2)+1-\sqrt{2}}{\tan(x/2)+1+\sqrt{2}}\right|+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 10.} Part (c), verification: differentiating with
\(\dfrac{dt}{dx}=\dfrac{1+t^2}{2}\) gives
\(\dfrac{1}{\sqrt{2}}\left(\dfrac{1}{t+1-\sqrt{2}}-\dfrac{1}{t+1+\sqrt{2}}\right)\dfrac{1+t^2}{2}=\dfrac{1}{\sqrt{2}}\cdot\dfrac{2\sqrt{2}}{(t+1)^2-2}\cdot\dfrac{1+t^2}{2}=\dfrac{1+t^2}{t^2+2t-1}=\dfrac{1}{\sin x-\cos x}\).

\smallskip

\textbf{Step 11.} Part (d), choice: the SEC/TAN even-secant rule (a
trig-power technique) with \(u=\tan x\). The power of secant is \(6\),
which is even, so one factor \(\sec^2x=\dfrac{d}{dx}\tan x\) can be
peeled off, and the remaining \(\sec^4x\) is converted to tangents by
\(\sec^2x=1+\tan^2x\). Using the Weierstrass substitution here would
produce a rational function of degree \(10\) in \(t\), far messier for
no benefit.

\smallskip

\textbf{Step 12.} Part (d), evaluation, step 1: write
\(\sec^6x=\sec^4x\cdot\sec^2x=(\sec^2x)^2\sec^2x=(1+\tan^2x)^2\sec^2x\).

\smallskip

\textbf{Step 13.} Part (d), evaluation, step 2: let \(u=\tan x\),
\(du=\sec^2x\,dx\). Expand \((1+u^2)^2=1+2u^2+u^4\). Then
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\sec^6x\,dx=\int(1+2u^2+u^4)\,du=u+\dfrac{2u^3}{3}+\dfrac{u^5}{5}+C.$\end{adjustbox}\par\noindent 

\smallskip

\textbf{Step 14.} Part (d), evaluation, step 3: substitute back:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\sec^6x\,dx=\tan x+\dfrac{2}{3}\tan^3x+\dfrac{1}{5}\tan^5x+C.$\end{adjustbox}\par\noindent 
Verify: the derivative is
\(\sec^2x+2\tan^2x\sec^2x+\tan^4x\sec^2x=\sec^2x\left(1+2\tan^2x+\tan^4x\right)=\sec^2x(1+\tan^2x)^2=\sec^2x\cdot\sec^4x=\sec^6x\).

\textbf{Answer.} (a) substitution: \(\dfrac{1}{2}\ln|x^2-9|+C\); (b)
substitution: \(\dfrac{1}{3}\sin\left(x^3\right)+C\); (c) Weierstrass
substitution:
\(\dfrac{1}{\sqrt{2}}\ln\left|\dfrac{\tan(x/2)+1-\sqrt{2}}{\tan(x/2)+1+\sqrt{2}}\right|+C\);
(d) even-secant rule with \(u=\tan x\):
\(\tan x+\dfrac{2}{3}\tan^3x+\dfrac{1}{5}\tan^5x+C\)
\end{solbox}
\vspace{4pt}

**26.** For each integral, name the most efficient single technique (substitution, integration by parts, trig-power identities, partial fractions, or the Weierstrass substitution) and then evaluate it: (a) $\displaystyle\int x\cos x\,dx$; (b) $\displaystyle\int\dfrac{1}{x^2-4x+3}\,dx$; (c) $\displaystyle\int\cos^3x\,dx$.

\begin{solbox}\sollabel

\textbf{Step 1.} Part (a), choice: INTEGRATION BY PARTS. The integrand
is a product of a polynomial \(x\) and a trigonometric function
\(\cos x\), and differentiating the polynomial factor simplifies it (its
derivative is \(1\)), which is the situation for which
\(\int u\,dv=uv-\int v\,du\) is designed. Substitution fails because
\(\cos x\) is not the derivative of any inner function appearing in
\(x\).

\smallskip

\textbf{Step 2.} Part (a), evaluation: choose \(u=x\) and
\(dv=\cos x\,dx\). Then \(du=dx\) and \(v=\sin x\). Apply the formula:
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int x\cos x\,dx=x\sin x-\int\sin x\,dx=x\sin x-(-\cos x)+C=x\sin x+\cos x+C.$\end{adjustbox}\par\noindent 
Verify: \(\dfrac{d}{dx}[x\sin x+\cos x]=\sin x+x\cos x-\sin x=x\cos x\).

\smallskip

\textbf{Step 3.} Part (b), choice: PARTIAL FRACTIONS. The integrand is a
rational function whose denominator is a quadratic that factors over the
reals, and the numerator is a constant, with no
derivative-of-the-denominator pattern for substitution to use. Factor
the quadratic: \(x^2-4x+3=(x-1)(x-3)\), since \((-1)+(-3)=-4\) and
\((-1)(-3)=3\).

\smallskip

\textbf{Step 4.} Part (b), evaluation, step 1: set up
\(\dfrac{1}{(x-1)(x-3)}=\dfrac{A}{x-1}+\dfrac{B}{x-3}\), so
\(1=A(x-3)+B(x-1)\). Substitute \(x=1\): \(1=A(-2)\), so
\(A=-\dfrac{1}{2}\). Substitute \(x=3\): \(1=B(2)\), so
\(B=\dfrac{1}{2}\). Check:
\(-\dfrac{1}{2}(x-3)+\dfrac{1}{2}(x-1)=\dfrac{-x+3+x-1}{2}=1\).

\smallskip

\textbf{Step 5.} Part (b), evaluation, step 2: integrate with
\(\int\dfrac{du}{u}=\ln|u|\):
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\dfrac{dx}{x^2-4x+3}=-\dfrac{1}{2}\ln|x-1|+\dfrac{1}{2}\ln|x-3|+C=\dfrac{1}{2}\ln\left|\dfrac{x-3}{x-1}\right|+C.$\end{adjustbox}\par\noindent 
Verify:
\(-\dfrac{1}{2(x-1)}+\dfrac{1}{2(x-3)}=\dfrac{-(x-3)+(x-1)}{2(x-1)(x-3)}=\dfrac{2}{2(x-1)(x-3)}=\dfrac{1}{x^2-4x+3}\).

\smallskip

\textbf{Step 6.} Part (c), choice: TRIG-POWER IDENTITIES (odd power of
cosine). The power of cosine is \(3\), which is odd, so one factor
\(\cos x\) can be peeled off and the remaining even power \(\cos^2x\)
converted using \(\cos^2x=1-\sin^2x\), after which \(u=\sin x\) works.
Substitution alone fails because \(\cos^3x\,dx\) is not \(du\) for any
simple \(u\) until the factor is split.

\smallskip

\textbf{Step 7.} Part (c), evaluation, step 1: write
\(\cos^3x=\cos^2x\cdot\cos x=(1-\sin^2x)\cos x\) using the Pythagorean
identity \(\sin^2x+\cos^2x=1\).

\smallskip

\textbf{Step 8.} Part (c), evaluation, step 2: let \(u=\sin x\), so
\(du=\cos x\,dx\). Then
\par\begin{adjustbox}{max width=\boxmathwidth,center}$\int\cos^3x\,dx=\int(1-u^2)\,du=u-\dfrac{u^3}{3}+C=\sin x-\dfrac{\sin^3x}{3}+C.$\end{adjustbox}\par\noindent 
Verify:
\(\dfrac{d}{dx}\left[\sin x-\dfrac{\sin^3x}{3}\right]=\cos x-\sin^2x\cos x=\cos x\left(1-\sin^2x\right)=\cos^3x\).

\textbf{Answer.} (a) integration by parts: \(x\sin x+\cos x+C\); (b)
partial fractions: \(\dfrac{1}{2}\ln\left|\dfrac{x-3}{x-1}\right|+C\);
(c) odd power of cosine with \(u=\sin x\):
\(\sin x-\dfrac{\sin^3x}{3}+C\)
\end{solbox}
\vspace{4pt}

