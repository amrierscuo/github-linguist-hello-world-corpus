@STATIC;1.0;t;387;{var the_class = objj_allocateClassPair(Nil, "Greeting"),
meta_class = the_class.isa;objj_registerClassPair(the_class);
class_addMethods(meta_class, [new objj_method(sel_getUid("say"), function $Greeting__say(self, _cmd)
{
    console.log("Hello, World!");
}

,["void"])]);
}
function main(args, namedArgs)
{
    (Greeting.isa.method_msgSend["say"] || _objj_forward)(Greeting, "say");
}
