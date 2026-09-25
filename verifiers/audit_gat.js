const fs = require("fs");
function load(file, names) {
  const src = fs.readFileSync(file, "utf8")
    .replace('const { buildSet } = require("./exam_engine");', "const buildSet = async () => {};")
    .replace(/\(async \(\) => \{[\s\S]*$/, "").replace(/^for \(const \[name, cfg\][\s\S]*$/m, "");
  const m = { exports: {} };
  new Function("module","exports","require", src + `\nmodule.exports = { ${names.join(",")} };`)(m, m.exports, require);
  return m.exports;
}
const all = { ...load("gat_worksheets.js", ["W2","W4"]), ...load("gat_worksheets2.js", ["W3","W5"]) };
const out = {};
for (const [wk, cfg] of Object.entries(all)) {
  out[wk] = { header: cfg.headerLine, timing: cfg.timing, n: cfg.items.length,
    items: cfg.items.map((it, i) => ({ n: i+1, code: it.code, lvl: it.lvl,
      stem: it.stem, note: it.note || "", fig: it.fig || "",
      opts: it.opts.map(o => typeof o === "string" ? o : "EQ:" + o.eq), ans: it.ans })) };
}
fs.writeFileSync("gat_audit.json", JSON.stringify(out, null, 1));
console.log("dumped", Object.values(out).reduce((a,b)=>a+b.n,0), "items");
