
// 使用方法：
// 1. 表单 -> Javascript控制台 -> 粘贴下横线下面内容 -> 点击运行
// 2. 附加工具 -> 看到“联动⬇️”，“联动⬆️”


/*
// 1. 在右键菜单添加：联动向下
var d = app.activeDocs;
if (d && d.length >= 2) {
    d[0].pageNum += 1;
    d[1].pageNum += 1;
}
*/

/*
// 2. 在右键菜单添加：联动向上
var d = app.activeDocs;
if (d && d.length >= 2) {
    d[0].pageNum -= 1;
    d[1].pageNum -= 1;
}
*/

/*
(function nuclearHomeIntegration() {
    // 1. 执行物理锁死逻辑
    var ds = app.activeDocs;
    if (!ds || ds.length < 2) {
        console.println("❌ 扫描失败：未识别到并排文档。");
        return;
    }
    global.docSlot0 = ds[0];
    global.docSlot1 = ds[1];
    console.println("✅ 句柄已锁死：" + ds[0].documentFileName + " & " + ds[1].documentFileName);
    // 2. 定义翻页逻辑函数
    global.fnNext = function() { if(global.docSlot0 && global.docSlot1){ global.docSlot0.pageNum++; global.docSlot1.pageNum++; } };
    global.fnPrev = function() { if(global.docSlot0 && global.docSlot1){ global.docSlot0.pageNum--; global.docSlot1.pageNum--; } };
    // 3. 注册为“系统命令”，使其可以被添加到【主页】
    app.addMenuItem({
        cName: "cmd.syncNext",   // 命令ID
        cUser: "联动⬇️",    // 显示名称
        cParent: "View", 
        cExec: "global.fnNext()",
        cEnable: "event.rc = true;"
    });
    app.addMenuItem({
        cName: "cmd.syncPrev",
        cUser: "联动⬆️",
        cParent: "View", 
        cExec: "global.fnPrev()",
        cEnable: "event.rc = true;"
    });
    // 4. 同时保留快捷按钮（位于附加工具，作为备用）
    app.addToolButton({
        cName: "Btn_SyncNext",
        cExec: "global.fnNext()",
        cLabel: "联动⬇️",
        cEnable: "event.rc = true;"
    });
    
    app.addToolButton({
        cName: "Btn_SyncPrev",
        cExec: "global.fnPrev()",
        cLabel: "联动⬆️",
        cEnable: "event.rc = true;"
    });
    console.println(">>> 命令已注册，现在可以去【自定义功能区】将它们加入主页了。");
})();

*/