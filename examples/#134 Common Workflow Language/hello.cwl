cwlVersion: v1.2
class: CommandLineTool
baseCommand: echo
inputs:
  greeting:
    type: string
    default: "Hello, World!"
    inputBinding:
      position: 1
outputs:
  output:
    type: File
    outputBinding:
      glob: hello.txt
stdout: hello.txt
