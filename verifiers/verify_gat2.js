const fs = require("fs");
const src = fs.readFileSync("gat_worksheets2.js", "utf8")
  .replace('const { buildSet } = require("./exam_engine");', "const buildSet = async () => {};")
  .replace(/\(async \(\) => \{[\s\S]*$/, "");
const mod = { exports: {} };
new Function("module", "exports", "require", src + "\nmodule.exports = { W3, W5 };")(mod, mod.exports, require);
const out = {};
for (const [name, cfg] of Object.entries(mod.exports)) {
  out[name] = cfg.items.map((it, i) => ({
    n: i + 1, code: it.code,
    ans: typeof it.opts[it.ans] === "string" ? it.opts[it.ans] : it.opts[it.ans].eq,
    nopts: new Set(it.opts.map(o => typeof o === "string" ? o : o.eq)).size,
    ntraps: (it.traps || []).length, trick: (it.trick || "").length,
    lvl: it.lvl,
  }));
}
fs.writeFileSync("gat2_dump.json", JSON.stringify(out, null, 1));
