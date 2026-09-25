#!/usr/bin/env python3
import os, re, csv, zipfile, subprocess, shutil, html
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path.cwd()
OUT = ROOT / "ANALIZA_WYDOBYTA"
OUT.mkdir(exist_ok=True)

KEYWORDS = [
    "wniosek","swz","specyfik","oglosz","ogłosz","otwar","ofert","wezwan","uzup","uzupeł",
    "wybor","wybór","wynik","umow","umów","protok","wadium","zabezpiec","wykonan","odbior","odbiór",
    "informac","odpowiedz","odpowiedź","zmian","aneks","krk","oswiadc","oświadc","szacunk","plan"
]
TEXT_EXTS = {".txt",".md",".csv",".xml",".html",".htm",".rtf",".json"}

def safe(s):
    s = re.sub(r'[^\w.\-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ ]+', '_', s)
    return re.sub(r'\s+', ' ', s).strip()[:180]

def xml_text(data):
    try:
        root=ET.fromstring(data)
        return "\n".join(t.strip() for t in root.itertext() if t and t.strip())
    except Exception:
        return ""

def extract_docx(p):
    try:
        with zipfile.ZipFile(p) as z:
            parts=[]
            for name in z.namelist():
                if name.startswith("word/") and name.endswith(".xml") and (
                    "document.xml" in name or "header" in name or "footer" in name or "footnotes" in name or "endnotes" in name
                ):
                    parts.append(xml_text(z.read(name)))
            return "\n".join(parts)
    except Exception as e:
        return f"[BŁĄD DOCX: {e}]"

def extract_xlsx(p):
    try:
        with zipfile.ZipFile(p) as z:
            shared=[]
            if "xl/sharedStrings.xml" in z.namelist():
                root=ET.fromstring(z.read("xl/sharedStrings.xml"))
                shared=[" ".join(x.itertext()).strip() for x in root]
            out=[]
            for name in sorted(n for n in z.namelist() if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")):
                root=ET.fromstring(z.read(name))
                vals=[]
                for c in root.iter():
                    if c.tag.endswith("}c"):
                        typ=c.attrib.get("t")
                        v=next((x for x in c if x.tag.endswith("}v")),None)
                        if v is None or v.text is None: continue
                        val=v.text
                        if typ=="s":
                            try: val=shared[int(val)]
                            except: pass
                        vals.append(val)
                out.append(f"### {name}\n"+"\n".join(vals))
            return "\n\n".join(out)
    except Exception as e:
        return f"[BŁĄD XLSX: {e}]"

def extract_pdf(p):
    try:
        q=subprocess.run(["pdftotext","-layout",str(p),"-"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=90)
        return q.stdout.decode("utf-8","ignore")
    except Exception as e:
        return f"[BŁĄD PDF: {e}]"

def extract_doc(p):
    for cmd in (["antiword",str(p)],["catdoc",str(p)]):
        if shutil.which(cmd[0]):
            try:
                q=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60)
                text=q.stdout.decode("utf-8","ignore")
                if text.strip(): return text
            except Exception: pass
    try:
        q=subprocess.run(["strings","-el",str(p)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60)
        return q.stdout.decode("utf-8","ignore")
    except Exception as e:
        return f"[BŁĄD DOC: {e}]"

def read_text(p):
    ext=p.suffix.lower()
    if ext==".docx": return extract_docx(p)
    if ext==".xlsx": return extract_xlsx(p)
    if ext==".pdf": return extract_pdf(p)
    if ext==".doc": return extract_doc(p)
    if ext in TEXT_EXTS:
        b=p.read_bytes()
        for enc in ("utf-8","cp1250","latin1"):
            try: return b.decode(enc)
            except: pass
    return ""

rows=[]
for zpath in sorted(ROOT.glob("RIN.271.1.*.zip")):
    post = zpath.stem
    tmp=ROOT/"_extract_tmp"/safe(post)
    if tmp.exists(): shutil.rmtree(tmp)
    tmp.mkdir(parents=True,exist_ok=True)
    try:
        with zipfile.ZipFile(zpath) as z:
            z.extractall(tmp)
    except Exception as e:
        rows.append([post,str(zpath.name),"ZIP_ERROR",0,str(e)])
        continue

    postout=OUT/safe(post)
    postout.mkdir(parents=True,exist_ok=True)
    manifest=[]
    docs=[]
    for p in sorted(x for x in tmp.rglob("*") if x.is_file()):
        rel=str(p.relative_to(tmp))
        ext=p.suffix.lower()
        low=rel.lower()
        relevant = any(k in low for k in KEYWORDS)
        text=""
        if ext in TEXT_EXTS or ext in {".docx",".xlsx",".pdf",".doc"}:
            text=read_text(p)
        manifest.append([rel,ext,p.stat().st_size,len(text),relevant])
        if text.strip():
            # Zachowaj pełny tekst do maks. 300k znaków na dokument, do analizy.
            t=text[:300000]
            outname=safe(rel.replace("/","__"))+".txt"
            (postout/outname).write_text(
                f"ŹRÓDŁO: {post}\nPLIK: {rel}\nROZMIAR: {p.stat().st_size}\n\n{t}",
                encoding="utf-8"
            )
            docs.append((rel,outname,len(text),relevant))
    with (postout/"_MANIFEST.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter=';')
        w.writerow(["plik","ext","bytes","text_chars","relevant_name"])
        w.writerows(manifest)
    with (postout/"_INDEKS.txt").open("w",encoding="utf-8") as f:
        for rel,outname,n,relv in docs:
            f.write(f"{'*' if relv else '-'} {rel} -> {outname} ({n} znaków)\n")
    rows.extend([[post,*m] for m in manifest])

# Arkusz historyczny - tekstowa ekstrakcja
hist = ROOT/"Zestawienie postepowan do 2021 do 2024 roku.xlsx"
if hist.exists():
    (OUT/"ZESTAWIENIE_HISTORYCZNE.txt").write_text(extract_xlsx(hist),encoding="utf-8")

with (OUT/"MANIFEST_WSZYSTKO.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.writer(f,delimiter=';')
    w.writerow(["postepowanie","plik","ext","bytes","text_chars","relevant_name"])
    w.writerows(rows)

print(f"Wygenerowano {len(rows)} wpisów manifestu w {OUT}")

# trigger: 2026-09-25 analysis extraction
