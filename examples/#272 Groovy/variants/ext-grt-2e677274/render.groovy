import groovy.text.GStringTemplateEngine
print new GStringTemplateEngine().createTemplate(new File("hello.grt")).make([name:"World"]).toString()
