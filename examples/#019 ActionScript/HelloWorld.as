package
{
    import flash.display.Sprite;
    import flash.text.TextField;
    import flash.text.TextFieldAutoSize;

    public class HelloWorld extends Sprite
    {
        public function HelloWorld()
        {
            var greeting:TextField = new TextField();
            greeting.autoSize = TextFieldAutoSize.LEFT;
            greeting.text = "Hello World";
            addChild(greeting);
        }
    }
}
