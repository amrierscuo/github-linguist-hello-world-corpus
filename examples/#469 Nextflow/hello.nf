nextflow.enable.dsl=2

process GREETING {
    output:
    stdout

    script:
    """
    printf 'Hello, World!\n'
    """
}

workflow {
    GREETING().view()
}
