<?php
$source = getenv('LATTE_SOURCE');
if ($source) {
    spl_autoload_register(function ($class) use ($source) {
        if (str_starts_with($class, 'Latte\\')) require $source . '/' . str_replace('\\', '/', substr($class, 6)) . '.php';
    });
} else {
    require 'vendor/autoload.php';
}
$engine = new Latte\Engine;
$actual = $engine->renderToString(__DIR__ . '/hello.latte', ['audience' => 'World']);
if (trim($actual) !== '<p>Hello, World!</p>') throw new RuntimeException('Unexpected rendering');
echo $actual;
