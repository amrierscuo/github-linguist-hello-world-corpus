<?php
// Copy beside vendor/ and bootstrap/ at the root of a Laravel application.
require __DIR__ . '/vendor/autoload.php';
$app = require __DIR__ . '/bootstrap/app.php';
$app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();
$source = file_get_contents(__DIR__ . '/hello.blade.php');
$output = Illuminate\Support\Facades\Blade::render($source, ['audience' => 'World']);
if ($output !== "<p>Hello, World!</p>\n") {
    fwrite(STDERR, "Unexpected Blade output: " . var_export($output, true) . "\n");
    exit(1);
}
echo $output;
