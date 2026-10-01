const { buildAll } = require("./docs_engine");
const fs = require("fs");
const cfgs = [require("./wk6_docs_l63").GR11_L63, require("./wk6_docs_l64").GR11_L64,
              require("./wk6_docs_g10a").GR10_L212, require("./wk6_docs_g10b").GR10_L23];
(async () => {
  for (const c of cfgs) {
    await buildAll(c);
    const f = `Classwork_${c.slug}.docx`; if (fs.existsSync(f)) fs.unlinkSync(f);
  }
})();
