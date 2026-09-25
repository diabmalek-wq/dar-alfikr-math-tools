const Module=require("module"),orig=Module.prototype.require;
Module.prototype.require=function(i){if(i==="./exam_engine")return{buildSet:c=>{global.__c=c}};return orig.apply(this,arguments)};
require(process.argv[2]);const c=global.__c;let bad=0;
c.items.forEach((it,i)=>{
  if(!(it.ans>=0&&it.ans<it.opts.length))console.log("  ans out of range at",i+1),bad++;
  if(it.opts.length!==4)console.log("  not 4 options at",i+1),bad++;
  const keys=it.opts.map(o=>typeof o==="string"?o:o.eq);
  if(new Set(keys).size!==keys.length)console.log("  duplicate option at",i+1),bad++;
  if(!it.why||!it.traps||it.traps.length!==3)console.log("  missing why/traps at",i+1),bad++;
});
console.log(" ",process.argv[2],bad?bad+" PROBLEMS":"clean ("+c.items.length+" items)");
