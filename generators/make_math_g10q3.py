from mathgen import render
INK, WHITE = "222E2D", "FFFFFF"
B = r"\underline{\qquad}"
E = {
 "c_title_w": (r"f(x)=a(x-p)(x-q)", WHITE),
 "c_p1": (r"f(x)=x^{2}-6x+5", INK),
 "c_p2": (r"f(x)=2(x-3)^{2}-1", INK),
 "c_p3": (r"(x+2)(x-5)=x^{2}-3x-10", INK),
 "c_co_w": (r"x^{2}-2x-3\ =\ (x+1)(x-3)", WHITE),
 "c_d1": (r"(x+2)(x-5)=" + B, INK),
 "c_d2": (r"f(x)=x^{2}-4.\quad f(2)=" + B, INK),
 "c_d3": (r"a\cdot b=0\ \Rightarrow\ " + B, INK),
 "c_d4": (r"x^{2}+5x+6=" + B, INK),
 "c_d5": (r"f(x)=x^{2}-2x-3:\ \text{axis}\ x=" + B, INK),
 "c_f1": (r"f(x)=(x+1)(x-3)", INK),
 "c_z1": (r"x^{2}-2x-3=0", INK),
 "c_z2": (r"(x+1)(x-3)=0", INK),
 "c_z3": (r"x+1=0\ \ \text{or}\ \ x-3=0", INK),
 "c_z4": (r"x=-1\ \ \text{or}\ \ x=3", INK),
 "c_i1": (r"f(x)>0\ \text{when}\ x<-1\ \text{or}\ x>3", INK),
 "c_i2": (r"f(x)<0\ \text{when}\ -1<x<3", INK),
 "c_qc": (r"f(x)=(x-4)(x+2)", INK),
 "c_g1": (r"x^{2}+5x+6=0", INK),
 "c_g2": (r"f(x)=(x-1)(x-5)", INK),
 "c_ws1": (r"f(x)=(x+3)(x-2)", INK),
 "c_ws3": (r"f(x)=2(x+2)(x-4)", INK),
 "c_model_w": (r"h(x)=-\tfrac{1}{4}\,x(x-8)", WHITE),
 "c_gate_w": (r"\text{zeros}\ -3\ \text{and}\ 1,\ \text{through}\ (0,6)", WHITE),
}
render(E, "g10q3", "math_g10q3")
