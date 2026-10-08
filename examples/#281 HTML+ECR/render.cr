require "ecr/macros"

audience = "World"
rendered = ECR.render("hello.ecr")
raise "Unexpected rendering" unless rendered == "<p>Hello, World!</p>\n"
print rendered
