#!/usr/bin/env python3
"""Generate the verified q=3 figure as TikZ source, deterministic PDF, and PNG."""
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from affine_q3 import data, serialized

root = Path(__file__).resolve().parents[1]
out = root / 'paper/figures'
out.mkdir(parents=True, exist_ok=True)
points, supplies, selected = data()
# Exhaustive exact checks finish before any figure is exported.
record = serialized()
tex = [r'''\documentclass{article}
\usepackage[paperwidth=6.5in,paperheight=7.6in,margin=0in]{geometry}
\usepackage{tikz,fix-cm,amsmath,amssymb}
\pagestyle{empty}
\definecolor{blue}{HTML}{276185}
\definecolor{red}{HTML}{AD3E35}
\definecolor{ink}{HTML}{262626}
\definecolor{gray}{HTML}{666666}
\definecolor{green}{HTML}{35734A}
\begin{document}\noindent\sffamily
\begin{tikzpicture}[x=1pt,y=-1pt,every node/.style={inner sep=0pt,text=ink}]
\path[use as bounding box] (0,0) rectangle (467,530);
''']

def text(x, y, value, size=9, color='ink', anchor='west'):
    tex.append(r'\node[anchor=%s,text=%s,font=\sffamily\fontsize{%s}{%s}\selectfont] at (%s,%s) {%s};'
               % (anchor, color, size, size*1.3, x, y, value))

def line(x, y, xx, yy, color='black!12', width=.4):
    tex.append(r'\draw[%s,line width=%spt] (%s,%s)--(%s,%s);' % (color,width,x,y,xx,yy))

def dot(x, y, color, radius=2.1):
    tex.append(r'\fill[%s] (%s,%s) circle (%spt);' % (color,x,y,radius))

def box(x, y, xx, yy, color='red'):
    tex.append(r'\fill[%s,opacity=.09] (%s,%s) rectangle (%s,%s);' % (color,x,y,xx,yy))

text(3,12,r'The affine construction at $q=3$',14)
text(3,32,r'Nine points $(x,y)\in\mathbb F_3^2$, plus a common root $r$.',9,'gray')
text(3,56,'All nine supply edges',11)
xs = {(x,y):100+108*x+29*y for x in range(3) for y in range(3)}
box(51,98,69,268); box(198,98,277,268)
for point in sorted(selected):
    xx=xs[point]; box(xx-6,98,xx+6,268,'green')
text(21,88,r'$(a,b)$',8.5,anchor='center')
text(60,74,'root',8,anchor='center'); text(60,89,r'$r$',9,anchor='center')
for x in range(3):
    text(129+108*x,74,f'$x={x}$',9,'red' if x==1 else 'ink','center')
    for y in range(3):text(xs[x,y],89,str(y),8,'gray','center')
text(424,89,r'hits $T$',8.5,'green','center')
for i, ((a,b), edge) in enumerate(supplies.items()):
    yy=106+19*i; color='blue' if a==0 else 'gray'
    line(60,yy,374,yy)
    text(21,yy,f'$({a},{b})$',9,color,'center'); dot(60,yy,color)
    for point in sorted(edge):dot(xs[point],yy,'green' if point in selected else color)
    if edge & selected:dot(424,yy,'green')
for yy in [153.5,210.5]:line(3,yy,442,yy,'black!25')
text(3,286,r'Each row is $e_{a,b}=\{r\}\cup\{(x,ax+b):x\in\mathbb F_3\}$.',9)
text(3,303,r'Green strips mark $T$; the six green row markers show supplies hitting $T$.',8.5,'green')
line(3,318,460,318,'black!25')
text(3,340,'A column costs three',11)
text(217,340,'The all-cut comparison',11)
text(217,361,r'For every $T$: $P(\mathrm{column\ hit})\leq\frac53P(\mathrm{supply\ hit})$.',8.5)
text(217,383,r'Example: $T=\{(0,0),(1,0),(2,1)\}$.',9,'green')
# No spatial cut region: T is represented only by the marked table columns.
box(75,361,89,462)
for y in range(3):
    yy=455-42*y; line(40,yy,124,yy,'blue',1.2)
    for x in range(3):dot(40+42*x,yy,'red' if x==1 else 'ink')
    text(27,yy,str(y),8,'gray','east');text(134,yy,f'$L_{{0,{y}}}$',8,'blue')
for x in range(3):text(40+42*x,474,str(x),8,'gray','center')
text(82,358,r'$Q_1$',9,'red','center');text(143,474,r'$x$',8,'gray')
text(217,408,'Columns hit',9);text(373,408,r'$3/3=1$',10,'green')
text(217,430,'Supplies hit',9);text(373,430,r'$6/9=2/3$',10,'green')
text(217,455,r'Ratio: $\displaystyle\frac{1}{2/3}=\frac32<\frac53$.',11)
text(217,482,r'Worst cut at $q=3$: exact maximum $3/2$.',9,'green')
text(3,495,r'Each blue line plus $r$ is a unit-cost supply.',8.5,'blue')
text(3,513,r'Every supply hits $Q_1$ once, so $\delta(\{r\}\cup Q_1)=3$.',8.5)
text(217,504,r'All edges contain $r\notin T$: hitting means crossing.',8)
text(217,525,r'The finite check does not replace the general proof.',8,'gray')
tex.append(r'\end{tikzpicture}\end{document}')
source = '\n'.join(tex) + '\n'
compiler = os.environ.get('PDFLATEX','pdflatex')
renderer = os.environ.get('PDFTOPPM','pdftoppm')
env=dict(os.environ,SOURCE_DATE_EPOCH='1789257600',FORCE_SOURCE_DATE='1',TZ='UTC')
pdfs=[]; pngs=[]
for _ in range(2):
    with tempfile.TemporaryDirectory(prefix='affine-q3-') as tmp:
        work=Path(tmp); (work/'affine-q3.tex').write_text(source)
        for _ in range(2):
            result=subprocess.run([compiler,'-no-shell-escape','-halt-on-error','-interaction=nonstopmode','affine-q3.tex'],cwd=work,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            if result.returncode:raise SystemExit(result.stdout)
        log=(work/'affine-q3.log').read_text()
        bad=[row for row in log.splitlines() if any(s in row for s in ['Warning:', 'Overfull', 'Underfull'])]
        if bad:raise SystemExit('\n'.join(bad))
        subprocess.run([renderer,'-f','1','-singlefile','-r','180','-png','affine-q3.pdf','affine-q3'],cwd=work,check=True)
        pdfs.append((work/'affine-q3.pdf').read_bytes());pngs.append((work/'affine-q3.png').read_bytes())
if pdfs[0]!=pdfs[1] or pngs[0]!=pngs[1]:raise SystemExit('Figure builds differ')
for name,content in [('affine-q3.tex',source.encode()),('affine-q3.pdf',pdfs[0]),('affine-q3.png',pngs[0]),('affine-q3-checks.json',record.encode())]:
    (out/name).write_bytes(content)
print('PASS: exact 512-subset enumeration; two clean figure builds match (PDF and PNG)')
print('Figure PDF SHA-256: '+hashlib.sha256(pdfs[0]).hexdigest())
