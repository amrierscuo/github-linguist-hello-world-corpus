# #069 Blade

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Render a Blade template with audience = World and get the Hello, World! paragraph.

The fixture loads the autoloader and bootstrap/app.php, starts the console kernel, and calls the framework's Blade::render engine. Interpolation uses native HTML escaping. Checking the output does not substitute for the Blade parser.

## Toolchain and reproduction

Laravel 12.x con PHP compatibile e applicazione configurata; versione effettiva da registrare

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
Copiare hello.blade.php e verify.php nella root di un’app Laravel configurata, poi: php verify.php
```

## Expected result and status

stdout esatto <p>Hello, World!</p> seguito da newline; exit 0.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; no native parser or runtime has been performed for this item.

Commitments: PHP and a complete Laravel application are not prepared in this environment; the Blade engine has not been executed.

## Primary sources

- https://laravel.com/docs/12.x/blade

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.blade` | [hello.blade](variants/ext-blade-2e626c616465/hello.blade) created; verification pending |
| `.blade.php` | [hello.blade.php](hello.blade.php) created; verification pending |
