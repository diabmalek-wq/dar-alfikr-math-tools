// Print every item next to the trick it will carry, so a shifted TRICKS array
// is visible instead of silently printing the wrong trick in the answer key.
const Module = require("module");
const orig = Module.prototype.require;
Module.prototype.require = function (id) {
  if (id === "./exam_engine") return { buildSet: (c) => { global.__cfg = c; } };
  return orig.apply(this, arguments);
};
require(process.argv[2]);
const c = global.__cfg;
c.items.forEach((it, i) => {
  const stem = (it.stem || "").replace(/\s+/g, " ").slice(0, 50);
  console.log(String(i + 1).padStart(2), (it.code || "").padEnd(11), stem.padEnd(52), "|", (it.trick || "").slice(0, 44));
});
