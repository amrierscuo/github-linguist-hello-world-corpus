#include <QCoreApplication>
#include <QScriptEngine>
#include <QFile>
#include <QTextStream>
int main(int argc,char **argv) { QCoreApplication app(argc,argv); QFile file("hello.qs"); if(!file.open(QIODevice::ReadOnly)) return 1; QScriptEngine engine; QScriptValue value=engine.evaluate(QString::fromUtf8(file.readAll()),"hello.qs"); if(engine.hasUncaughtException()) return 2; QTextStream(stdout)<<value.toString()<<"\n"; return 0; }
