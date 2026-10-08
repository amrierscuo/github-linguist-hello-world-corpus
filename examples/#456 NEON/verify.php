<?php
$library = realpath($argv[1]);
spl_autoload_register(function ($class) use ($library) {
    if (str_starts_with($class, 'Nette\\')) {
        $file = $library . '/src/' . str_replace('\\', '/', substr($class, 6)) . '.php';
        if (is_file($file)) require $file;
    }
});
$data = Nette\Neon\Neon::decode(file_get_contents($argv[2]));
if ($data !== ['message'=>'Hello, World!', 'language'=>'en']) throw new RuntimeException('Unexpected data');
echo $data['message'], "\n";
echo "PASS: genuine Nette NEON decoder and data model\n";
