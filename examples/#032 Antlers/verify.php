<?php
// Execute this file at the root of a Statamic application.
require __DIR__ . '/vendor/autoload.php';
$app = require __DIR__ . '/bootstrap/app.php';
$app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();
$template = file_get_contents(__DIR__ . '/hello.antlers.html');
$output = (string) Statamic\Facades\Antlers::parse($template, ['audience' => 'World']);
if ($output !== "<p>Hello, World!</p>\n") {
    fwrite(STDERR, "Unexpected rendered output: " . var_export($output, true) . "\n");
    exit(1);
}
echo $output;
