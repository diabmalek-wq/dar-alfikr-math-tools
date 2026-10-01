import json, os
from mathgen import render
INK = "222E2D"; B = r"\underline{\qquad}"
E = {
 # Gr11 L6-3
 "k_l3a": (r"\log_5 25=" + B, INK), "k_l3b": (r"\log_3 1=" + B, INK),
 "k_l3c": (r"\log 50\approx" + B, INK), "k_l3d": (r"\ln 50\approx" + B, INK),
 "k_logb": (r"\log_b x", INK), "k_logbk": (r"\log_b\!\left(b^{k}\right)=k", INK),
 "k_l3p": (r"V(t)=500\,000\,(0.96)^{t}", INK),
 "k_l3t": (r"A=A_0\,b^{t}\ \Longrightarrow\ t=\log_b\!\left(\dfrac{A}{A_0}\right)", INK),
 # Gr11 L6-4
 "k_l4a": (r"f(x)=4^{x}", INK), "k_l4b": (r"g(x)=\log_5 x", INK), "k_l4c": (r"h(x)=\log_{10} x", INK),
 "k_l4p": (r"P(t)=10\cdot 3^{t/5}", INK), "k_l4i": (r"t(P)=5\log_3\!\left(\dfrac{P}{10}\right)", INK),
 "k_finv": (r"f^{-1}(9)\ \ne\ \dfrac{1}{f(9)}", INK),
 "k_logbase3": (r"y=\log_3 x", INK), "k_a3": (r"A(x)=\log_3 x", INK),
 # Gr10 L2-1+2
 "k_q1": (r"f(x)=3(x-5)^{2}-2", INK), "k_q2": (r"g(x)=-2(x+1)^{2}+6", INK),
 "k_q3": (r"h(x)=\dfrac{1}{2}(x-4)^{2}+1", INK),
 "k_q4": (r"\text{vertex}\ (2,-3),\ a=1", INK), "k_q5": (r"\text{vertex}\ (-1,4),\ \text{through}\ (0,2)", INK),
 "k_q6": (r"f(x)=x^{2}-4x+3", INK),
 "k_qj": (r"h(x)=-(x-2)^{2}+5", INK), "k_qj2": (r"h_2(x)=-\dfrac{2}{3}(x-3)^{2}+6", INK),
 "k_qform": (r"f(x)=a(x-h)^{2}+k=ax^{2}-2ahx+\left(ah^{2}+k\right)", INK),
 # Gr10 L2-3
 "k_r1": (r"f(x)=(x+3)(x-2)", INK), "k_r2": (r"x^{2}-7x+12=0", INK), "k_r3": (r"x^{2}+2x=0", INK),
 "k_r4": (r"g(x)=(x-1)(x+5)", INK), "k_r5": (r"x^{2}+x-6=0", INK), "k_r6": (r"h(x)=(x+4)(x+1)", INK),
 "k_ra": (r"h(x)=-\dfrac{1}{4}\,x(x-8)", INK), "k_ra2": (r"h_2(x)=-\dfrac{1}{5}\,x(x-10)", INK),
 "k_rtrap": (r"(x-2)(x-3)=6", INK), "k_rdef": (r"f(x)=a(x-p)(x-q)", INK),
 "k_rzp": (r"a\cdot b=0\ \Longrightarrow\ a=0\ \text{or}\ b=0", INK),
}
render(E, "wk6doc", "math_wk6doc")
M = {}
for d in ("math_w6l3_doc", "math_w6l4_doc", "math_g10q12_doc", "math_g10q3_doc", "math_wk6doc_doc"):
    M.update(json.load(open(os.path.join(d, "_index.json"))))
os.makedirs("math_wk6_doc", exist_ok=True)
json.dump(M, open("math_wk6_doc/_index.json", "w"), indent=1)
print(len(M), "merged")
