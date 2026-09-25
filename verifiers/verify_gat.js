// dump the two sets so the answers can be checked independently in Python
const fs = require("fs");
const src = fs.readFileSync("gat_worksheets.js", "utf8")
  .replace('const { buildSet } = require("./exam_engine");', "const buildSet = async () => {};")
  .replace(/\(async \(\) => \{[\s\S]*$/, "");
const mod = { exports: {} };
new Function("module", "exports", "require", src + "\nmodule.exports = { W2, W4 };")(mod, mod.exports, require);
const out = {};
for (const [name, cfg] of Object.entries(mod.exports)) {
  out[name] = cfg.items.map((it, i) => ({
    n: i + 1, code: it.code,
    ans: typeof it.opts[it.ans] === "string" ? it.opts[it.ans] : it.opts[it.ans].eq,
    letter: "ABCD"[it.ans],
    nopts: new Set(it.opts.map(o => typeof o === "string" ? o : o.eq)).size,
    ntraps: (it.traps || []).length,
  }));
}
fs.writeFileSync("gat_dump.json", JSON.stringify(out, null, 1));
console.log("dumped");
