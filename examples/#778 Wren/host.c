#include <stdio.h>
#include <stdlib.h>
#include "wren.h"
static void writeText(WrenVM* vm,const char* text){(void)vm;fputs(text,stdout);}
static void errorText(WrenVM* vm,WrenErrorType kind,const char* module,int line,const char* message){(void)vm;fprintf(stderr,"Wren %d %s:%d %s\n",kind,module?module:"",line,message);}
int main(int argc,char**argv){
 if(argc!=2)return 2;FILE*f=fopen(argv[1],"rb");if(!f)return 3;
 fseek(f,0,SEEK_END);long length=ftell(f);rewind(f);char*source=calloc((size_t)length+1,1);if(!source)return 4;
 if(fread(source,1,(size_t)length,f)!=(size_t)length)return 5;fclose(f);
 WrenConfiguration config;wrenInitConfiguration(&config);config.writeFn=writeText;config.errorFn=errorText;
 WrenVM*vm=wrenNewVM(&config);WrenInterpretResult result=wrenInterpret(vm,"main",source);
 wrenFreeVM(vm);free(source);return result==WREN_RESULT_SUCCESS?0:1;
}
