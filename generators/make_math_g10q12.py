from mathgen import render
INK, WHITE = "222E2D", "FFFFFF"
B = r"\underline{\qquad}"
E = {
 "b_title_w": (r"a(x-h)^{2}+k\ \longleftrightarrow\ ax^{2}+bx+c", WHITE),
 "b_p1": (r"y=(x+2)^{2}-5", INK),
 "b_p2": (r"f(x)=2x-6", INK),
 "b_p3": (r"(x-3)^{2}=x^{2}-6x+9", INK),
 "b_co_w": (r"a(x-h)^{2}+k\ =\ ax^{2}+bx+c", WHITE),
 "b_d1": (r"(x-3)^{2}=" + B, INK),
 "b_d2": (r"f(x)=2x^{2}-8x+3.\quad f(0)=" + B, INK),
 "b_d3": (r"y=(x+2)^{2}-5", INK),
 "b_d4": (r"y=x^{2}:\ \text{axis of symmetry}\ x=" + B, INK),
 "b_d5": (r"\text{Halfway between}\ x=1\ \text{and}\ x=5:\ x=" + B, INK),
 "b_w1": (r"f(x)=a(x+2)^{2}+5", INK),
 "b_w2": (r"-3=a(0+2)^{2}+5", INK),
 "b_w3": (r"-8=4a\ \Rightarrow\ a=-2", INK),
 "b_w4": (r"f(x)=-2(x+2)^{2}+5", INK),
 "b_axis": (r"x=-\dfrac{b}{2a}", INK),
 "b_vtx": (r"\left(-\dfrac{b}{2a},\ f\!\left(-\dfrac{b}{2a}\right)\right)", INK),
 "b_s2": (r"x=-\dfrac{-6}{2(1)}=3", INK),
 "b_s3": (r"f(3)=9-18+5=-4\ \Rightarrow\ (3,-4)", INK),
 "b_s4": (r"(0,5)\ \text{and its mirror}\ (6,5)", INK),
 "b_s5": (r"f(x)=(x-3)^{2}-4", INK),
 "b_qc": (r"f(x)=-3(x+4)^{2}+7", INK),
 "b_g1": (r"\text{vertex}\ (1,-2),\ a=3:\ f(x)=" + B, INK),
 "b_g2": (r"f(x)=2x^{2}+8x-3", INK),
 "b_ws1": (r"f(x)=3(x-5)^{2}-2", INK),
 "b_ws3": (r"f(x)=-x^{2}+4x+1", INK),
 "b_model_w": (r"h(x)=-(x-2)^{2}+5", WHITE),
 "b_gate_w": (r"\text{vertex}\ (-1,4),\ \text{through}\ (1,0)", WHITE),
}
render(E, "g10q12", "math_g10q12")
