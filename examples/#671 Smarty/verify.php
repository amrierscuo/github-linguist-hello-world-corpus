<?php
require getenv("SMARTY_HOME") . "/libs/Smarty.class.php";
$smarty = new Smarty();
$smarty->setCompileDir(getenv("SMARTY_BUILD"));
$smarty->assign("target", "World");
$result = $smarty->fetch("file:" . __DIR__ . "/hello.tpl");
if ($result !== "Hello, World!\n") throw new Exception("unexpected output");
echo $result;
