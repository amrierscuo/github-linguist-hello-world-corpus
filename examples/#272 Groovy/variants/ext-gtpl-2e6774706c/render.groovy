import groovy.text.SimpleTemplateEngine
print new SimpleTemplateEngine().createTemplate(new File("hello.gtpl")).make([name:"World"]).toString()
